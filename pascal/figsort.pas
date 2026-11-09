program figsort;

const
	name='allresult.txt';
	os=3;
	a1=10;
	a2=20;
	a3=50;
	a4=100;
	
type
	vector = array[0..100] of integer;
	TF = function(n: integer): vector;

var
	tfile: text;
	srs1, srm1, srs2, srm2: real;

function gen1(n: integer): vector;
	var i: integer;
	begin
	for i:=1 to n do
		gen1[i-1]:=i;
	end;
	
function gen2(n: integer): vector;
	var i: integer;
	begin
	for i:=1 to n do
		gen2[i-1]:=-i;
	end;
	
function gen3(n: integer): vector;
	var i: integer;
	begin
	for i:=1 to n do
		begin
		if (i mod 2=0) then gen3[i-1]:=i
		else gen3[i-1]:=-i;
		end;
	end;

function gen4(n: integer): vector;
	var i: integer;
	begin
	for i:=1 to n do
		gen4[i-1]:=round(random(100));
	end;
	
procedure sort1(var a: vector; var n, cs, cm: integer);
    var i, j, l, m, r, x: integer;
    begin
    for i:=0 to n-1 do
        begin
        x:=a[i];
        l:=0;
        r:=i-1;
        repeat
            begin
            m:=(l+r) div 2;
            cs:=cs+1;
            if a[m]<x then l:=m+1
            else r:=m-1;
            end;
        until l>r;
        for j:=i-1 downto l do
            begin
            cm:=cm+1;
            a[j+1]:=a[j];
            end;
        a[l]:=x;
        end;
    end;

procedure merge(var a: vector; n, l, m, r: integer; var cs, cm: integer);
    var i, it1, it2: integer;
        res: vector;
    begin
    it1:=0;
    it2:=0;
    for i:=0 to n-1 do res[i]:=0;
    while ((l+it1)<m) and ((m+it2)<r) do
        begin
        if a[l+it1]<a[m+it2] then
            begin
            res[it1+it2]:=a[l+it1];
            it1:=it1+1;
            cs:=cs+1;
            cm:=cm+1;
            end
        else
            begin
            res[it1+it2]:=a[m+it2];
            it2:=it2+1;
            cs:=cs+1;
            cm:=cm+1;
            end
        end;
    while l+it1<m do
        begin
        res[it1+it2]:=a[l+it1];
        it1:=it1+1;
        cm:=cm+1;
        end;
    while m+it2<r do
        begin
        res[it1+it2]:=a[m+it2];
        it2:=it2+1;
        cm:=cm+1;
        end;
    for i:=0 to (it1+it2-1) do
        begin
        a[l+i]:=res[i];
        cm:=cm+1;
        end;
    end;

function min(x1, x2: integer): integer;
    begin
    if x1<=x2 then min:=x1
    else min:=x2;
    end;

procedure sort2(var a: vector; n: integer; var cs, cm: integer);
    var i, j: integer;
    begin
    i:=1;
    while i<=n do
        begin
        j:=0;
        while j<=n-i do
            begin
            merge(a, n, j, j+i, min(j+i*2, n), cs, cm);
            j:=j+i*2;
            end;
        i:=i*2;
        end;
    end;

procedure print(var a: vector; var n: integer);
    var i: integer;
    begin
    for i:=0 to n-1 do write(tfile, a[i], ' ');
    writeln(tfile);
    end;
   
procedure main(n: integer; gen: TF);
	var mas, mas2: vector;
		cs, cm: integer;
	begin
	writeln(tfile, 'FIRST SORT:');
	mas:=gen(n);
	mas2:=mas;
	write(tfile, 'INPUT: ');
	print(mas, n);
	cs:=0; cm:=0;
	sort1(mas, n, cs, cm);
	srs1:=srs1+cs; srm1:=srm1+cm;
	write(tfile, 'OUTPUT: ');
	print(mas, n);
	writeln(tfile, n:os, ', ',cs:os,', ', cm:os, ' - elements, comparison, modification');
	writeln(tfile, 'SECOND SORT:');
	write(tfile, 'INPUT: ');
	print(mas2, n);
	cs:=0; cm:=0;
	sort2(mas2, n, cs, cm);
	srs2:=srs2+cs; srm2:=srm2+cm;
	write(tfile, 'OUTPUT: ');
	print(mas2, n);
	writeln(tfile, n:os, ', ',cs:os,', ', cm:os, ' - elements, comparison, modification');
	writeln(tfile);
	end;

begin
assign(tfile, name);
rewrite(tfile);
srs1:=0; srm1:=0;
srs2:=0; srm2:=0;
main(a1, @gen1);
main(a1, @gen2);
main(a1, @gen3);
main(a1, @gen4);
writeln('The meaning of comparisons and modifications');
writeln('The average value for 1 and 2 sorts for 10 values:');
writeln(srs1/4:os:os, '   ', srm1/4:os:os);
writeln(srs2/4:os:os, '   ', srm2/4:os:os);
srs1:=0; srm1:=0;
srs2:=0; srm2:=0;
main(a2, @gen1);
main(a2, @gen2);
main(a2, @gen3);
main(a2, @gen4);
writeln('The average value for 1 and 2 sorts for 20 values:');
writeln(srs1/4:os:os, '   ', srm1/4:os:os);
writeln(srs2/4:os:os, '   ', srm2/4:os:os);
srs1:=0; srm1:=0;
srs2:=0; srm2:=0;
main(a3, @gen1);
main(a3, @gen2);
main(a3, @gen3);
main(a3, @gen4);
writeln('The average value for 1 and 2 sorts for 50 values:');
writeln(srs1/4:os:os, '   ', srm1/4:os:os);
writeln(srs2/4:os:os, '   ', srm2/4:os:os);
srs1:=0; srm1:=0;
srs2:=0; srm2:=0;
main(a4, @gen1);
main(a4, @gen2);
main(a4, @gen3);
main(a4, @gen4);
writeln('The average value for 1 and 2 sorts for 100 values:');
writeln(srs1/4:os:os, '   ', srm1/4:os:os);
writeln(srs2/4:os:os, '   ', srm2/4:os:os);
close(tfile);
end.
