program help; 
const n1=5; n2=10; n3=20; n4=50;
type vector = array [1..n4] of integer;
var a, ans_cmp, ans_swp: vector; swp, cmp, j, n, k, s1, s2, count: integer;
 
procedure swap(var a,b:integer);
var c:integer;
begin
	c:=a;
	a:=b;
	b:=c
end;
 
 
procedure write_v(var a:vector; n: integer);
var i:integer;
begin
    for i:=1 to n do 
    begin 
        write(a[i]);
        write(' ');
    end;
    writeln;
end; 
 
procedure tests(var list: vector; n, code:integer);
var i:integer;
begin
if code = 1 then 
	for i:=1 to n do list[i]:=i;
if code = 2 then
	for i:=1 to n do list[i]:= n - i + 1;
if code = 3 then
	for i:=1 to n do if (i mod 2 = 0) then list[i]:=n-i+1 else list[i]:=i;
if code=4 then
	for i:=1 to n do list[i]:=random(100);
if code=5 then
	for i:=1 to n do list[i]:=random(100);
end;
 
procedure bubble(var a: vector; n:integer);
var i:integer;
begin 
if n>1 then 
begin
    for i:=1 to n-1 do 
    begin
		cmp:=cmp+1;
		if a[i]>a[i+1] then 
			begin
			swap(a[i], a[i+1]);
			swp:=swp+1;
			end;
	end;
bubble(a, n-1);
end;
end;
 
 
procedure partition(var a:vector; l,r:integer; var q:integer);
var i, j:integer;
begin
	i:=l-1;
	for j:=l to r-1 do
	begin;
		cmp:=cmp+1;
		if a[j]<=a[r] then
		begin
			i:=i+1;
			swap(a[j],a[i]);
			if i<>j then swp:=swp+1;
		end;
	end;
	swap(a[i+1],a[r]);
	if i+1<>r then swp:=swp+1;
	q:=i+1
end;
 
procedure qsort(var a:vector; l,r:integer);
var q:integer;
begin
	if l<r then 
	begin
		partition(a,l,r,q);
		qsort(a,l,q-1);
		qsort(a,q+1,r)
	end
end;
 
procedure body(code: integer);
begin
    k:=1;
    if code=1 then writeln('BUBBLE') else writeln('QSORT');
    n:=0;
    while n <> n4 do
    begin
        if n = 0 then n := n1
        else if n = n1 then n := n2
        else if n = n2 then n := n3
        else if n = n3 then n := n4;
        for j:=1 to 5 do 
        begin 
        	tests(a, n, j);
        	cmp:=0; swp:=0;
        	write('unsorted: ');
        	write_v(a, n);
        	write('sorted: ');
        	if code=1 then bubble(a, n) else qsort(a, 1, n);
        	write_v(a, n);
        	ans_cmp[k]:=cmp;
        	ans_swp[k]:=swp;
        	k:=k+1;
        	writeln('cmp: ', cmp, ' ', 'swp: ', swp);
        	writeln('----------------------------------------------------------');
        end;
    end;
 
    writeln;
    writeln('*******************************************************************');
    writeln;
    writeln(' n | argument |           sequence      number                 | average |');
    writeln('   |          |       1      2      3      4      5            |         |');
    writeln('--------------------------------------------------------------------');
    n:=0;
    count:=0;
    while n <> n4 do
    begin
        if n = 0 then n := n1
        else if n = n1 then n := n2
        else if n = n2 then n := n3
        else if n = n3 then n := n4;
        begin 
        s1 := 0;
        s2 := 0;
        write(n:3,'|comparing|  ');  
        for j := count to count+5 do
        	begin
        	write(ans_cmp[j]:6,' ');
        	s1 := s1 + ans_cmp[j];
        	end;
 
        writeln('     | ', (s1 div 5):7,' |');
        write('   |swapping |  ');
 
        for j := count to count+5 do
        	begin
        	write(ans_swp[j]:6,' ');
        	s2 := s2 + ans_swp[j];
        	end;
        writeln('     | ', (s2 div 5):7,' |');
        writeln('--------------------------------------------------------------------');
        count:=count+5;
        end;
    end;
end; 
 
begin
randomize;
body(1);
body(2);
end.
