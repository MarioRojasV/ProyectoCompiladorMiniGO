; ModuleID = "miniGO"
target triple = "x86_64-pc-windows-msvc"
target datalayout = ""

define void @"prueba"()
{
entry:
  %"x" = alloca i64
  store i64 10, i64* %"x"
  %"x.1" = load i64, i64* %"x"
  %".3" = icmp sgt i64 %"x.1", 5
  %"i" = alloca i64
  br i1 %".3", label %"then", label %"merge"
then:
  %".5" = getelementptr inbounds [6 x i8], [6 x i8]* @".str0", i32 0, i32 0
  %".6" = getelementptr inbounds [4 x i8], [4 x i8]* @".str1", i32 0, i32 0
  %".7" = call i32 (i8*, ...) @"printf"(i8* %".6", i8* %".5")
  br label %"merge"
merge:
  %"x.2" = load i64, i64* %"x"
  %".9" = icmp sgt i64 %"x.2", 5
  br i1 %".9", label %"then.1", label %"else"
then.1:
  %".11" = getelementptr inbounds [6 x i8], [6 x i8]* @".str2", i32 0, i32 0
  %".12" = getelementptr inbounds [4 x i8], [4 x i8]* @".str3", i32 0, i32 0
  %".13" = call i32 (i8*, ...) @"printf"(i8* %".12", i8* %".11")
  br label %"merge.1"
else:
  %".15" = getelementptr inbounds [6 x i8], [6 x i8]* @".str4", i32 0, i32 0
  %".16" = getelementptr inbounds [4 x i8], [4 x i8]* @".str5", i32 0, i32 0
  %".17" = call i32 (i8*, ...) @"printf"(i8* %".16", i8* %".15")
  br label %"merge.1"
merge.1:
  br label %"while_header"
while_header:
  %"x.3" = load i64, i64* %"x"
  %".20" = icmp sgt i64 %"x.3", 0
  br i1 %".20", label %"while_body", label %"while_exit"
while_body:
  %".22" = load i64, i64* %"x"
  %".23" = sub i64 %".22", 1
  store i64 %".23", i64* %"x"
  br label %"while_header"
while_exit:
  store i64 0, i64* %"i"
  br label %"for_header"
for_header:
  %"i.1" = load i64, i64* %"i"
  %".28" = icmp slt i64 %"i.1", 10
  br i1 %".28", label %"for_body", label %"for_exit"
for_body:
  %".30" = getelementptr inbounds [5 x i8], [5 x i8]* @".str6", i32 0, i32 0
  %".31" = getelementptr inbounds [4 x i8], [4 x i8]* @".str7", i32 0, i32 0
  %".32" = call i32 (i8*, ...) @"printf"(i8* %".31", i8* %".30")
  br label %"for_post"
for_post:
  %".34" = load i64, i64* %"i"
  %".35" = add i64 %".34", 1
  store i64 %".35", i64* %"i"
  br label %"for_header"
for_exit:
  %"x.4" = load i64, i64* %"x"
  switch i64 %"x.4", label %"sw_case.2" [i64 1, label %"sw_case" i64 2, label %"sw_case.1"]
sw_merge:
  ret void
sw_case:
  %".39" = getelementptr inbounds [4 x i8], [4 x i8]* @".str8", i32 0, i32 0
  %".40" = getelementptr inbounds [4 x i8], [4 x i8]* @".str9", i32 0, i32 0
  %".41" = call i32 (i8*, ...) @"printf"(i8* %".40", i8* %".39")
  br label %"sw_merge"
sw_case.1:
  %".43" = getelementptr inbounds [4 x i8], [4 x i8]* @".str10", i32 0, i32 0
  %".44" = getelementptr inbounds [4 x i8], [4 x i8]* @".str11", i32 0, i32 0
  %".45" = call i32 (i8*, ...) @"printf"(i8* %".44", i8* %".43")
  br label %"sw_merge"
sw_case.2:
  %".47" = getelementptr inbounds [5 x i8], [5 x i8]* @".str12", i32 0, i32 0
  %".48" = getelementptr inbounds [4 x i8], [4 x i8]* @".str13", i32 0, i32 0
  %".49" = call i32 (i8*, ...) @"printf"(i8* %".48", i8* %".47")
  br label %"sw_merge"
}

@".str0" = private unnamed_addr constant [6 x i8] c"mayor\00"
declare i32 @"printf"(i8* %".1", ...)

@".str1" = private unnamed_addr constant [4 x i8] c"%s\0a\00"
@".str2" = private unnamed_addr constant [6 x i8] c"mayor\00"
@".str3" = private unnamed_addr constant [4 x i8] c"%s\0a\00"
@".str4" = private unnamed_addr constant [6 x i8] c"menor\00"
@".str5" = private unnamed_addr constant [4 x i8] c"%s\0a\00"
@".str6" = private unnamed_addr constant [5 x i8] c"hola\00"
@".str7" = private unnamed_addr constant [4 x i8] c"%s\0a\00"
@".str8" = private unnamed_addr constant [4 x i8] c"uno\00"
@".str9" = private unnamed_addr constant [4 x i8] c"%s\0a\00"
@".str10" = private unnamed_addr constant [4 x i8] c"dos\00"
@".str11" = private unnamed_addr constant [4 x i8] c"%s\0a\00"
@".str12" = private unnamed_addr constant [5 x i8] c"otro\00"
@".str13" = private unnamed_addr constant [4 x i8] c"%s\0a\00"