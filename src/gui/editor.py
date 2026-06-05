import tkinter as tk
from tkinter import ttk, filedialog, messagebox, font
import subprocess
import sys
import os
import re

# Agrega src/ al path para importar el compilador
_SRC = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, _SRC)

from main import compile_file

# Colores del tema
BG       = "#1e1e2e"
BG_PANEL = "#2a2a3e"
FG       = "#cdd6f4"
ACCENT   = "#89b4fa"
ERR_COL  = "#f38ba8"
OK_COL   = "#a6e3a1"
LINE_BG  = "#181825"
LINE_FG  = "#585b70"
KWORD_COL= "#cba6f7"
STR_COL  = "#a6e3a1"
NUM_COL  = "#fab387"
CMT_COL  = "#6c7086"
SEL_BG   = "#45475a"

KEYWORDS = (
    "package", "func", "var", "type", "struct", "if", "else",
    "for", "switch", "case", "default", "return", "break", "continue",
    "append", "len", "cap", "println", "print", "true", "false", "int",
    "float64", "string", "bool", "rune",
)


class LineNumbers(tk.Canvas):
    def __init__(self, master, text_widget, **kw):
        super().__init__(master, **kw)
        self.text = text_widget
        self.text.bind("<<Change>>",      lambda e: self._redraw())
        self.text.bind("<Configure>",     lambda e: self._redraw())
        self.text.bind("<KeyRelease>",    lambda e: self._redraw())
        self.text.bind("<ButtonRelease>", lambda e: self._redraw())

    def _redraw(self):
        self.delete("all")
        i = self.text.index("@0,0")
        while True:
            dline = self.text.dlineinfo(i)
            if dline is None:
                break
            y = dline[1]
            linenum = int(str(i).split(".")[0])
            self.create_text(2, y, anchor="nw", text=str(linenum), fill=LINE_FG,
                             font=self.text.cget("font"))
            i = self.text.index(f"{i}+1line")
            if i == self.text.index(f"{i}-0c"):
                break


