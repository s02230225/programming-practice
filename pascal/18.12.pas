program Hello;
// I - 1 V - 5 X - 10 L - 50 C - 100 D - 500 M - 1000
type list = ^node;
	node = record
		elem: char;
		next: list;
		end;
var st:list=nil;
x:char='0';

procedure AddElemStack(var q: list; x:char);
begin
if q = nil then 
	begin
	new(q);
	q^.elem:=x;
	q^.next:=nil;
	{write('Added ',x,' ');}
	end
else AddElemStack(q^.next, x)
end;


function DelElemStack(var q: list):char;
begin
if q <> nil then
	if q^.next = nil then 
		begin
		DelElemStack:=q^.elem;
		dispose(q^.next);
		q:=nil
		end
	else DelElemStack:=DelElemStack(q^.next)
else DelElemStack:= '0'
end;



procedure Print(q: list);
begin
if q <> nil then
	begin
	write(q^.elem,' ');
	Print(q^.next);
	end
else writeln;
end;
	

procedure DelStack(var q:list);
begin
if q = nil then exit;
if q^.next = nil then dispose(q)
else DelStack(q^.next);
dispose(q);
end;


function Checker(prs, prv : char):integer; // IX XC CM и ещё IV XL CD
begin
if (prs = 'I') and ((prv = 'X') or (prv = 'V')) then Checker:= -1
else if (prs = 'X') and ((prv = 'C') or (prv = 'L')) then Checker:= -10
else if (prs = 'C') and ((prv = 'M') or (prv = 'D')) then Checker:= -100 

else if prs = 'I' then Checker := 1
else if prs = 'V' then Checker := 5
else if prs = 'X' then Checker := 10
else if prs = 'L' then Checker := 50
else if prs = 'C' then Checker := 100
else if prs = 'D' then Checker := 500
else if prs = 'M' then Checker := 1000
end;


function Reader(var st: list):integer;
var prs, prv : char;
begin
prs := '0';
Reader:=0;
while st <> nil do
	begin
	prv := prs;
	prs:=DelElemStack(st);
	{writeln(prv,' ',prs);}
	Reader:=Reader + Checker(prs,prv);
	{Print(st)}
	end
end;


begin
writeln('Write down a number in Riman Counting System: ');
read(x);
while x <> ' ' do 
	begin
	AddElemStack(st,x);
	read(x);
	end;
writeln(Reader(st));
end.
