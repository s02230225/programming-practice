program sus;
// Т.к. при просмотре постфиксной записи неясно, как разделять, например, 571+ : 5+71 или 57+1,
// То примем '0' -- '9' за 0 -- 9, a -- z за 10 -- 35, A -- Z за 36 -- 61
type list = ^node;
	node = record
		elem: char;
		next: list;
		end;
var st: list=nil;
que :list = nil;
inf,postf : text;


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
else DelElemStack:= ' '
end;


function DelElemQ(var q: list):char;
var p: list;
begin
if q <> nil then
	begin
	p:=q^.next;
	DelElemQ:=q^.elem;
	dispose(q);
	q:=p
	end
else DelElemQ:= ' '
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


function Allowed(x: char):boolean;
begin
if x in ['(',')','+','*','-','^'] then Allowed := true
else Allowed := false
end;


procedure Adult(x:char); // Пишем в файл операторы с приоритетом не менее данного.
var q:char;
begin
q := DelElemStack(st);
while (q <> '(') and (q <> ')') do
	begin
	if (x in ['*', '^']) and (q in ['+', '-']) then
		AddElemStack(que, q)
	else
		write(postf,q);
	q := DelElemStack(st);
	end;
AddElemStack(st, q);
while que <> nil do
	begin
	q:= DelElemQ(que);
	AddElemStack(st, q);
	end
end;

procedure Translate(var inf,postf:text);
var x:char;
begin
reset(inf);
rewrite(postf);
while not(eoln(inf)) do
	begin
	read(inf,x);
	if Allowed(x) then 
		begin
		if x = '(' then AddElemStack(st, x)
		else if x = ')' then
			begin
			x := DelElemStack(st);
			while x <> '(' do
				begin
				write(postf,x);
				x := DelElemStack(st);
				end
			end
		else 
			begin
			Adult(x);
			AddElemStack(st,x)
			end
		end
	else write(postf,x);
	end;
close(inf);
close(postf);
end;


begin
assign(inf, 'infix.txt');
assign(postf, 'postfix.txt');
writeln('Started working!');
Translate(inf,postf);
DelStack(st);
DelStack(que);
writeln('End!');
end.

