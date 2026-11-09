program privetik;
const n = 5;
type vector = array[1..n] of integer;
var a:vector;
s,t,sum:integer;

procedure InitVector(var a:vector);
var i: integer;
begin
writeln('Adding elements to array!');
for i:=1 to n do
	begin
	write('Write down element number ',i,': ');
	readln(a[i])
	end;
end;


function FindMax(var a:vector):integer;
var i:integer;
begin
FindMax:=1;
for i:=2 to n do
	if a[i] >= a[FindMax] then FindMax:=i;
end;


function Summa(var a:vector):integer;
var i:integer;
begin
Summa:=0;
for i:=1 to n do
	Summa:=Summa+a[i]
end;


procedure PrintVector(var a:vector);
var i:integer;
begin
writeln;
for i:=1 to n do
	write(a[i],' ')
end;


begin
InitVector(a);
write('Write down s: ');
readln(s);
sum:=Summa(a);
while sum >= s do
	begin
	t:=FindMax(a);
	sum:= sum - a[t];
	a[t]:=0
	end;
PrintVector(a);
end.
