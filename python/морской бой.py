from random import *
#МОРСКОЙ БОЙ

def da(a,b):
    #проверка наличия на поле
    if 0<=a<=9 and 0<=b<=9: return True
    else: return False
    
def f(x,z):
    #создание полей
    y=x
    s=randint(0,1)
    if s==0:
        q=True
        while q:
            b=randint(0,9-z)
            c=randint(0,9)
            qq=[]
            for i in range(z):
                qq.append([b+i,c])
                if da(b+i+1,c):
                    if y[b+i+1][c]=="#": break
                if da(b+i-1,c):
                    if y[b+i-1][c]=="#": break
                if da(b+i,c+1):
                    if y[b+i][c+1]=="#": break
                if da(b+i,c-1):
                    if y[b+i][c-1]=="#": break    
                if da(b+i+1,c+1):
                    if y[b+i+1][c+1]=="#": break
                if da(b+i+1,c-1):
                    if y[b+i+1][c-1]=="#": break
                if da(b+i-1,c+1):
                    if y[b+i-1][c+1]=="#": break
                if da(b+i-1,c-1):
                    if y[b+i-1][c-1]=="#": break
            else: q=False
        for i,j in qq:
            y[i][j]="#"
    else:
        q=True
        b=randint(0,9)
        c=randint(0,9-z)
        qq=[]
        while q:
            b=randint(0,9)
            c=randint(0,9-z)
            qq=[]
            for i in range(z):
                qq.append([b,c+i])
                if da(b+1,c+i):
                    if y[b+1][c+i]=="#": break
                if da(b-1,c+i):
                    if y[b-1][c+i]=="#": break
                if da(b,c+i+1):
                    if y[b][c+i+1]=="#": break
                if da(b,c+i-1):
                    if y[b][c+i-1]=="#": break    
                if da(b+i+1,c+1):
                    if y[b+i+1][c+1]=="#": break
                if da(b+i+1,c-1):
                    if y[b+i+1][c-1]=="#": break
                if da(b+i-1,c+1):
                    if y[b+i-1][c+1]=="#": break
                if da(b+i-1,c-1):
                    if y[b+i-1][c-1]=="#": break
            else: q=False
        for i,j in qq:
            y[i][j]="#"
    return y

def pr():
    #вывод вашего поля и поля вашей стрельбы
    global a,b
    print("  0 1 2 3 4 5 6 7 8 9",' '*6,"  0 1 2 3 4 5 6 7 8 9")
    for j in range(10):
        print(j,*a[j],' '*6,j,*b[j])
    print()
    
def st():
    #вы стреляете по противнику
    global b,с
    print("Вы стреляете, выберете клетку:")
    z=True
    while z:
        x,y=map(int,input().split())
        if not da(x,y):
            print("Неправильный ввод, выберете другую клетку:")
        elif b[x][y]=='*'  or b[x][y]=='o':
            print("Вы уже туда стреляли, выберете другую клетку:")
        else: z=False    
    if c[x][y]=='#':
        print("Попал!")
        b[x][y]='o'
    else:
        print("Мимо")
        b[x][y]='*'

def bt():
    #противник стреляет по вам
    global a,d
    x=randint(0,9)
    y=randint(0,9)
    z=True
    while z:
        x=randint(0,9)
        y=randint(0,9)
        if da(x,y) and not d[x][y]=='*' and not d[x][y]=='o':
            z=False
    if a[x][y]=='#':
        d[x][y]='o'
        a[x][y]='u'
        print("Ваш противник выстрелил и попал!")
    else:
        d[x][y]='*'
        a[x][y]='*'
        print("Ваш противник выстрелил и НЕ попал")
    print()

def wn():
    #проверка на победу/проигрыш
    global a,c
    aa=0
    cc=0
    for i in range(10):
        aa+=a[i].count('#')
    for i in range(10):
        cc+=c[i].count('#')
    if cc==0:
        print("Вы победили!!!")
        return False
    elif aa==0:
        print("Вы проиграли!!!")
        return False
    else: return True
a=[['.']*10 for _ in range(10)] #ваше поле
b=[['.']*10 for _ in range(10)] #поле вашей стрельбы
c=[['.']*10 for _ in range(10)] #поле противника
d=[['.']*10 for _ in range(10)] #поле стрельбы противника
tb=[4,3,3,2,2,2,1,1,1,1]
for i in tb:
    a=f(a,i)
    c=f(c,i)
print(" "*14,"Морской бой!")
print("Сначала вводить столбец, потом строку!")
print("Ваше поле"," "*18,"Поле вашей стрельбы")
pr()
end=True
while end:
    st()
    bt()
    pr()
    end=wn()