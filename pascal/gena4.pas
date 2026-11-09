program gena;
 
const
 n=10;
 ac=9;
 pair=5;
 right_border=1;
 left_border=-32;
 exit_step_all=100000;
 exit_step_delta=50000;
 per_mutation_gen=75;
 per_mutation_bit=25;
 count_mutation=3;
 limit=1000000;
 
type
 gt = array [left_border..right_border] of boolean;
 generation = array [1..n] of gt;
 real_list = array [0..n] of real;
 int_list = array [0..n] of integer;

var
 flock: generation;
 ans_gen: gt;
 y_list: real_list;
 mask: int_list;
 y_min, y_max: real;
 step_all, step_delta: int64;
 test, testbd: boolean;
 str: string;
 

procedure swap(var a, b: boolean);
 var c: boolean;
 begin
 c:=a;
 a:=b;
 b:=c;
 end;
 
function f(x: real): real;
 begin 
 f:=x*(x-2)*(x-2.75)*exp(x/10)*cos(x/10)*(2-exp((x-2)*ln(3)));
 end;
 
function bin_to_dec(gen: gt): real;
 var i: integer;
  ans: real;
 begin
 ans:=0;
 for i:=left_border to right_border do
  if gen[i] then ans:=ans+exp(i*ln(2));
 bin_to_dec:=ans;
 end;
 
procedure print_unit_bin(var gen: gt);
 var i: integer;
 begin
 for i:=left_border to right_border do
  if ans_gen[i] then write('1')
  else write(0);
  
 end;
 
procedure print_unit_dec(var gen: gt);
 begin
 write(bin_to_dec(gen):ac:ac);
 end;
 
procedure print_flock();
 var i: integer;
 begin
 for i:=1 to n do
  begin
  if testbd then print_unit_bin(flock[i])
  else print_unit_dec(flock[i]);
  write(' ');
  end;
 writeln();
 end;
 
 
procedure new_flock();
 var i, j: integer;
 begin
 for i:=1 to n do
  for j:=left_border to right_border do
   if round(random())=1 then flock[i][j]:=True
   else flock[i][j]:=False;
 end;
 
procedure estimate();
 var i: integer;
 begin
 for i:=1 to n do
  begin
  y_list[i]:=f(bin_to_dec(flock[i]));
  if y_list[i]>y_max then
   begin
   y_max:=y_list[i];
   ans_gen:=flock[i];
   step_delta:=0;
   end;
  if y_list[i]<y_min then
   y_min:=y_list[i];
  end;
 step_all:=step_all+1;
 step_delta:=step_delta+1;
 end;
 
function ostanov(): boolean;
 begin 
 if (step_all>exit_step_all)
 or (step_delta>exit_step_delta)
 or (y_max>limit)
  then ostanov:=True
  else ostanov:=False;
 end;
 
procedure selection();
 var i, j, m1, m2: integer;
  r1, r2: real;
 begin
 for i:=1 to n do
  begin
  y_list[i]:=(y_list[i]-y_min+1)+y_list[i-1];
  mask[i-1]:=0;
  end;
 for i:=0 to (pair-1) do
  while True do
   begin
   r1:=random()*y_list[n];
   r2:=random()*y_list[n];
   for j:=1 to n do
    begin
          if (y_list[j-1]<=r1) and (r1<y_list[j]) and (mask[2*i]=0)
     then m1:=j;
    if (y_list[j-1]<=r2) and (r2<y_list[j]) and (mask[2*i]=0)
     then m2:=j;
    end;
   if m1<>m2 then
    begin
    mask[2*i]:=m1;
    mask[2*i+1]:=m2;
    break;
    end;
   end;
 end;
 
procedure crossing();
 var i, j, r: integer; 
 begin
 for i:=0 to (pair-1) do
  begin
  r:=round(random(right_border-left_border-1))+left_border;
  for j:=r to 1 do
   swap(flock[mask[2*i]][j], flock[mask[2*i+1]][j]);
  end;
 end;
 
procedure mutation();
 var i, j, r1, r2: integer;
 begin
 for i:=1 to count_mutation do
  begin
  r1:=round(random(n-1))+1;
  r2:=round(random(99))+1;
  if r2<=per_mutation_gen then 
   for j:=left_border to 1 do 
    begin 
    r2:=round(random(99))+1;
    if r2<per_mutation_bit then
     flock[r1][j]:=not(flock[r1][j]);
    end;
  end;
 end;


begin
randomize;
test:=False;
testbd:=True;
new_flock();

write('for test mod press "1", for main mod press 2: ');
readln(str);
if str='1' then test:=True;
if test then
 begin
 write('for bin press "1", for dec mod press 2: ');
 readln(str);
 if str='2' then testbd:=False;
 end;
writeln();

while True do 
 begin
 estimate;
 if test then
  begin
  write(step_all:4,': ');
  print_flock();
  end;
 if ostanov() then break;
 selection();
 crossing();
 mutation();
 end;

writeln();
write('For ', step_all, ' cycles, the value y=',
 f(bin_to_dec(ans_gen)):ac:ac, ' was found, which is acieved at x=',
 bin_to_dec(ans_gen):ac:ac, ' (with the [');
print_unit_bin(ans_gen);
writeln('] gene).');
end.
