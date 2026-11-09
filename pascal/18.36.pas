program privetik;
const n = 4;
type list = ^node;
	node = record
		elem: char;
		next: list
		end;
	mass = array[1..n] of integer;
var q: list;
a: mass;
t: char;
s:integer;

procedure InitQueue(var q:list);
begin
q:=nil;
end;

procedure DelQueue(var q:list);
begin
if q = nil then exit;
if q^.next = nil then dispose(q)
else DelQueue(q^.next);
dispose(q);
end;


procedure InitArray(var a: mass);
var i:integer;
begin
writeln('Adding objects to massive!');
for i:=1 to n do
	begin
	write('Write down integer number ',i,': ');
	readln(a[i])
	end
end;


procedure AddElemQueue(var q: list; x:char);
begin
if q = nil then 
	begin
	new(q);
	q^.elem:=x;
	q^.next:=nil
	end
else AddElemQueue(q^.next, x)
end;


procedure DelElemQueue(var q: list);
begin
if q <> nil then
	if q^.next = nil then 
		begin
		dispose(q^.next);
		q:=nil
		end
	else DelElemQueue(q^.next);
end;



function Oper(sum,i:integer):boolean;

procedure Print(q: list; i:integer);
begin
if q <> nil then
	begin
	write(a[i],' ', q^.elem,' ');
	Print(q^.next, i+1);
	if i = n-1 then
		writeln(a[n]);
	end;
end;
	
begin
Oper := false;
if i = n then
	if sum = s then
		begin
		Oper:= true;
		write('Answer! ');
		Print(q,1)
		end
	else Oper:= false
else 
	begin
	AddElemQueue(q, '+');
	Oper:=Oper(sum + a[i+1], i+1) or Oper;
	t := '+';
	DelElemQueue(q);
	{write('+: ');
	Print(q,i);}
	AddElemQueue(q, '-');
	Oper:=Oper(sum - a[i+1], i+1) or Oper;
	t := '-';
	DelElemQueue(q);
	{write('-: ');
	Print(q,i);}
	AddElemQueue(q, '*');
	if t = '+' then
		Oper:=Oper(sum + a[i] * (a[i+1]-1), i+1) or Oper
	else 	Oper:=Oper(sum - a[i] * (a[i+1]-1), i+1) or Oper;
	DelElemQueue(q);
	{write('*: ');
	Print(q,i);}
	end;
end;
	
	

begin
InitArray(a);
InitQueue(q);
write('Write down s: ');
readln(s);
writeln(Oper(a[1],1));
writeln('End!');
end.
