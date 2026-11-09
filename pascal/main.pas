program BigProgramByPugachev;
const
    n=100;
    s=63;
type
    tgun = record
        nam: string[s];
        caliber: real;
        automatic: boolean;
        yearconstruct: integer;
        end;
    tguns = array [1..n] of tgun;
    fod = file of tguns;
var i, count: integer;
    guns: tguns;
    zerogun: tgun;
    action: string[s];

procedure f1();
    var i, j: integer;
        filename: string[s];
        newguns: tguns;
        fod1: fod;
        flag: boolean;
    begin
    write('Введите имя файла загрузки: ');
    readln(filename);
    assign(fod1, filename);
    reset(fod1);
    read(fod1, newguns);
    for i:=1 to n do
        begin
        if newguns[i].nam='none' then break;
        flag:=true;
        for j:=1 to count do
            if guns[j].nam=newguns[i].nam then flag:=false;
        if flag then
            begin
            guns[count+1]:=newguns[i];
            count:=count+1;
            end;
        end;
    writeln('База данных загружена');
    close(fod1);
    end;

procedure f2();
    var filename: string[s];
        fod1: fod;
    begin
    write('Введите имя файла выгрузки: ');
    readln(filename);
    assign(fod1, filename);
    rewrite(fod1);
    write(fod1, guns);
    close(fod1);
    writeln('Успешно сохранено');
    end;

procedure f3();
    var i, year: integer;
        caliber: real;
        nam, ans: string[s];
        flag: boolean;
    begin
    flag:=true;
    writeln('Добавление оружия');
    write('Введите название: ');
    readln(nam);
    for i:=1 to count do
        begin
        if guns[i].nam=nam then
            begin
            writeln('Оружие с таким именем уже есть в базе данных');
            flag:=false;
            end;
        end;
    if flag then
        begin
        guns[count+1].nam:=nam;
        write('Введите калибр: ');
        readln(caliber);
        guns[count+1].caliber:=caliber;
        write('Если оружие автоматическое, то введите "да", иначе - "нет": ');
        readln(ans);
        if (ans='да') or (ans='yes') then guns[count+1].automatic:=true
        else guns[count+1].automatic:=false;
        write('Введите год производства: ');
        readln(year);
        guns[count+1].yearconstruct:=year;
        count:=count+1;
        end;
    end;

procedure f4();
    var i,j: integer;
        nam: string[s];
        flag: boolean;
    begin
    flag:=false;
    writeln('Удаление оружия');
    write('Введите название: ');
    readln(nam);
    for i:=1 to count do
        begin
        if guns[i].nam=nam then
            begin
            flag:=true;
            j:=i;
            break;
            end;
        end;
    if flag then
        begin
        for i:=j to n-1 do
            guns[i]:=guns[i+1];
        guns[n]:=zerogun;
        count:=count-1;
        writeln('Успешно удалено');
        end
    else writeln('Оружия с таким именем не найдено');
    end;

procedure printgun(i, k: integer);
    begin
    write(k, ') ' ,guns[i].nam,' с калибром ', guns[i].caliber:3:2);
    if guns[i].automatic=true then write(' ,автоматическое, ')
    else write(' ,неавтоматическое, ');
    write('впервые сконструированное в ');
    writeln(guns[i].yearconstruct, ' году');
    end;

procedure f5();
    var i: integer;
    begin
    if count=0 then writeln('Оружия не найдено')
    else
        begin
        writeln('Весь список оружия: ');
        for i:=1 to count do
            printgun(i, i);
        end;
    end;
    

procedure f6();
    var i, ans, year, k: integer;
        nam: string[s];
        caliber: real;
        flag: boolean;
    begin
    writeln('Если вы ищете оружие:');
    writeln(' по названию, то напишите "1"');
    writeln(' по калибру, то напишите "2"');
    writeln(' по году производства, то напишите "3"');
    writeln(' автоматическое, то напишите "4"');
    writeln(' автоматическое, то напишите "5"');
    write('Введите цифру: ');
    readln(ans);
    if ans=1 then
        begin
        write('Введите название: ');
        readln(nam);
        flag:=false;
        for i:=1 to count do
            if guns[i].nam=nam then 
                begin
                write('Оружие из списка с названием ', nam);
                write(' имеет калибр ', guns[i].caliber:3:2);
                if guns[i].automatic=true then write(' ,автоматическое, ')
                else write(' ,неавтоматическое, ');
                write('впервые сконструированное в ');
                writeln(guns[i].yearconstruct, ' году');
                flag:=true;
                end;
        if flag=false then writeln('Оружие с таким названием не найдено');
        end;
    if ans=2 then
        begin
        write('Введите калибр: ');
        readln(caliber);
        k:=1;
        flag:=false;
        for i:=1 to count do
            if guns[i].caliber=caliber then 
                begin
                printgun(i, k);
                flag:=true;
                k:=k+1;
                end;
        if flag=false then writeln('Оружие с таким калибром не найдено');
        end;
    if ans=3 then
        begin
        write('Введите год производства: ');
        readln(year);
        k:=1;
        flag:=false;
        for i:=1 to count do
            if guns[i].yearconstruct=year then 
                begin
                printgun(i, k);
                flag:=true;
                k:=k+1;
                end;
        if flag=false then
            writeln('Оружие с таким годом производства не найдено');
        end;
    if ans=4 then
        begin
        k:=1;
        flag:=false;
        for i:=1 to count do
            if guns[i].automatic=true then 
                begin
                printgun(i, k);
                flag:=true;
                k:=k+1;
                end;
        if flag=false then writeln('Автоматическое оружие не найдено');
        end;
    if ans=5 then
        begin
        k:=1;
        flag:=false;
        for i:=1 to count do
            if guns[i].automatic=false then 
                begin
                printgun(i, k);
                flag:=true;
                k:=k+1;
                end;
        if flag=false then writeln('Неавтоматическое оружие не найдено');
        end;
    end;

begin
with zerogun do
    begin
    nam:='none';
    caliber:=0;
    automatic:=false;
    yearconstruct:=0;
    end;
count:=0;
for i:=1 to n do guns[i]:=zerogun;
writeln('БАЗА ДАННЫХ ОРУЖИЯ');
while true do
    begin
    writeln();
    writeln('Действия, нажмите:');
    writeln(' 1 - загрузить базу данных оружия');
    writeln(' 2 - выгрузить базу данных оружия');
    writeln(' 3 - добавить оружие');
    writeln(' 4 - удалить оружие');
    writeln(' 5 - распечатать весь список оружия');
    writeln(' 6 - поиск оружия по характеристике');
    writeln(' 0 - завершение работы программы');
    writeln('Введите цифру: ');
    readln(action);
    case action of
        '1': f1();
        '2': f2();
        '3': f3();
        '4': f4();
        '5': f5();
        '6': f6();
        '0': exit();
        else writeln('Неверный ввод');
        end;
    end;
end.