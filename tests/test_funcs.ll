; ModuleID = "miniGO"
target triple = "unknown-unknown-unknown"
target datalayout = ""

define void @"sinRetorno"(i64 %"a", i64 %"b")
{
entry:
  %"a.1" = alloca i64
  store i64 %"a", i64* %"a.1"
  %"b.1" = alloca i64
  store i64 %"b", i64* %"b.1"
  %"a.2" = load i64, i64* %"a.1"
  %"b.2" = load i64, i64* %"b.1"
  %".6" = add i64 %"a.2", %"b.2"
  %"c" = alloca i64
  store i64 %".6", i64* %"c"
  ret void
}

define i64 @"conRetorno"(i64 %"a", i64 %"b")
{
entry:
  %"a.1" = alloca i64
  store i64 %"a", i64* %"a.1"
  %"b.1" = alloca i64
  store i64 %"b", i64* %"b.1"
  %"a.2" = load i64, i64* %"a.1"
  %"b.2" = load i64, i64* %"b.1"
  %".6" = add i64 %"a.2", %"b.2"
  ret i64 %".6"
}

define i64 @"sinParametros"()
{
entry:
  ret i64 42
}
