program eightqueens(output);
{Looking for 1 solution of 8 queens problem}

var i : integer; q : boolean;
    a : array[ 1 .. 8] of boolean; {vertical lines}
    b : array[ 2 .. 16] of boolean; { / lines}
    c : array[ -7 .. 7] of boolean;{ \ lines}
    
    x : array[ 1 .. 8] of integer;{the array for accumulation solution}


procedure try( i : integer; var q : boolean);
{trying to put i-th queen, q=true if succeeded}

var j : integer; {will have values of all possible posiiton in the i-th row}

begin j := 0;
  repeat j := j + 1; q := false;
    if a[ j] and b[ i + j] and c[ i - j] then {the position is suitable}
    begin x[ i] := j;
      a[ j] := false; b[ i + j] := false; c[ i - j] := false;
      if i < 8 then
      begin try( i + 1, q);
        if not q then {impossible to put the rest queens - one step back}
        begin a[ j] := true; b[ i + j] := true; c[ i - j] := true;
        end
      end else q := true {the position is found}
    end
  until q or (j = 8);
end;


begin
{all the positions are suitable}
for i := 1 to 8 do a[  i] := true;
for i := 2 to 16 do b[  i] := true;
for i := -7 to 7 do c[  i] := true;

try( 1, q);

if q then
  for i := 1 to 8 do write( i:4, ' -- ' ,x[i]);
writeln

end.

