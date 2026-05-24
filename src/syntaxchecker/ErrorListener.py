import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from antlr4.error.ErrorListener import ErrorListener
from generated.MiniGOLexer import MiniGOLexer
from generated.MiniGOParser import MiniGOParser

class MiniGOErrorListener(ErrorListener):
    def __init__(self):
        super().__init__()
        self.error_list = []

    def hasErrors(self):
        return len(self.error_list) > 0

    def getErrorList(self):
        return self.error_list

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        if isinstance(recognizer, MiniGOLexer):
            self.error_list.append(
                f"SCANNER ERROR: {msg} (line: {line}, column: {column})"
            )
        elif isinstance(recognizer, MiniGOParser):
            self.error_list.append(
                f"PARSER ERROR: {msg} (line: {line}, column: {column})"
            )