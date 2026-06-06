; ModuleID = "miniGO"
target triple = "x86_64-pc-windows-msvc"
target datalayout = ""

define i32 @"main"()
{
entry:
  %"globalA" = load i64, i64* @"globalA"
  %".2" = getelementptr inbounds [6 x i8], [6 x i8]* @".str0", i32 0, i32 0
  %".3" = call i32 (i8*, ...) @"printf"(i8* %".2", i64 %"globalA")
  %"globalB" = load double, double* @"globalB"
  %".4" = getelementptr inbounds [4 x i8], [4 x i8]* @".str1", i32 0, i32 0
  %".5" = call i32 (i8*, ...) @"printf"(i8* %".4", double %"globalB")
  %"globalC" = load i1, i1* @"globalC"
  %".6" = getelementptr inbounds [6 x i8], [6 x i8]* @".str2", i32 0, i32 0
  %".7" = getelementptr inbounds [7 x i8], [7 x i8]* @".str3", i32 0, i32 0
  %".8" = select  i1 %"globalC", i8* %".6", i8* %".7"
  %".9" = call i32 (i8*, ...) @"printf"(i8* %".8")
  %"globalD" = load i64, i64* @"globalD"
  %".10" = getelementptr inbounds [6 x i8], [6 x i8]* @".str4", i32 0, i32 0
  %".11" = call i32 (i8*, ...) @"printf"(i8* %".10", i64 %"globalD")
  %"globalA.1" = load i64, i64* @"globalA"
  %".12" = add i64 %"globalA.1", 10
  store i64 %".12", i64* @"globalA"
  %"globalA.2" = load i64, i64* @"globalA"
  %".14" = getelementptr inbounds [6 x i8], [6 x i8]* @".str5", i32 0, i32 0
  %".15" = call i32 (i8*, ...) @"printf"(i8* %".14", i64 %"globalA.2")
  %"localA" = alloca i64
  store i64 100, i64* %"localA"
  %"localB" = alloca double
  store double 0x4005ae147ae147ae, double* %"localB"
  %"localC" = alloca i1
  store i1 0, i1* %"localC"
  %"localD" = alloca i64
  store i64 0, i64* %"localD"
  %"localA.1" = load i64, i64* %"localA"
  %".20" = getelementptr inbounds [6 x i8], [6 x i8]* @".str6", i32 0, i32 0
  %".21" = call i32 (i8*, ...) @"printf"(i8* %".20", i64 %"localA.1")
  %"localB.1" = load double, double* %"localB"
  %".22" = getelementptr inbounds [4 x i8], [4 x i8]* @".str7", i32 0, i32 0
  %".23" = call i32 (i8*, ...) @"printf"(i8* %".22", double %"localB.1")
  %"localC.1" = load i1, i1* %"localC"
  %".24" = getelementptr inbounds [6 x i8], [6 x i8]* @".str8", i32 0, i32 0
  %".25" = getelementptr inbounds [7 x i8], [7 x i8]* @".str9", i32 0, i32 0
  %".26" = select  i1 %"localC.1", i8* %".24", i8* %".25"
  %".27" = call i32 (i8*, ...) @"printf"(i8* %".26")
  %"localD.1" = load i64, i64* %"localD"
  %".28" = getelementptr inbounds [6 x i8], [6 x i8]* @".str10", i32 0, i32 0
  %".29" = call i32 (i8*, ...) @"printf"(i8* %".28", i64 %"localD.1")
  %"localA.2" = load i64, i64* %"localA"
  %"globalA.3" = load i64, i64* @"globalA"
  %".30" = add i64 %"localA.2", %"globalA.3"
  store i64 %".30", i64* %"localD"
  %"localD.2" = load i64, i64* %"localD"
  %".32" = getelementptr inbounds [6 x i8], [6 x i8]* @".str11", i32 0, i32 0
  %".33" = call i32 (i8*, ...) @"printf"(i8* %".32", i64 %"localD.2")
  %"inferido" = alloca i64
  store i64 99, i64* %"inferido"
  %"inferido.1" = load i64, i64* %"inferido"
  %".35" = getelementptr inbounds [6 x i8], [6 x i8]* @".str12", i32 0, i32 0
  %".36" = call i32 (i8*, ...) @"printf"(i8* %".35", i64 %"inferido.1")
  ret i32 0
}

@"globalA" = internal global i64 42
@"globalB" = internal global double 0x40091eb851eb851f
@"globalC" = internal global i1 1
@"globalD" = internal global i64 0
declare i32 @"printf"(i8* %".1", ...)

@".str0" = private unnamed_addr constant [6 x i8] c"%lld\0a\00"
@".str1" = private unnamed_addr constant [4 x i8] c"%f\0a\00"
@".str2" = private unnamed_addr constant [6 x i8] c"true\0a\00"
@".str3" = private unnamed_addr constant [7 x i8] c"false\0a\00"
@".str4" = private unnamed_addr constant [6 x i8] c"%lld\0a\00"
@".str5" = private unnamed_addr constant [6 x i8] c"%lld\0a\00"
@".str6" = private unnamed_addr constant [6 x i8] c"%lld\0a\00"
@".str7" = private unnamed_addr constant [4 x i8] c"%f\0a\00"
@".str8" = private unnamed_addr constant [6 x i8] c"true\0a\00"
@".str9" = private unnamed_addr constant [7 x i8] c"false\0a\00"
@".str10" = private unnamed_addr constant [6 x i8] c"%lld\0a\00"
@".str11" = private unnamed_addr constant [6 x i8] c"%lld\0a\00"
@".str12" = private unnamed_addr constant [6 x i8] c"%lld\0a\00"