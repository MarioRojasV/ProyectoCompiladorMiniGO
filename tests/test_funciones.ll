; ModuleID = "miniGO"
target triple = "x86_64-pc-windows-msvc"
target datalayout = ""

define i64 @"sumar"(i64 %"a", i64 %"b")
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

define i64 @"restar"(i64 %"a", i64 %"b")
{
entry:
  %"a.1" = alloca i64
  store i64 %"a", i64* %"a.1"
  %"b.1" = alloca i64
  store i64 %"b", i64* %"b.1"
  %"a.2" = load i64, i64* %"a.1"
  %"b.2" = load i64, i64* %"b.1"
  %".6" = sub i64 %"a.2", %"b.2"
  ret i64 %".6"
}

define i64 @"multiplicar"(i64 %"a", i64 %"b")
{
entry:
  %"a.1" = alloca i64
  store i64 %"a", i64* %"a.1"
  %"b.1" = alloca i64
  store i64 %"b", i64* %"b.1"
  %"a.2" = load i64, i64* %"a.1"
  %"b.2" = load i64, i64* %"b.1"
  %".6" = mul i64 %"a.2", %"b.2"
  %"resultado" = alloca i64
  store i64 %".6", i64* %"resultado"
  %"resultado.1" = load i64, i64* %"resultado"
  ret i64 %"resultado.1"
}

define i64 @"maximo"(i64 %"a", i64 %"b")
{
entry:
  %"a.1" = alloca i64
  store i64 %"a", i64* %"a.1"
  %"b.1" = alloca i64
  store i64 %"b", i64* %"b.1"
  %"a.2" = load i64, i64* %"a.1"
  %"b.2" = load i64, i64* %"b.1"
  %".6" = icmp sgt i64 %"a.2", %"b.2"
  br i1 %".6", label %"then", label %"merge"
then:
  %"a.3" = load i64, i64* %"a.1"
  ret i64 %"a.3"
merge:
  %"b.3" = load i64, i64* %"b.1"
  ret i64 %"b.3"
}

define void @"imprimirSuma"(i64 %"a", i64 %"b")
{
entry:
  %"a.1" = alloca i64
  store i64 %"a", i64* %"a.1"
  %"b.1" = alloca i64
  store i64 %"b", i64* %"b.1"
  %"a.2" = load i64, i64* %"a.1"
  %"b.2" = load i64, i64* %"b.1"
  %".6" = add i64 %"a.2", %"b.2"
  %"s" = alloca i64
  store i64 %".6", i64* %"s"
  %"s.1" = load i64, i64* %"s"
  %".8" = getelementptr inbounds [6 x i8], [6 x i8]* @".str0", i32 0, i32 0
  %".9" = call i32 (i8*, ...) @"printf"(i8* %".8", i64 %"s.1")
  ret void
}

define i64 @"cuarenta"()
{
entry:
  ret i64 40
}

define i32 @"main"()
{
entry:
  %".2" = call i64 @"sumar"(i64 10, i64 20)
  %".3" = getelementptr inbounds [6 x i8], [6 x i8]* @".str1", i32 0, i32 0
  %".4" = call i32 (i8*, ...) @"printf"(i8* %".3", i64 %".2")
  %".5" = call i64 @"restar"(i64 50, i64 15)
  %".6" = getelementptr inbounds [6 x i8], [6 x i8]* @".str2", i32 0, i32 0
  %".7" = call i32 (i8*, ...) @"printf"(i8* %".6", i64 %".5")
  %".8" = call i64 @"multiplicar"(i64 6, i64 7)
  %".9" = getelementptr inbounds [6 x i8], [6 x i8]* @".str3", i32 0, i32 0
  %".10" = call i32 (i8*, ...) @"printf"(i8* %".9", i64 %".8")
  %".11" = call i64 @"maximo"(i64 25, i64 18)
  %".12" = getelementptr inbounds [6 x i8], [6 x i8]* @".str4", i32 0, i32 0
  %".13" = call i32 (i8*, ...) @"printf"(i8* %".12", i64 %".11")
  call void @"imprimirSuma"(i64 3, i64 4)
  %".15" = call i64 @"cuarenta"()
  %"n" = alloca i64
  store i64 %".15", i64* %"n"
  %"n.1" = load i64, i64* %"n"
  %".17" = getelementptr inbounds [6 x i8], [6 x i8]* @".str5", i32 0, i32 0
  %".18" = call i32 (i8*, ...) @"printf"(i8* %".17", i64 %"n.1")
  %".19" = call i64 @"maximo"(i64 5, i64 3)
  %".20" = call i64 @"cuarenta"()
  %".21" = call i64 @"sumar"(i64 %".19", i64 %".20")
  %"x" = alloca i64
  store i64 %".21", i64* %"x"
  %"x.1" = load i64, i64* %"x"
  %".23" = getelementptr inbounds [6 x i8], [6 x i8]* @".str6", i32 0, i32 0
  %".24" = call i32 (i8*, ...) @"printf"(i8* %".23", i64 %"x.1")
  ret i32 0
}

declare i32 @"printf"(i8* %".1", ...)

@".str0" = private unnamed_addr constant [6 x i8] c"%lld\0a\00"
@".str1" = private unnamed_addr constant [6 x i8] c"%lld\0a\00"
@".str2" = private unnamed_addr constant [6 x i8] c"%lld\0a\00"
@".str3" = private unnamed_addr constant [6 x i8] c"%lld\0a\00"
@".str4" = private unnamed_addr constant [6 x i8] c"%lld\0a\00"
@".str5" = private unnamed_addr constant [6 x i8] c"%lld\0a\00"
@".str6" = private unnamed_addr constant [6 x i8] c"%lld\0a\00"