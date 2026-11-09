program sus;
var k,n:integer;

function pow(x,y:integer):integer; // Только для натуральных чисел, вывод соответственно только натуральное число
begin
if y = 0 then pow:=1
else pow:=x*pow(x,y-1);
end;

function amount(x:integer):integer; // Целая часть sqrt(10**n)
begin
if x = 0 then amount:=0
else amount:=trunc(sqrt(pow(10,x))) - (x-1) mod 2 // Но также нам не подходят степени 100.
end;

function digit(var n:integer; k:integer):integer;
var t,i:integer;
begin
t:=n*(amount(n) - amount(n-1)); // количество цифр всех n-значных полных квадратов
writeln('t: ', t);
if k > t then
	begin
	n:=n+1;
	writeln(n);
	digit:=digit(n,k-t)
	end
else 
	begin
	t:=amount(n-1) + 1 + (k-1) div n;
	t:= t * t; // Строим n-значное число нужного порядка
	writeln(n,' ', t);
	writeln(n - 1 - ((k-1) mod n)); // Отладка
	i:=pow(10, n - 1 - ((k-1) mod n)); // 10**(n-1) --- 10**0 в зависимости от нужной цифры
	digit:= (t div i) mod 10
	end;
end;

begin
n:=1;
writeln('Write down k: ');
readln(k);
k:=digit(n,k);
writeln('Result: ',k);
writeln('End!');
end.

