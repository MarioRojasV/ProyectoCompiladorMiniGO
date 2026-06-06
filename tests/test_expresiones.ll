; ModuleID = "miniGO"
target triple = "x86_64-pc-windows-msvc"
target datalayout = ""

define i32 @"main"()
{
entry:
  %"a" = alloca i64
  store i64 10, i64* %"a"
  %"b" = alloca i64
  store i64 3, i64* %"b"
  %"a.1" = load i64, i64* %"a"
  %"b.1" = load i64, i64* %"b"
  %".4" = add i64 %"a.1", %"b.1"
  %".5" = getelementptr inbounds [6 x i8], [6 x i8]* @".str0", i32 0, i32 0
  %".6" = call i32 (i8*, ...) @"printf"(i8* %".5", i64 %".4")
  %"a.2" = load i64, i64* %"a"
  %"b.2" = load i64, i64* %"b"
  %".7" = sub i64 %"a.2", %"b.2"
  %".8" = getelementptr inbounds [6 x i8], [6 x i8]* @".str1", i32 0, i32 0
  %".9" = call i32 (i8*, ...) @"printf"(i8* %".8", i64 %".7")
  %"a.3" = load i64, i64* %"a"
  %"b.3" = load i64, i64* %"b"
  %".10" = mul i64 %"a.3", %"b.3"
  %".11" = getelementptr inbounds [6 x i8], [6 x i8]* @".str2", i32 0, i32 0
  %".12" = call i32 (i8*, ...) @"printf"(i8* %".11", i64 %".10")
  %"a.4" = load i64, i64* %"a"
  %"b.4" = load i64, i64* %"b"
  %".13" = sdiv i64 %"a.4", %"b.4"
  %".14" = getelementptr inbounds [6 x i8], [6 x i8]* @".str3", i32 0, i32 0
  %".15" = call i32 (i8*, ...) @"printf"(i8* %".14", i64 %".13")
  %"a.5" = load i64, i64* %"a"
  %"b.5" = load i64, i64* %"b"
  %".16" = srem i64 %"a.5", %"b.5"
  %".17" = getelementptr inbounds [6 x i8], [6 x i8]* @".str4", i32 0, i32 0
  %".18" = call i32 (i8*, ...) @"printf"(i8* %".17", i64 %".16")
  %"a.6" = load i64, i64* %"a"
  %"b.6" = load i64, i64* %"b"
  %".19" = add i64 %"a.6", %"b.6"
  %".20" = mul i64 %".19", 2
  %"c" = alloca i64
  store i64 %".20", i64* %"c"
  %"c.1" = load i64, i64* %"c"
  %".22" = getelementptr inbounds [6 x i8], [6 x i8]* @".str5", i32 0, i32 0
  %".23" = call i32 (i8*, ...) @"printf"(i8* %".22", i64 %"c.1")
  %"a.7" = load i64, i64* %"a"
  %"b.7" = load i64, i64* %"b"
  %".24" = mul i64 %"a.7", %"b.7"
  %"a.8" = load i64, i64* %"a"
  %"b.8" = load i64, i64* %"b"
  %".25" = sub i64 %"a.8", %"b.8"
  %".26" = mul i64 %".25", 2
  %".27" = add i64 %".24", %".26"
  %"d" = alloca i64
  store i64 %".27", i64* %"d"
  %"d.1" = load i64, i64* %"d"
  %".29" = getelementptr inbounds [6 x i8], [6 x i8]* @".str6", i32 0, i32 0
  %".30" = call i32 (i8*, ...) @"printf"(i8* %".29", i64 %"d.1")
  %"a.9" = load i64, i64* %"a"
  %".31" = icmp eq i64 %"a.9", 10
  %".32" = getelementptr inbounds [6 x i8], [6 x i8]* @".str7", i32 0, i32 0
  %".33" = getelementptr inbounds [7 x i8], [7 x i8]* @".str8", i32 0, i32 0
  %".34" = select  i1 %".31", i8* %".32", i8* %".33"
  %".35" = call i32 (i8*, ...) @"printf"(i8* %".34")
  %"a.10" = load i64, i64* %"a"
  %"b.9" = load i64, i64* %"b"
  %".36" = icmp ne i64 %"a.10", %"b.9"
  %".37" = getelementptr inbounds [6 x i8], [6 x i8]* @".str9", i32 0, i32 0
  %".38" = getelementptr inbounds [7 x i8], [7 x i8]* @".str10", i32 0, i32 0
  %".39" = select  i1 %".36", i8* %".37", i8* %".38"
  %".40" = call i32 (i8*, ...) @"printf"(i8* %".39")
  %"a.11" = load i64, i64* %"a"
  %"b.10" = load i64, i64* %"b"
  %".41" = icmp sgt i64 %"a.11", %"b.10"
  %".42" = getelementptr inbounds [6 x i8], [6 x i8]* @".str11", i32 0, i32 0
  %".43" = getelementptr inbounds [7 x i8], [7 x i8]* @".str12", i32 0, i32 0
  %".44" = select  i1 %".41", i8* %".42", i8* %".43"
  %".45" = call i32 (i8*, ...) @"printf"(i8* %".44")
  %"a.12" = load i64, i64* %"a"
  %"b.11" = load i64, i64* %"b"
  %".46" = icmp slt i64 %"a.12", %"b.11"
  %".47" = getelementptr inbounds [6 x i8], [6 x i8]* @".str13", i32 0, i32 0
  %".48" = getelementptr inbounds [7 x i8], [7 x i8]* @".str14", i32 0, i32 0
  %".49" = select  i1 %".46", i8* %".47", i8* %".48"
  %".50" = call i32 (i8*, ...) @"printf"(i8* %".49")
  %"a.13" = load i64, i64* %"a"
  %".51" = icmp sge i64 %"a.13", 10
  %".52" = getelementptr inbounds [6 x i8], [6 x i8]* @".str15", i32 0, i32 0
  %".53" = getelementptr inbounds [7 x i8], [7 x i8]* @".str16", i32 0, i32 0
  %".54" = select  i1 %".51", i8* %".52", i8* %".53"
  %".55" = call i32 (i8*, ...) @"printf"(i8* %".54")
  %"a.14" = load i64, i64* %"a"
  %"b.12" = load i64, i64* %"b"
  %".56" = icmp sle i64 %"a.14", %"b.12"
  %".57" = getelementptr inbounds [6 x i8], [6 x i8]* @".str17", i32 0, i32 0
  %".58" = getelementptr inbounds [7 x i8], [7 x i8]* @".str18", i32 0, i32 0
  %".59" = select  i1 %".56", i8* %".57", i8* %".58"
  %".60" = call i32 (i8*, ...) @"printf"(i8* %".59")
  %"f" = alloca double
  store double 0x40091eb851eb851f, double* %"f"
  %"g" = alloca double
  store double 0x4000000000000000, double* %"g"
  %"f.1" = load double, double* %"f"
  %"g.1" = load double, double* %"g"
  %".63" = fadd double %"f.1", %"g.1"
  %".64" = getelementptr inbounds [4 x i8], [4 x i8]* @".str19", i32 0, i32 0
  %".65" = call i32 (i8*, ...) @"printf"(i8* %".64", double %".63")
  %"f.2" = load double, double* %"f"
  %"g.2" = load double, double* %"g"
  %".66" = fsub double %"f.2", %"g.2"
  %".67" = getelementptr inbounds [4 x i8], [4 x i8]* @".str20", i32 0, i32 0
  %".68" = call i32 (i8*, ...) @"printf"(i8* %".67", double %".66")
  %"f.3" = load double, double* %"f"
  %"g.3" = load double, double* %"g"
  %".69" = fmul double %"f.3", %"g.3"
  %".70" = getelementptr inbounds [4 x i8], [4 x i8]* @".str21", i32 0, i32 0
  %".71" = call i32 (i8*, ...) @"printf"(i8* %".70", double %".69")
  %"f.4" = load double, double* %"f"
  %"g.4" = load double, double* %"g"
  %".72" = fdiv double %"f.4", %"g.4"
  %".73" = getelementptr inbounds [4 x i8], [4 x i8]* @".str22", i32 0, i32 0
  %".74" = call i32 (i8*, ...) @"printf"(i8* %".73", double %".72")
  %"suma" = alloca i64
  store i64 0, i64* %"suma"
  %".76" = load i64, i64* %"suma"
  %".77" = add i64 %".76", 5
  store i64 %".77", i64* %"suma"
  %".79" = load i64, i64* %"suma"
  %".80" = add i64 %".79", 3
  store i64 %".80", i64* %"suma"
  %"suma.1" = load i64, i64* %"suma"
  %".82" = getelementptr inbounds [6 x i8], [6 x i8]* @".str23", i32 0, i32 0
  %".83" = call i32 (i8*, ...) @"printf"(i8* %".82", i64 %"suma.1")
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
@".str7" = private unnamed_addr constant [6 x i8] c"true\0a\00"
@".str8" = private unnamed_addr constant [7 x i8] c"false\0a\00"
@".str9" = private unnamed_addr constant [6 x i8] c"true\0a\00"
@".str10" = private unnamed_addr constant [7 x i8] c"false\0a\00"
@".str11" = private unnamed_addr constant [6 x i8] c"true\0a\00"
@".str12" = private unnamed_addr constant [7 x i8] c"false\0a\00"
@".str13" = private unnamed_addr constant [6 x i8] c"true\0a\00"
@".str14" = private unnamed_addr constant [7 x i8] c"false\0a\00"
@".str15" = private unnamed_addr constant [6 x i8] c"true\0a\00"
@".str16" = private unnamed_addr constant [7 x i8] c"false\0a\00"
@".str17" = private unnamed_addr constant [6 x i8] c"true\0a\00"
@".str18" = private unnamed_addr constant [7 x i8] c"false\0a\00"
@".str19" = private unnamed_addr constant [4 x i8] c"%f\0a\00"
@".str20" = private unnamed_addr constant [4 x i8] c"%f\0a\00"
@".str21" = private unnamed_addr constant [4 x i8] c"%f\0a\00"
@".str22" = private unnamed_addr constant [4 x i8] c"%f\0a\00"
@".str23" = private unnamed_addr constant [6 x i8] c"%lld\0a\00"