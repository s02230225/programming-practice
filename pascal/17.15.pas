program help;
type tree = ^tnode;
	tnode = record
		key: char;
		left: tree;
		right: tree;
		end;
var t:tree=nil;
f:text;

procedure TDel(var t:tree);
begin
if t <> nil then
	begin
	TDel(t^.left);
	TDel(t^.right);
	dispose(t)
	end
end;
	

procedure InitT(var t:tree);
begin
new(t);
t^.left := nil;
t^.right := nil;
end;


function TResult(t:tree):integer; // Пункт а
begin
if (t^.left = nil) and (t^.right = nil) then TResult := ord(t^.key) - ord('0')
else
	if t^.key = '+' then TResult := TResult(t^.left) + TResult(t^.right)
	else if t^.key = '-' then TResult := TResult(t^.left) - TResult(t^.right)
	else TResult:= TResult(t^.left) * TResult(t^.right)
end;


function Letter(x:char):boolean;
begin
Letter:=(x in ['0'..'9']) or (x in ['a'..'z'])
end;


function Oper(x:char):boolean;
begin
Oper := x in ['+', '-', '*'];
end;


function TCheck(t:tree):boolean; // Пункт б
begin
if (t^.left = nil) and (t^.right = nil) then TCheck := Letter(t^.key)
else if ((t^.left <> nil) and (t^.right = nil)) or ((t^.left = nil) and (t^.right <> nil)) then TCheck := false
else TCheck := Oper(t^.key) and TCheck(t^.left) and TCheck(t^.right);
end;


procedure Builder(var f:text; var t:tree); // Пункт в
var x:char;
begin
if eoln(f) then exit;
read(f,x);
if x = '(' then
	begin
	InitT(t^.left);
	// writeln('Left');
	Builder(f, t^.left);
	read(f,x);
	// writeln('Mid ',x);
	t^.key := x;
	InitT(t^.right);
	Builder(f, t^.right);
	// writeln('Right');
	Builder(f, t);
	end
else if x = ')' then exit
else if Oper(x) or Letter(x) then
	begin
	t^.key := x;
	// write(x,' ');
	end
end;
	
	
procedure Form(var f:text; var t:tree); // Пункт г
begin
if (t^.left = nil) and (t^.right = nil) then write(f,t^.key)
else
	begin
	write(f, '(');
	Form(f, t^.left);
	write(f,t^.key);
	Form(f, t^.right);
	write(f, ')');
	end
end;


procedure Postfix(var f:text; var t:tree); // Пункт д
begin
if (t^.left = nil) and (t^.right = nil) then write(f,t^.key)
else
	begin
	Postfix(f, t^.left);
	Postfix(f, t^.right);
	write(f,t^.key);
	end
end;

	
procedure Prefix(var f:text; var t:tree); // Пункт е
begin
if (t^.left = nil) and (t^.right = nil) then write(f,t^.key)
else
	begin
	write(f,t^.key);
	Prefix(f, t^.left);
	Prefix(f, t^.right);
	end
end;


begin
assign(f, 'Form.txt');
reset(f);
InitT(t);
Builder(f,t); // Пункт в
close(f);
writeln(TResult(t)); // Пункт а
writeln('Check: ', TCheck(t)); // Пункт б
// Теперь вывод
assign(f, 'Form.txt');
rewrite(f);
Form(f,t); // Пункт г - результат в файле
writeln(f);
Postfix(f,t); // Пункт д - результат в файле
writeln(f);
Prefix(f,t); // Пункт е - результат в файле
close(f);
TDel(t);
writeln('Work is done!');
end.
