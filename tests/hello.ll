; ModuleID = "miniGO"
target triple = "x86_64-pc-windows-msvc"
target datalayout = ""

define i32 @"main"()
{
entry:
  %".2" = getelementptr inbounds [11 x i8], [11 x i8]* @".str0", i32 0, i32 0
  %".3" = getelementptr inbounds [4 x i8], [4 x i8]* @".str1", i32 0, i32 0
  %".4" = call i32 (i8*, ...) @"printf"(i8* %".3", i8* %".2")
  %"x" = alloca i64
  store i64 10, i64* %"x"
  %"x.1" = load i64, i64* %"x"
  %".6" = icmp sgt i64 %"x.1", 5
  %"i" = alloca i64
  br i1 %".6", label %"then", label %"merge"
then:
  %".8" = getelementptr inbounds [12 x i8], [12 x i8]* @".str2", i32 0, i32 0
  %".9" = getelementptr inbounds [4 x i8], [4 x i8]* @".str3", i32 0, i32 0
  %".10" = call i32 (i8*, ...) @"printf"(i8* %".9", i8* %".8")
  br label %"merge"
merge:
  store i64 0, i64* %"i"
  br label %"while_header"
while_header:
  %"i.1" = load i64, i64* %"i"
  %".14" = icmp slt i64 %"i.1", 3
  br i1 %".14", label %"while_body", label %"while_exit"
while_body:
  %".16" = getelementptr inbounds [9 x i8], [9 x i8]* @".str4", i32 0, i32 0
  %".17" = getelementptr inbounds [4 x i8], [4 x i8]* @".str5", i32 0, i32 0
  %".18" = call i32 (i8*, ...) @"printf"(i8* %".17", i8* %".16")
  %".19" = load i64, i64* %"i"
  %".20" = add i64 %".19", 1
  store i64 %".20", i64* %"i"
  br label %"while_header"
while_exit:
  ret i32 0
}

@".str0" = private unnamed_addr constant [11 x i8] c"Hola Mundo\00"
declare i32 @"printf"(i8* %".1", ...)

@".str1" = private unnamed_addr constant [4 x i8] c"%s\0a\00"
@".str2" = private unnamed_addr constant [12 x i8] c"mayor que 5\00"
@".str3" = private unnamed_addr constant [4 x i8] c"%s\0a\00"
@".str4" = private unnamed_addr constant [9 x i8] c"iterando\00"
@".str5" = private unnamed_addr constant [4 x i8] c"%s\0a\00"