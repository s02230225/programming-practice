import random
import time
print("Игра в шарики")
a,b=10,10
c=int(random.uniform(0,2))
if c==0: print("Вы ходите первым!")
else: print("Ваш противник ходит первым!")
while a!=0 and b!=0:
    if c==0:
        time.sleep(0.8)
        print("Ваш ход, загадайте количество шариков от 1 до стольки, сколько есть у вас")
        d=int(input())
        while not 1<=d<=a:
            print("Ваше число не подходит, повторите ввод")
            d=int(input())
        time.sleep(0.2)
        print("Ваш противние пытается угадать, сколько у вас шариков")
        if b>6: e=int(random.uniform(1,b//2+1))
        else: e=int(random.uniform(1,b+1))
        f=int(random.uniform(0,3))
        time.sleep(0.8)
        if d%2==f:
            a-=e
            b+=e
            if a<0: a=0
            print("Ваш противник угадал, теперь количество ваших очков составляет",a)
        else:
            a+=e
            b-=e
            print("Ваш противник не угадал, теперь количество ваших очков составляет",a)
        c=1
    else:
        time.sleep(0.8)
        e=int(random.uniform(1,b+1))
        print("Ход вашего противника, загадайте количество шаров, сколько хотите выиграть и готовы потерять при поражении")
        f=int(input())
        while not 1<=f<=a:
            print("Ваше число не подходит, повторите ввод")
            f=int(input())
        time.sleep(0.2)
        print("Теперь попробуйте угадать, чётное или нечётное число загадал противник, 0 - чётное, 1 - нечётное")
        d=int(input())
        while not 0<=d<=1:
            print("Ваше число не подходит, повторите ввод")
            d=int(input())
        time.sleep(0.2)
        if e%2==d:
            a+=f
            b-=f
            print("Вы угадали, теперь количество ваших очков составляет",a)
        else:
            a-=f
            b+=f
            if a<=0: a=0
            print("Вы не угадали, теперь количество ваших очков составляет",a)
        c=0
    if a<=0:
        print("Вы проиграли!")
        break
    elif b<=0:
        print("Вы победили!")
        break