class MiniGOEditor(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Compilador MiniGO")
        self.geometry("1100x700")
        self.configure(bg=BG)

        self._current_file = None
        self._compiled_bin = None
        self._compiled_ll  = None
        self._hl_job       = None

        self._build_ui()
        self._bind_keys()
        self._update_statusbar()

    # ── Construcción de UI ────────────────────────────────────────────────

    def _build_ui(self):
        self._build_toolbar()
        self._build_panes()
        self._build_statusbar()

    def _build_toolbar(self):
        bar = tk.Frame(self, bg=BG_PANEL, pady=4)
        bar.pack(fill=tk.X)
        btn_kw = dict(bg=BG_PANEL, fg=FG, relief=tk.FLAT, padx=10, pady=2,
                      activebackground=ACCENT, activeforeground=BG,
                      cursor="hand2", font=("Segoe UI", 9))
        tk.Button(bar, text="Abrir",    command=self._open,   **btn_kw).pack(side=tk.LEFT, padx=2)
        tk.Button(bar, text="Guardar",  command=self._save,   **btn_kw).pack(side=tk.LEFT, padx=2)
        tk.Button(bar, text="Compilar", command=self._compile,**btn_kw).pack(side=tk.LEFT, padx=2)
        tk.Button(bar, text="Ejecutar", command=self._run,    **btn_kw).pack(side=tk.LEFT, padx=2)
        tk.Button(bar, text="Nuevo",    command=self._new,    **btn_kw).pack(side=tk.LEFT, padx=2)

    def _build_panes(self):
        paned = tk.PanedWindow(self, orient=tk.HORIZONTAL, bg=BG, sashwidth=4,
                               sashrelief=tk.FLAT, sashpad=0)
        paned.pack(fill=tk.BOTH, expand=True)

        # ── Panel izquierdo: editor ──────────────────────────────────────
        left = tk.Frame(paned, bg=BG)
        paned.add(left, minsize=400, stretch="always")

        mono = font.Font(family="Consolas", size=11)

        # Números de línea + editor
        editor_frame = tk.Frame(left, bg=BG)
        editor_frame.pack(fill=tk.BOTH, expand=True)

        self.editor = tk.Text(
            editor_frame,
            bg=BG, fg=FG, insertbackground=FG,
            selectbackground=SEL_BG, selectforeground=FG,
            font=mono, wrap=tk.NONE, undo=True,
            relief=tk.FLAT, padx=6, pady=6,
            tabs=("4c",),
        )
        self.line_nums = LineNumbers(editor_frame, self.editor,
                                     width=40, bg=LINE_BG, bd=0, highlightthickness=0)
        self.line_nums.pack(side=tk.LEFT, fill=tk.Y)

        scroll_y = ttk.Scrollbar(editor_frame, orient=tk.VERTICAL,
                                  command=self._scroll_both_y)
        scroll_x = ttk.Scrollbar(left, orient=tk.HORIZONTAL,
                                  command=self.editor.xview)
        self.editor.configure(yscrollcommand=scroll_y.set,
                              xscrollcommand=scroll_x.set)
        scroll_y.pack(side=tk.RIGHT, fill=tk.Y)
        self.editor.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scroll_x.pack(fill=tk.X)

        self.editor.bind("<KeyRelease>", self._on_key)
        self.editor.bind("<ButtonRelease>", lambda e: self._update_statusbar())

        # Tags de syntax highlighting
        self._setup_tags(mono)

        # ── Panel derecho: errores + output ─────────────────────────────
        right = tk.Frame(paned, bg=BG_PANEL)
        paned.add(right, minsize=300)

        # Errores
        tk.Label(right, text="  ERRORES", bg=BG_PANEL, fg=ERR_COL,
                 font=("Segoe UI", 9, "bold"), anchor="w").pack(fill=tk.X, pady=(6, 0))
        self.err_list = tk.Listbox(
            right, bg=BG_PANEL, fg=ERR_COL,
            selectbackground=SEL_BG, selectforeground=FG,
            font=("Consolas", 9), relief=tk.FLAT, height=10,
            activestyle="none",
        )
        self.err_list.pack(fill=tk.X, padx=4)
        self.err_list.bind("<Double-Button-1>", self._goto_error)

        # Output
        tk.Label(right, text="  OUTPUT", bg=BG_PANEL, fg=OK_COL,
                 font=("Segoe UI", 9, "bold"), anchor="w").pack(fill=tk.X, pady=(10, 0))
        self.output = tk.Text(
            right, bg=BG, fg=FG,
            font=("Consolas", 9), relief=tk.FLAT,
            state=tk.DISABLED, wrap=tk.WORD,
            padx=6, pady=4,
        )
        self.output.pack(fill=tk.BOTH, expand=True, padx=4, pady=(0, 4))

    def _scroll_both_y(self, *args):
        self.editor.yview(*args)
        self.line_nums._redraw()

    def _setup_tags(self, mono):
        self.editor.tag_configure("keyword",  foreground=KWORD_COL, font=font.Font(font=mono, weight="bold"))
        self.editor.tag_configure("string",   foreground=STR_COL)
        self.editor.tag_configure("number",   foreground=NUM_COL)
        self.editor.tag_configure("comment",  foreground=CMT_COL)
        self.editor.tag_configure("error_line", background="#3d1e2e")

    def _build_statusbar(self):
        bar = tk.Frame(self, bg=BG_PANEL, height=22)
        bar.pack(fill=tk.X, side=tk.BOTTOM)
        self.status_pos  = tk.Label(bar, text="Lín: 1  Col: 1", bg=BG_PANEL,
                                    fg=LINE_FG, font=("Segoe UI", 8))
        self.status_file = tk.Label(bar, text="Sin título", bg=BG_PANEL,
                                    fg=FG, font=("Segoe UI", 8))
        self.status_msg  = tk.Label(bar, text="", bg=BG_PANEL,
                                    fg=OK_COL, font=("Segoe UI", 8))
        self.status_pos.pack(side=tk.LEFT, padx=8)
        tk.Label(bar, text="│", bg=BG_PANEL, fg=LINE_FG).pack(side=tk.LEFT)
        self.status_file.pack(side=tk.LEFT, padx=8)
        self.status_msg.pack(side=tk.RIGHT, padx=8)

    def _bind_keys(self):
        self.bind("<Control-o>", lambda e: self._open())
        self.bind("<Control-s>", lambda e: self._save())
        self.bind("<Control-Return>", lambda e: self._compile())
        self.bind("<F5>", lambda e: self._run())

    # ── Acciones de toolbar ───────────────────────────────────────────────

    def _new(self):
        self.editor.delete("1.0", tk.END)
        self._current_file = None
        self._compiled_bin = None
        self._compiled_ll  = None
        self.title("Compilador MiniGO")
        self.status_file.config(text="Sin título")
        self._clear_errors()
        self._clear_output()

    def _open(self):
        path = filedialog.askopenfilename(
            filetypes=[("MiniGO", "*.mgo"), ("Todos", "*.*")]
        )
        if not path:
            return
        with open(path, encoding="utf-8") as f:
            content = f.read()
        self.editor.delete("1.0", tk.END)
        self.editor.insert("1.0", content)
        self._current_file = path
        self.title(f"Compilador MiniGO — {os.path.basename(path)}")
        self.status_file.config(text=os.path.basename(path))
        self._highlight_all()
        self._clear_errors()
        self._clear_output()

    def _save(self):
        if self._current_file is None:
            path = filedialog.asksaveasfilename(
                defaultextension=".mgo",
                filetypes=[("MiniGO", "*.mgo"), ("Todos", "*.*")]
            )
            if not path:
                return
            self._current_file = path
            self.title(f"Compilador MiniGO — {os.path.basename(path)}")
            self.status_file.config(text=os.path.basename(path))
        with open(self._current_file, "w", encoding="utf-8") as f:
            f.write(self.editor.get("1.0", tk.END))
        self._set_status("Guardado.", OK_COL)

    def _compile(self):
        # Guardar antes de compilar
        if self._current_file is None:
            self._save()
        if self._current_file is None:
            return
        self._save()
        self._clear_errors()
        self._clear_output()
        self.editor.tag_remove("error_line", "1.0", tk.END)

        ok, errs, ll_path, bin_path = compile_file(self._current_file)

        self._compiled_ll  = ll_path
        self._compiled_bin = bin_path

        if ok:
            if bin_path:
                self._set_status(f"Compilado OK → {os.path.basename(bin_path)}", OK_COL)
            else:
                self._set_status(f"IR generado: {os.path.basename(ll_path)}", OK_COL)
        else:
            self._set_status(f"{len(errs)} error(es) encontrado(s)", ERR_COL)
            for e in errs:
                self.err_list.insert(tk.END, e)
                # Destacar línea en el editor
                m = re.search(r"line:\s*(\d+)", e)
                if m:
                    ln = m.group(1)
                    self.editor.tag_add("error_line", f"{ln}.0", f"{ln}.end")

    def _run(self):
        if self._compiled_bin is None and self._compiled_ll is None:
            self._set_status("Compila primero.", ERR_COL)
            return
        self._clear_output()

        if self._compiled_bin and os.path.isfile(self._compiled_bin):
            # Binario nativo (si se compiló con clang)
            result = subprocess.run(
                [self._compiled_bin],
                capture_output=True, text=True, timeout=10
            )
            self._append_output(result.stdout)
            if result.stderr:
                self._append_output(result.stderr)
        elif self._compiled_ll and os.path.isfile(self._compiled_ll):
            # JIT con llvmlite — sin necesidad de clang
            runner = os.path.join(_SRC, "runner.py")
            result = subprocess.run(
                [sys.executable, runner, self._compiled_ll],
                capture_output=True, text=True, timeout=15
            )
            if result.stdout:
                self._append_output(result.stdout)
            if result.stderr:
                self._append_output(result.stderr)
            if result.returncode not in (0, 1) and not result.stdout and not result.stderr:
                self._append_output("(sin output)")
        else:
            self._set_status("Sin archivo .ll — compilá primero.", ERR_COL)

    # ── Helpers de UI ─────────────────────────────────────────────────────

    def _clear_errors(self):
        self.err_list.delete(0, tk.END)

    def _clear_output(self):
        self.output.config(state=tk.NORMAL)
        self.output.delete("1.0", tk.END)
        self.output.config(state=tk.DISABLED)

    def _append_output(self, text):
        self.output.config(state=tk.NORMAL)
        self.output.insert(tk.END, text)
        self.output.config(state=tk.DISABLED)
        self.output.see(tk.END)

    def _set_status(self, msg, color=OK_COL):
        self.status_msg.config(text=msg, fg=color)

    def _update_statusbar(self):
        pos = self.editor.index(tk.INSERT)
        ln, col = pos.split(".")
        self.status_pos.config(text=f"Lín: {ln}  Col: {int(col)+1}")

    def _goto_error(self, event):
        sel = self.err_list.curselection()
        if not sel:
            return
        text = self.err_list.get(sel[0])
        m = re.search(r"line:\s*(\d+).*column:\s*(\d+)", text)
        if m:
            ln, col = m.group(1), str(int(m.group(2)) - 1)
            self.editor.mark_set(tk.INSERT, f"{ln}.{col}")
            self.editor.see(f"{ln}.{col}")
            self.editor.focus_set()

    # ── Syntax highlighting ───────────────────────────────────────────────

    def _on_key(self, event):
        self._update_statusbar()
        if self._hl_job:
            self.after_cancel(self._hl_job)
        self._hl_job = self.after(200, self._highlight_all)

    def _highlight_all(self):
        for tag in ("keyword", "string", "number", "comment"):
            self.editor.tag_remove(tag, "1.0", tk.END)

        text = self.editor.get("1.0", tk.END)

        # Comentarios de línea
        for m in re.finditer(r"//[^\n]*", text):
            self._apply_tag("comment", m.start(), m.end())

        # Strings (raw y comillas dobles)
        for m in re.finditer(r'`[^`]*`|"(?:[^"\\]|\\.)*"', text):
            self._apply_tag("string", m.start(), m.end())

        # Números
        for m in re.finditer(r"\b\d+(?:\.\d*)?\b", text):
            self._apply_tag("number", m.start(), m.end())

        # Keywords
        kw_pattern = r"\b(" + "|".join(KEYWORDS) + r")\b"
        for m in re.finditer(kw_pattern, text):
            self._apply_tag("keyword", m.start(), m.end())

    def _apply_tag(self, tag, start_char, end_char):
        content = self.editor.get("1.0", tk.END)
        # Convertir índice de carácter a índice de texto de tk
        s = self.editor.index(f"1.0 + {start_char} chars")
        e = self.editor.index(f"1.0 + {end_char} chars")
        self.editor.tag_add(tag, s, e)


def main():
    app = MiniGOEditor()
    app.mainloop()


if __name__ == "__main__":
    main()
