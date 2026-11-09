program main;
{$calling stdcall}
{$L ‪C:\Users\egor1\OneDrive\Рабочий стол\Внебрачный сын паскаля и ассемблера\main\moduls\module_1.obj}
var x, y: longint;
function check(var a, b: longint): longint; external name '_check@0';
begin
read(x);
read(y);
if ((x>0) and (y>0)) then
	begin
	writeln('check = ', check(x, y));
	writeln('x = ', x);
	writeln('y = ', y)
	end
else writeln('ERROR INPUT!!!')
end.
