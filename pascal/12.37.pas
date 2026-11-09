Program TwelveThirtySix;
uses Base;
const N=5;

type vector = array[1..N] of int64;
var a:vector;
	s,p:int64;
	i,amount,mamount:integer;
	ok:boolean;
	b,res,o,c:string;
	
function Sum(i,l,k:integer;p:int64;res:string):int64;
var j:integer;
	
begin
for j:=i to N do begin
	{writeln(j,' ',k,' ',p);}
	if k=1 then begin
		p:=a[j];
		str(p,b);
		res:=b;
		if p=s then begin
			{writeln(ok,' ',res);}
			if not ok then 
				o:=res;
			ok:=true;
			
			break
		end
		else begin
			if (j+1<=N) and (k<l) then 
				Sum(j,l,k+1,p,res);
		end;
	end
	else begin
		if p+a[j]=s then begin

			str(a[j],b);
			res:=res + ' '+ b + ' ';
			{writeln(ok,' ',res);}
			if not ok then 
				o:=res;
			ok:=true;
					
			break
		end
		else
			if p+a[j]<s then
				if (j+1<=N) and (k<l) then begin
					str(a[j],b);
					Sum(j,l,k+1,p+a[j],res+' '+ b)
				end
			else
				break
	end;
	
end;
end;



begin
res:='';
ok:=false;
InpArray(a);
readln(s);

Reverse(a);

for i:=1 to N do begin
	p:=0;
	Sum(1,i,1,p,res);
end;
writeln(ok,' ',o);


end.

