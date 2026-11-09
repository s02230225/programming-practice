program byPugachev1238;
const n=10;
	os=3;
	flag=True;
	name='sortresult.txt';

type vector = array[0..n-1] of integer;

var tfile: text;
	count, counts, countm: integer;
	

procedure swap(var a,b: integer);
var c: integer;
   begin
   c:=a; a:=b; b:=c
   end;

procedure input(var a: vector);
    var i: integer;
    begin
    for i:=1 to n do read(a[i])
    end;

procedure print(var a: vector);
    var i: integer;
    begin
    for i:=1 to n do write(a[i], ' ');
    writeln();
    end;

procedure rewr(var a: vector; count: integer);
	var i: integer;
	begin
	write(tfile, count:os ,') ');
	for i:=1 to n do
		write(tfile, a[i], ' ');
	writeln(tfile);
	end;
	
function min(x1, x2: integer): integer;
	begin
	if x1<=x2 then min:=x1
	else min:=x2;
	end;


procedure main1(var a: vector);
	var i, j, l, m, r, x: integer;
	begin
	count:=0;
	counts:=0;
	countm:=0;
	if flag then rewr(a, count);
	for i:=1 to n-1 do
		begin
		x:=a[i];
		l:=0;
		r:=i-2;
		repeat
			begin
			m:=(l+r) div 2;
			counts:=counts+1;
			if a[m]<x then l:=m+1
			else r:=m-1;
			end;
		until l>r;
		for j:=i-1 downto l do
			begin
			countm:=countm+1;
			a[j+1]:=a[j];
			end;
		a[l]:=x;
		count:=count+1;
		if flag then rewr(a, count);
		end;
	write('Sorting by binary inserts has finished its work in ');
	writeln(counts, ' comparisons and ', countm, ' replacements.');
	writeln('Result (see the steps in the "sortresult.txt" file) :');
	print(a);
	end;


procedure merge(var a: vector; l, m, r: integer);
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
			counts:=counts+1;
			countm:=countm+1;
			end
		else
			begin
			res[it1+it2]:=a[m+it2];
			it2:=it2+1;
			counts:=counts+1;
			countm:=countm+1;
			end
		end;
	while l+it1<m do
		begin
		res[it1+it2]:=a[l+it1];
		it1:=it1+1;
		countm:=countm+1;
		end;
	while m+it2<r do
		begin
		res[it1+it2]:=a[m+it2];
		it2:=it2+1;
		countm:=countm+1;
		end;
	for i:=0 to (it1+it2) do
		begin
		a[l+i]:=res[i];
		countm:=countm+1;
		end;
	end;
	
procedure main2(var a: vector);
	var i, j: integer;
	begin
	i:=1;
	if flag then rewr(a, count);
	while i<=n do
		begin
		j:=0;
		while j<=n-i do
			begin
			merge(a, j, j+i, min(j+i*2, n));
			count:=count+1;
			if flag then rewr(a, count);
			j:=j+i*2;
			end;
		i:=i*2;
		end;
	write('Sorting by simple inserts has finished its work in ');
	writeln(counts, ' comparisons and ', countm, ' replacements(/2).');
	writeln('Result (see the steps in the "sortresult.txt" file) :');
	print(a);
	end;
	

// -1 1 1 2 2 3 3 4 5 6
// 6 3 1 2 5 4 3 2 1 -1
var a: vector;
begin
if flag then
	begin
	assign(tfile, name);
	rewrite(tfile);
	writeln(tfile, '----------begin----------');
	end;
input(a);
// choosing a sort
main2(a);
writeln(tfile, '----------end----------');
close(tfile);
end.
