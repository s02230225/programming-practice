program gena;

const eps=1/16384;
	n=10;
	maxx_operation=10000;
	maxx_amount_of_notdiff=1000;
	p_xman=40;
	p_xman_bit=10;
	amount_of_xman=2;
	infinity=10000000000;

type gen_type = array [-14..1] of boolean;
	f_type = array [0..n] of real;
	generation_type = array [1..n] of gen_type;
	
var generation: generation_type;
	gen_maxx: gen_type;
	f_array: f_type;
	maxx, minn: real;
	operation, amount_of_notdiff, x1, x2 : integer;

procedure swap(var a, b: boolean);
	var c: boolean;
	begin
		c:=a;
		a:=b;
		b:=c;
	end;

function f(x: real): real;
	begin 
		f:=x*(x-2)*(x-2.75)*exp(x/10)*cos(x/10)*(2-exp((x-2)*ln(3))) 
	end;

function bin_to_dec(gen: gen_type): real;
	var i: integer;
		ans: real;
	begin
		ans:=0;
		for i:=-14 to 1 do
			if gen[i] then ans:=ans+exp(i*ln(2));
		bin_to_dec:=ans;
	end;

procedure print_generation();
	var i: integer;
	begin
		for i:=1 to n do
			begin
				write(bin_to_dec(generation[i]):5:5);
				write(' ');
			end;
		writeln();
	end;

	 
procedure newgen();
	var i, j: integer;
	begin
	for i:=1 to n do
		for j:=-14 to 1 do
			begin
				if round(random())=0 then generation[i][j]:=False
				else generation[i][j]:=True;
			end
	end;
	
procedure check();
	var i: integer;
	begin
		for i:=1 to n do
			begin
				f_array[i]:=f(bin_to_dec(generation[i]));
				if f_array[i]>maxx then
					begin
					maxx:=f_array[i];
					gen_maxx:=generation[i];
					amount_of_notdiff:=0;
					end;
				if f_array[i]<minn then minn:=f_array[i];
			end;
		amount_of_notdiff:=amount_of_notdiff+1;
		operation:=operation+1;
	end;

function stop_(): boolean;
begin 
	if (operation>maxx_operation) or (amount_of_notdiff>maxx_amount_of_notdiff)
	   or (maxx>infinity) then stop_:=True else stop_:=False
end;

procedure selection();
	var  i: integer; r1, r2: real;
	begin
		for i:=1 to n do f_array[i]:=f_array[i]-minn+1;
		for i:=1 to n do f_array[i]:=f_array[i-1]+f_array[i];
		r1:=random()*f_array[n];
		r2:=random()*f_array[n];
		for i:=1 to n do
		begin
			if (f_array[i-1]<=r1) and (r1<f_array[i]) then x1:=i;
			if (f_array[i-1]<=r2) and (r2<f_array[i]) then x2:=i;
		end;
	end;
	
procedure crossing();
	var number, i: integer; 
	begin
	number:=round(random(14))-14;
	for i:=number to 1 do 
		swap(generation[x1][i], generation[x2][i]);
	end;

procedure mutation();
	var gen1_num, gen2_num, i: integer; p1, p2, p: real;
	begin
		gen1_num:=round(random(n))+1;
		gen2_num:=round(random(n))+1;
		while gen1_num=gen2_num do gen2_num:=round(random(n))+1;
		p1:=random(100);
		p2:=random(100);
		if p1<p_xman then 
		begin 
			for i:=-14 to 1 do 
			begin 
				p:=round(random(100));
				if p<p_xman_bit then
					generation[gen1_num][i]:=not(generation[gen1_num][i])
			end
		end;
		if p2<p_xman then 
		begin 
			for i:=-14 to 1 do 
			begin 
				p:=round(random(100));
				if p<p_xman_bit then
					generation[gen2_num][i]:=not(generation[gen1_num][i])
			end
		end;
	end;




var i, j: integer;	test_or_not, stop_or_not: boolean; a: char;
 sss: real;
begin
randomize;
maxx:=-1000000000;
minn:=1000000000;

writeln('test mode? yes-press y, no-press n');
readln(a);
if a='y' then test_or_not:=True else test_or_not:=False;
sss:=0;
for j:=1 to 10000 do
begin
newgen();

while True do 
begin
	x1:=0;
	x2:=0;
	check;
	if test_or_not then print_generation;
	stop_or_not:=stop_;
	if stop_or_not then break;
	selection;
	crossing;
	mutation;
end;
sss:=sss+bin_to_dec(gen_maxx);
end;
writeln(sss/10000:5:5);

end.
