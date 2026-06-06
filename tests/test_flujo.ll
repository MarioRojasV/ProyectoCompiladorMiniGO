; ModuleID = "miniGO"
target triple = "x86_64-pc-windows-msvc"
target datalayout = ""

define i32 @"main"()
{
entry:
  %"x" = alloca i64
  store i64 10, i64* %"x"
  %"x.1" = load i64, i64* %"x"
  %".3" = icmp sgt i64 %"x.1", 5
  %"i" = alloca i64
  %"j" = alloca i64
  br i1 %".3", label %"then", label %"merge"
then:
  %".5" = getelementptr inbounds [12 x i8], [12 x i8]* @".str0", i32 0, i32 0
  %".6" = getelementptr inbounds [4 x i8], [4 x i8]* @".str1", i32 0, i32 0
  %".7" = call i32 (i8*, ...) @"printf"(i8* %".6", i8* %".5")
  br label %"merge"
merge:
  %"x.2" = load i64, i64* %"x"
  %".9" = icmp sgt i64 %"x.2", 15
  br i1 %".9", label %"then.1", label %"else"
then.1:
  %".11" = getelementptr inbounds [13 x i8], [13 x i8]* @".str2", i32 0, i32 0
  %".12" = getelementptr inbounds [4 x i8], [4 x i8]* @".str3", i32 0, i32 0
  %".13" = call i32 (i8*, ...) @"printf"(i8* %".12", i8* %".11")
  br label %"merge.1"
else:
  %".15" = getelementptr inbounds [16 x i8], [16 x i8]* @".str4", i32 0, i32 0
  %".16" = getelementptr inbounds [4 x i8], [4 x i8]* @".str5", i32 0, i32 0
  %".17" = call i32 (i8*, ...) @"printf"(i8* %".16", i8* %".15")
  br label %"merge.1"
merge.1:
  %"x.3" = load i64, i64* %"x"
  %".19" = icmp eq i64 %"x.3", 10
  br i1 %".19", label %"then.2", label %"else.1"
then.2:
  %".21" = getelementptr inbounds [8 x i8], [8 x i8]* @".str6", i32 0, i32 0
  %".22" = getelementptr inbounds [4 x i8], [4 x i8]* @".str7", i32 0, i32 0
  %".23" = call i32 (i8*, ...) @"printf"(i8* %".22", i8* %".21")
  br label %"merge.3"
else.1:
  %"x.4" = load i64, i64* %"x"
  %".24" = icmp eq i64 %"x.4", 5
  br i1 %".24", label %"then.3", label %"else.2"
then.3:
  %".26" = getelementptr inbounds [9 x i8], [9 x i8]* @".str8", i32 0, i32 0
  %".27" = getelementptr inbounds [4 x i8], [4 x i8]* @".str9", i32 0, i32 0
  %".28" = call i32 (i8*, ...) @"printf"(i8* %".27", i8* %".26")
  br label %"merge.2"
else.2:
  %".30" = getelementptr inbounds [12 x i8], [12 x i8]* @".str10", i32 0, i32 0
  %".31" = getelementptr inbounds [4 x i8], [4 x i8]* @".str11", i32 0, i32 0
  %".32" = call i32 (i8*, ...) @"printf"(i8* %".31", i8* %".30")
  br label %"merge.2"
merge.2:
  br label %"merge.3"
merge.3:
  store i64 0, i64* %"i"
  br label %"while_header"
while_header:
  %"i.1" = load i64, i64* %"i"
  %".38" = icmp slt i64 %"i.1", 5
  br i1 %".38", label %"while_body", label %"while_exit"
while_body:
  %"i.2" = load i64, i64* %"i"
  %".40" = getelementptr inbounds [6 x i8], [6 x i8]* @".str12", i32 0, i32 0
  %".41" = call i32 (i8*, ...) @"printf"(i8* %".40", i64 %"i.2")
  %"i.3" = load i64, i64* %"i"
  %".42" = add i64 %"i.3", 1
  store i64 %".42", i64* %"i"
  br label %"while_header"
while_exit:
  store i64 1, i64* %"j"
  br label %"for_header"
for_header:
  %"j.1" = load i64, i64* %"j"
  %".47" = icmp sle i64 %"j.1", 3
  br i1 %".47", label %"for_body", label %"for_exit"
for_body:
  %"j.2" = load i64, i64* %"j"
  %".49" = getelementptr inbounds [6 x i8], [6 x i8]* @".str13", i32 0, i32 0
  %".50" = call i32 (i8*, ...) @"printf"(i8* %".49", i64 %"j.2")
  br label %"for_post"
for_post:
  %".52" = load i64, i64* %"j"
  %".53" = add i64 %".52", 1
  store i64 %".53", i64* %"j"
  br label %"for_header"
for_exit:
  %"x.5" = load i64, i64* %"x"
  switch i64 %"x.5", label %"sw_case.2" [i64 10, label %"sw_case" i64 20, label %"sw_case.1"]
sw_merge:
  ret i32 0
sw_case:
  %".57" = getelementptr inbounds [5 x i8], [5 x i8]* @".str14", i32 0, i32 0
  %".58" = getelementptr inbounds [4 x i8], [4 x i8]* @".str15", i32 0, i32 0
  %".59" = call i32 (i8*, ...) @"printf"(i8* %".58", i8* %".57")
  br label %"sw_merge"
sw_case.1:
  %".61" = getelementptr inbounds [7 x i8], [7 x i8]* @".str16", i32 0, i32 0
  %".62" = getelementptr inbounds [4 x i8], [4 x i8]* @".str17", i32 0, i32 0
  %".63" = call i32 (i8*, ...) @"printf"(i8* %".62", i8* %".61")
  br label %"sw_merge"
sw_case.2:
  %".65" = getelementptr inbounds [5 x i8], [5 x i8]* @".str18", i32 0, i32 0
  %".66" = getelementptr inbounds [4 x i8], [4 x i8]* @".str19", i32 0, i32 0
  %".67" = call i32 (i8*, ...) @"printf"(i8* %".66", i8* %".65")
  br label %"sw_merge"
}

