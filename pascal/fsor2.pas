program www1;
 
 
var i,n: integer;
    name: string;
    tfile: text;
    
begin
n:=20;
name:='sorttest.txt';
assign(tfile, name);
rewrite(tfile);
for i:=1 to n do
    write(tfile, i, ' ');
writeln(tfile);
for i:=n downto 1 do
    write(tfile, i, ' ');
writeln(tfile);
for i:=1 to n do
    begin
    if (i mod 2=0) then write(tfile, i, ' ')
    else write(tfile, -i, ' ');
    end;
writeln(tfile);
for i:=1 to n do
    write(tfile, round(random(101)), ' ');
writeln(tfile);
for i:=1 to n do
    write(tfile, round(random(101)), ' ');
writeln(tfile);
close(tfile);
end.
 
