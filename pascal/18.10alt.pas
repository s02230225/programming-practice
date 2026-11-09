program oof;
type int = int64;
var k:int;


function pow(x, y:int):int;
begin
if y = 0 then pow:=1
else pow:=x*pow(x,y-1)
end;


function len(n: int):int;
begin
len := trunc(ln(n)/ln(10))+1
end;


function a( k, n:int):int;
var l: int;
begin
l := len(n);
k := k - l;
if k <= 0 then a := n div (pow(10, -k)) mod 10
else 
	begin 
	n := n + 1;
	a := a(k, n);
	end;
end;


function b( k, n:int):int;
var l: int;
begin
l := len(n);
k := k - l;
if k <= 0 then b := n div (pow(10, -k)) mod 10
else 
	begin 
	n := n + 2*trunc(sqrt(n)) + 1;
	b := b(k, n);
	end;
end;


function c( k, n, pred:int):int;
var l: int;
begin
l := len(n);
k := k - l;
if k <= 0 then c := n div (pow(10, -k)) mod 10
else 
	begin
	n := n + pred;
	c := c(k, n, n - pred);
	end;
end;



begin
write('Write down k: ');
readln(k);
writeln(a(k, 1));
writeln(b(k, 1));
writeln(c(k, 1, 0));
end.
		
		
		
	