@".str0" = private unnamed_addr constant [12 x i8] c"mayor que 5\00"
declare i32 @"printf"(i8* %".1", ...)

@".str1" = private unnamed_addr constant [4 x i8] c"%s\0a\00"
@".str2" = private unnamed_addr constant [13 x i8] c"mayor que 15\00"
@".str3" = private unnamed_addr constant [4 x i8] c"%s\0a\00"
@".str4" = private unnamed_addr constant [16 x i8] c"no mayor que 15\00"
@".str5" = private unnamed_addr constant [4 x i8] c"%s\0a\00"
@".str6" = private unnamed_addr constant [8 x i8] c"es diez\00"
@".str7" = private unnamed_addr constant [4 x i8] c"%s\0a\00"
@".str8" = private unnamed_addr constant [9 x i8] c"es cinco\00"
@".str9" = private unnamed_addr constant [4 x i8] c"%s\0a\00"
@".str10" = private unnamed_addr constant [12 x i8] c"otro numero\00"
@".str11" = private unnamed_addr constant [4 x i8] c"%s\0a\00"
@".str12" = private unnamed_addr constant [6 x i8] c"%lld\0a\00"
@".str13" = private unnamed_addr constant [6 x i8] c"%lld\0a\00"
@".str14" = private unnamed_addr constant [5 x i8] c"diez\00"
@".str15" = private unnamed_addr constant [4 x i8] c"%s\0a\00"
@".str16" = private unnamed_addr constant [7 x i8] c"veinte\00"
@".str17" = private unnamed_addr constant [4 x i8] c"%s\0a\00"
@".str18" = private unnamed_addr constant [5 x i8] c"otro\00"
@".str19" = private unnamed_addr constant [4 x i8] c"%s\0a\00"