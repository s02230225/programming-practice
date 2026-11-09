program Wut;
// Т.к. при просмотре постфиксной записи неясно, как разделять, например, 571+ : 5+71 или 57+1,
// То примем '0' -- '9' за 0 -- 9, a -- z за 10 -- 35, A -- Z за 36 -- 61
type list = ^node;
	node = record
		elem: integer;
		next: list;
		end;
var st: list=nil;
f : text;

procedure AddElemStack(var q: list; x:integer);
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


function DelElemStack(var q: list):integer;
begin
if q <> nil then
	if q^.next = nil then 
		begin
		DelElemStack:=q^.elem;
		dispose(q^.next);
		q:=nil
		end
	else DelElemStack:=DelElemStack(q^.next)
else DelElemStack:= 0
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


function Transform(x : char):integer;
begin
if ('0' <= x) and (x <= '9') then Transform := ord(x)-ord('0')
else if ('a' <= x) and (x <= 'z') then Transform := ord(x)-ord('a')+10
else if ('A' <= x) and (x <= 'Z') then Transform := ord(x)-ord('A')+36
end;


function Value(var f : text):integer;
var x:char;
s:integer;
begin
reset(f);
s := 0;
while not eoln(f) do
	begin
	read(f,x);
	if x = '+' then  
		begin
		s := DelElemStack(st) + DelElemStack(st);
		AddElemStack(st, s);
		end
	else if x = '-' then 
		begin
		s := - DelElemStack(st) + DelElemStack(st);
		AddElemStack(st, s);
		end
	else if x = '*' then 
		begin
		s := DelElemStack(st) * DelElemStack(st);
		AddElemStack(st, s);
		end
	else if x = '^' then 
		begin
		s := trunc( exp( DelElemStack(st) * ln(DelElemStack(st)) ));
		AddElemStack(st, s);
		end
	else 
		AddElemStack(st, Transform(x));
	end;
Value:=DelElemStack(st);
end;



begin
assign(f, 'postfix.txt');
writeln('Started working!');
writeln('Result of processing file postfix.txt: ', Value(f));
DelStack(st);
writeln('End!');
end.
