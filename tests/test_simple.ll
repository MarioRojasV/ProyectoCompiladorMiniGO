; ModuleID = "miniGO"
target triple = "x86_64-pc-windows-msvc"
target datalayout = ""

define i64 @"suma"(i64 %"a", i64 %"b")
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

define i32 @"main"()
{
entry:
  %".2" = call i64 @"suma"(i64 3, i64 4)
  %"r" = alloca i64
  store i64 %".2", i64* %"r"
  %"r.1" = load i64, i64* %"r"
  %".4" = getelementptr inbounds [6 x i8], [6 x i8]* @".str0", i32 0, i32 0
  %".5" = call i32 (i8*, ...) @"printf"(i8* %".4", i64 %"r.1")
  ret i32 0
}

declare i32 @"printf"(i8* %".1", ...)

@".str0" = private unnamed_addr constant [6 x i8] c"%lld\0a\00"