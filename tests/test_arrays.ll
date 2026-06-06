; ModuleID = "miniGO"
target triple = "x86_64-pc-windows-msvc"
target datalayout = ""

define i32 @"main"()
{
entry:
  %".2" = getelementptr inbounds [3 x i64], [3 x i64]* @"globalArr", i32 0, i64 0
  store i64 10, i64* %".2"
  %".4" = getelementptr inbounds [3 x i64], [3 x i64]* @"globalArr", i32 0, i64 1
  store i64 20, i64* %".4"
  %".6" = getelementptr inbounds [3 x i64], [3 x i64]* @"globalArr", i32 0, i64 2
  store i64 30, i64* %".6"
  %".8" = getelementptr inbounds [3 x i64], [3 x i64]* @"globalArr", i32 0, i64 0
  %".9" = load i64, i64* %".8"
  %".10" = getelementptr inbounds [6 x i8], [6 x i8]* @".str0", i32 0, i32 0
  %".11" = call i32 (i8*, ...) @"printf"(i8* %".10", i64 %".9")
  %".12" = getelementptr inbounds [3 x i64], [3 x i64]* @"globalArr", i32 0, i64 1
  %".13" = load i64, i64* %".12"
  %".14" = getelementptr inbounds [6 x i8], [6 x i8]* @".str1", i32 0, i32 0
  %".15" = call i32 (i8*, ...) @"printf"(i8* %".14", i64 %".13")
  %".16" = getelementptr inbounds [3 x i64], [3 x i64]* @"globalArr", i32 0, i64 2
  %".17" = load i64, i64* %".16"
  %".18" = getelementptr inbounds [6 x i8], [6 x i8]* @".str2", i32 0, i32 0
  %".19" = call i32 (i8*, ...) @"printf"(i8* %".18", i64 %".17")
  %".20" = getelementptr inbounds [6 x i8], [6 x i8]* @".str3", i32 0, i32 0
  %".21" = call i32 (i8*, ...) @"printf"(i8* %".20", i64 3)
  %"localArr" = alloca [5 x i64]
  %".22" = getelementptr inbounds [5 x i64], [5 x i64]* %"localArr", i32 0, i64 0
  store i64 1, i64* %".22"
  %".24" = getelementptr inbounds [5 x i64], [5 x i64]* %"localArr", i32 0, i64 1
  store i64 2, i64* %".24"
  %".26" = getelementptr inbounds [5 x i64], [5 x i64]* %"localArr", i32 0, i64 2
  store i64 3, i64* %".26"
  %".28" = getelementptr inbounds [5 x i64], [5 x i64]* %"localArr", i32 0, i64 3
  store i64 4, i64* %".28"
  %".30" = getelementptr inbounds [5 x i64], [5 x i64]* %"localArr", i32 0, i64 4
  store i64 5, i64* %".30"
  %"n" = alloca i64
  store i64 5, i64* %"n"
  %"n.1" = load i64, i64* %"n"
  %".33" = getelementptr inbounds [6 x i8], [6 x i8]* @".str4", i32 0, i32 0
  %".34" = call i32 (i8*, ...) @"printf"(i8* %".33", i64 %"n.1")
  %"suma" = alloca i64
  store i64 0, i64* %"suma"
  %"i" = alloca i64
  store i64 0, i64* %"i"
  %"j" = alloca i64
  br label %"for_header"
for_header:
  %"i.1" = load i64, i64* %"i"
  %"n.2" = load i64, i64* %"n"
  %".38" = icmp slt i64 %"i.1", %"n.2"
  br i1 %".38", label %"for_body", label %"for_exit"
for_body:
  %"suma.1" = load i64, i64* %"suma"
  %"i.2" = load i64, i64* %"i"
  %".40" = getelementptr inbounds [5 x i64], [5 x i64]* %"localArr", i32 0, i64 %"i.2"
  %".41" = load i64, i64* %".40"
  %".42" = add i64 %"suma.1", %".41"
  store i64 %".42", i64* %"suma"
  br label %"for_post"
for_post:
  %".45" = load i64, i64* %"i"
  %".46" = add i64 %".45", 1
  store i64 %".46", i64* %"i"
  br label %"for_header"
for_exit:
  %"suma.2" = load i64, i64* %"suma"
  %".49" = getelementptr inbounds [6 x i8], [6 x i8]* @".str5", i32 0, i32 0
  %".50" = call i32 (i8*, ...) @"printf"(i8* %".49", i64 %"suma.2")
  store i64 0, i64* %"j"
  br label %"while_header"
while_header:
  %"j.1" = load i64, i64* %"j"
  %"n.3" = load i64, i64* %"n"
  %".53" = icmp slt i64 %"j.1", %"n.3"
  br i1 %".53", label %"while_body", label %"while_exit"
while_body:
  %"j.2" = load i64, i64* %"j"
  %".55" = getelementptr inbounds [5 x i64], [5 x i64]* %"localArr", i32 0, i64 %"j.2"
  %".56" = load i64, i64* %".55"
  %".57" = getelementptr inbounds [6 x i8], [6 x i8]* @".str6", i32 0, i32 0
  %".58" = call i32 (i8*, ...) @"printf"(i8* %".57", i64 %".56")
  %"j.3" = load i64, i64* %"j"
  %".59" = add i64 %"j.3", 1
  store i64 %".59", i64* %"j"
  br label %"while_header"
while_exit:
  ret i32 0
}

@"globalArr" = internal global [3 x i64] zeroinitializer
declare i32 @"printf"(i8* %".1", ...)

@".str0" = private unnamed_addr constant [6 x i8] c"%lld\0a\00"
@".str1" = private unnamed_addr constant [6 x i8] c"%lld\0a\00"
@".str2" = private unnamed_addr constant [6 x i8] c"%lld\0a\00"
@".str3" = private unnamed_addr constant [6 x i8] c"%lld\0a\00"
@".str4" = private unnamed_addr constant [6 x i8] c"%lld\0a\00"
@".str5" = private unnamed_addr constant [6 x i8] c"%lld\0a\00"
@".str6" = private unnamed_addr constant [6 x i8] c"%lld\0a\00"