# добавление библиотек
import pygame
import random
import time
import sys
import os


# перевод из координат массива в координаты окна
def ksize(xx, yy):
    global wight, height, margin
    xx1 = xx * wight + (xx + 1) * margin
    yy1 = yy * height + (yy + 1) * margin
    return xx1, yy1


# проверка на наличие объекта на пути
def occup(xmove, ymove):
    global array, room, xhero, yhero
    if array[room][2][yhero + ymove][xhero + xmove] == 0:
        return True
    else:
        return False


# проверка на наличие объекта на пути врага
def occup2(xmove, ymove):
    global array, room
    if array[room][2][ymove][xmove] == 0 and array[room][0][ymove][xmove] != 1:
        return True
    else:
        return False

    # атака врагов


def attack(xat, yat, at):
    global array, enarray, room, nncount, nnmax
    num = array[room][2][yat][xat]
    for j in range(len(enarray)):
        if enarray[j][0] == num:
            if enarray[j][2] < at:
                print('нанесено повреждений:', at - enarray[j][2])
            else:
                print('нанесено повреждений:', at)
            enarray[j][2] -= at
            if enarray[j][2] <= 0:
                nncount += enarray[j][4]
                if nncount > nnmax:
                    nncount = nnmax
                enarray.pop(j)
                array[room][2][yat][xat] = 0
                break


# параметры экрана
wk = 15
hk = 15
wight = height = 32
margin = 4
menusize = 300
size = (wk * wight + (wk + 1) * margin + menusize, hk * wight + (hk + 1) * margin)
fps = 5

# создание окна игры
pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("моя игра")
clock = pygame.time.Clock()

# содание цветов
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# импорт графики и звуков
ahero = pygame.image.load("arts/pixil-0.png")
afloor = pygame.image.load("arts/pixil-1.png")
awall = pygame.image.load("arts/pixil-2.png")
adoor = pygame.image.load("arts/pixil-3.png")
ahill = pygame.image.load("arts/pixil-4.png")
aenemy1 = pygame.image.load("arts/pixil-5.png")
textfont = pygame.font.SysFont('arial', height)
textfont1 = pygame.font.SysFont('arial', 2 * height)
pygame.mixer.music.load('sounds/background.mp3')
pygame.mixer.music.set_volume(1)
pygame.mixer.music.play(-1)
sstep = pygame.mixer.Sound("sounds/s1.ogg")
sjerk = pygame.mixer.Sound("sounds/s1.ogg")
shit = pygame.mixer.Sound("sounds/s1.ogg")
sshot = pygame.mixer.Sound("sounds/s1.ogg")
scirc = pygame.mixer.Sound("sounds/s1.ogg")
shill = pygame.mixer.Sound("sounds/s1.ogg")
snewroom = pygame.mixer.Sound("sounds/s1.ogg")
sdamage = pygame.mixer.Sound("sounds/s1.ogg")

# переменные в игре
xhero = 1
yhero = 1

jlength = 3
jprice = 30

athp = 20
circhp = 10

shhp = 10
shlength = 3
shprice = 20

hpmax = 100
hpcount = 80
hpregen = 10

mpmax = 50
mpcount = 50
mpregen = 5

nncount = 50
nnmax = 100

room = 0
roomcount = 10
xdoor = 13
ydoor = 13
xdoornew = 1
ydoornew = 1

hillhp1 = 10
hillat1 = 0
hillnn1 = 20

enhp1 = 30
enat1 = 20
ennn1 = 10

doorscore = 100
hillscore = 100
enscore = 1000

text0 = 'ROOM: '
text1 = 'STRENGHT: '
text2 = 'NANITES: '
text3 = 'CHARGE: '
# создание массивов данных игры
en1array = [1, 1, 1, 1, 2, 2, 2, 3, 3, 3]
en2array = [0, 1, 1, 1, 1, 1, 2, 2, 2, 2]
enarray = []
doors = []
array = [[[[0] * wk for k in range(hk)] for j in range(3)] for i in range(roomcount)]
for k in range(roomcount):
    for i in range(hk):
        for j in range(wk):
            if i == 0 or j == 0 or i == hk - 1 or j == wk - 1:
                array[k][0][i][j] = 1
    if k < roomcount - 1:
        array[k][0][ydoor][xdoor] = doorscore
        doors.append([doorscore, k, xdoor, ydoor, doorscore + 1])
        doorscore += 1
        array[k + 1][0][ydoornew][xdoornew] = doorscore
        doors.append([doorscore, k + 1, xdoornew, ydoornew, doorscore - 1])
        doorscore += 1
    for i in range(en1array[k]):
        while True:
            enx = random.randint(2, wk - 3)
            eny = random.randint(2, hk - 3)
            if array[k][2][eny][enx] == 0:
                array[k][2][eny][enx] = hillscore
                enarray.append([hillscore, k, hillhp1, hillat1, hillnn1])
                hillscore += 1
                break
    for i in range(en2array[k]):
        while True:
            enx = random.randint(4, wk - 3)
            eny = random.randint(4, hk - 3)
            if array[k][2][eny][enx] == 0:
                array[k][2][eny][enx] = enscore
                enarray.append([enscore, k, enhp1, enat1, ennn1])
                enscore += 1
                break
# for i in range(hk):
# print(*array[k][0][i], ' ' * 5, *array[k][1][i], ' ' * 5, *array[k][2][i])
# print()

# в массиве array[комната][слой][у][х]
# 0 слой: текстуры стен, пола, дверей
# 1 слой: текстуры эффектов
# 2 слой: текстуры хила и враги

# в массиве enarray[враг][информация о нём]
# порядковый номер
# комната
# здоровье
# урон
# нанитов за его убийство

# в массиве doors[дверь][информация о ней]
# номер двери
# комната этой двери
# x комнаты
# y комнаты
# номер комнаты в которую ведёт эта дверь

# заставка игры, информация о кнопках управления, отображение первого кадра
flag0 = True
flagscore = 0
screen.fill(pygame.Color("black"))
gstart1 = textfont1.render('SPACE ATTACKERS', True, white, black)
screen.blit(gstart1, (180, 150))
text = 'НАЖМИТЕ "SPACE", ЧТОБЫ НАЧАТЬ'
gstart2 = textfont.render(text, True, white, black)
screen.blit(gstart2, (190, 250))
pygame.display.flip()
while flag0:
    for event in pygame.event.get():
        # выход из игры
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # нажатие клавиш
        elif event.type == pygame.KEYDOWN:
            key = pygame.key.get_pressed()
            # переход
            if key[pygame.K_SPACE]:
                if flagscore == 0:
                    screen.fill(pygame.Color("black"))
                    text4 = '(W,A,S,D) - ПЕРЕДВИЖЕНИЕ'
                    gstart4 = textfont.render(text4, True, white, black)
                    screen.blit(gstart4, (100, 60))
                    text5 = 'SHIFT + (W,A,S,D) - РЫВОК'
                    gstart5 = textfont.render(text5, True, white, black)
                    screen.blit(gstart5, (100, 100))
                    text6 = 'Q + (W,A,S,D) - АТАКА'
                    gstart6 = textfont.render(text6, True, white, black)
                    screen.blit(gstart6, (100, 140))
                    text7 = 'E + (W,A,S,D) - ВЫСТРЕЛ ЛАЗЕРОМ'
                    gstart7 = textfont.render(text7, True, white, black)
                    screen.blit(gstart7, (100, 180))
                    text8 = 'Z - КРУГОВАЯ АТАКА'
                    gstart8 = textfont.render(text8, True, white, black)
                    screen.blit(gstart8, (100, 220))
                    text9 = 'X - ЛЕЧЕНИЕ'
                    gstart9 = textfont.render(text9, True, white, black)
                    screen.blit(gstart9, (100, 260))
                    text10 = 'C - ВЗАИМОДЕЙСТВИЕ'
                    gstart10 = textfont.render(text10, True, white, black)
                    screen.blit(gstart10, (100, 300))
                    text11 = 'SPACE - ПРОПУСК ХОДА'
                    gstart11 = textfont.render(text11, True, white, black)
                    screen.blit(gstart11, (100, 340))
                    flagscore += 1
                    pygame.display.flip()
                elif flagscore == 1:
                    screen.fill(pygame.Color("black"))
                    for i in range(hk):
                        for j in range(wk):
                            x, y = ksize(j, i)
                            if array[room][0][i][j] >= 100:
                                screen.blit(adoor, (x, y))
                            elif array[room][0][i][j] == 1:
                                screen.blit(awall, (x, y))
                            elif array[room][0][i][j] == 0:
                                screen.blit(afloor, (x, y))
                            if 100 <= array[room][2][i][j] < 1000:
                                screen.blit(ahill, (x, y))
                            elif array[room][2][i][j] >= 1000:
                                screen.blit(aenemy1, (x, y))
                    screen.blit(ahero, (ksize(xhero, yhero)))
                    lvmark = textfont.render(text0 + str(room + 1), True, white, black)
                    screen.blit(lvmark, (wk * wight + (wk + 3) * margin, 1 * height + 2 * margin))
                    hpmark = textfont.render(text1 + str(hpcount) + '/' + str(hpmax), True, white, black)
                    screen.blit(hpmark, (wk * wight + (wk + 3) * margin, 2 * height + 3 * margin))
                    nnmark = textfont.render(text2 + str(nncount) + '/' + str(nnmax), True, white, black)
                    screen.blit(nnmark, (wk * wight + (wk + 3) * margin, 3 * height + 4 * margin))
                    mpmark = textfont.render(text3 + str(mpcount) + '/' + str(mpmax), True, white, black)
                    screen.blit(mpmark, (wk * wight + (wk + 3) * margin, 4 * height + 5 * margin))
                    pygame.display.flip()
                    flag0 = False
                    break

# основной цикл игры
while True:
    # цикл ожидания ввода действия
    flag1 = True
    while flag1:
        for event in pygame.event.get():
            # выход из игры
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # нажатие клавиш
            elif event.type == pygame.KEYDOWN:
                key = pygame.key.get_pressed()
                # обычная атака на Q
                if key[pygame.K_q]:
                    if key[pygame.K_w]:
                        attack(xhero, yhero - 1, athp)
                        shit.play()
                        flag1 = False
                        break
                    elif key[pygame.K_s]:
                        attack(xhero, yhero + 1, athp)
                        shit.play()
                        flag1 = False
                        break
                    elif key[pygame.K_a]:
                        attack(xhero - 1, yhero, athp)
                        shit.play()
                        flag1 = False
                        break
                    elif key[pygame.K_d]:
                        attack(xhero + 1, yhero, athp)
                        shit.play()
                        flag1 = False
                        break
                # рывок на SHIFT
                if key[pygame.K_LSHIFT] and mpcount >= jprice:
                    if key[pygame.K_w] and jlength - 1 < yhero and array[room][0][yhero - jlength][xhero] != 1:
                        if occup(0, -jlength):
                            yhero -= jlength
                            mpcount -= jprice + mpregen
                        sjerk.play()
                        flag1 = False
                        break
                    elif key[pygame.K_s] and yhero < hk - jlength and array[room][0][yhero + jlength][xhero] != 1:
                        if occup(0, jlength):
                            yhero += jlength
                            mpcount -= jprice + mpregen
                        sjerk.play()
                        flag1 = False
                        break
                    elif key[pygame.K_a] and jlength - 1 < xhero and array[room][0][yhero][xhero - jlength] != 1:
                        if occup(-jlength, 0):
                            xhero -= jlength
                            mpcount -= jprice + mpregen
                        sjerk.play()
                        flag1 = False
                        break
                    elif key[pygame.K_d] and xhero < hk - jlength and array[room][0][yhero][xhero + jlength] != 1:
                        if occup(jlength, 0):
                            xhero += jlength
                            mpcount -= jprice + mpregen
                        sjerk.play()
                        flag1 = False
                        break
                # выстрел лазером на e
                elif key[pygame.K_e] and mpcount >= shprice:
                    if key[pygame.K_w]:
                        for i in range(1, shlength + 1):
                            attack(xhero, yhero - i, shhp)
                        mpcount -= shprice + mpregen
                        sshot.play()
                        flag1 = False
                        break
                    elif key[pygame.K_s]:
                        for i in range(1, shlength + 1):
                            attack(xhero, yhero + i, shhp)
                        mpcount -= shprice + mpregen
                        sshot.play()
                        flag1 = False
                        break
                    elif key[pygame.K_a]:
                        for i in range(1, shlength + 1):
                            attack(xhero - i, yhero, shhp)
                        mpcount -= jprice + mpregen
                        sshot.play()
                        flag1 = False
                        break
                    elif key[pygame.K_d]:
                        for i in range(1, shlength + 1):
                            attack(xhero + i, yhero, shhp)
                        mpcount -= jprice + mpregen
                        sshot.play()
                        flag1 = False
                        break
                # круговая атака на z
                elif key[pygame.K_z]:
                    attack(xhero - 1, yhero - 1, circhp)
                    attack(xhero - 1, yhero, circhp)
                    attack(xhero - 1, yhero + 1, circhp)
                    attack(xhero, yhero - 1, circhp)
                    attack(xhero, yhero + 1, circhp)
                    attack(xhero + 1, yhero - 1, circhp)
                    attack(xhero + 1, yhero, circhp)
                    attack(xhero + 1, yhero + 1, circhp)
                    scirc.play()
                    flag1 = False
                    break
                # лечение на x
                elif key[pygame.K_x] and nncount >= hpregen and hpcount != hpmax:
                    nncount -= hpregen
                    hpcount += hpregen
                    if hpcount > hpmax:
                        hpcount = hpmax
                    shill.play()
                    flag1 = False
                    break
                # взаимодействие на c
                elif key[pygame.K_c]:
                    if array[room][0][yhero][xhero] >= 100:
                        numdoor = array[room][0][yhero][xhero]
                        flag2 = False
                        for i in range(len(doors)):
                            if doors[i][0] == numdoor:
                                newnumdoor = doors[i][4]
                                for j in range(len(doors)):
                                    if doors[j][0] == newnumdoor:
                                        room = doors[j][1]
                                        xhero = doors[j][2]
                                        yhero = doors[j][3]
                                        flag2 = True
                                        break
                            if flag2:
                                break
                        snewroom.play()
                    flag1 = False
                    break
                # шаг
                elif key[pygame.K_w] and 0 < yhero and array[room][0][yhero - 1][xhero] != 1:
                    if occup(0, -1):
                        yhero -= 1
                    sstep.play()
                    flag1 = False
                    break
                elif key[pygame.K_s] and yhero < hk - 1 and array[room][0][yhero + 1][xhero] != 1:
                    if occup(0, 1):
                        yhero += 1
                    sstep.play()
                    flag1 = False
                    break
                elif key[pygame.K_a] and 0 < xhero and array[room][0][yhero][xhero - 1] != 1:
                    if occup(-1, 0):
                        xhero -= 1
                    sstep.play()
                    flag1 = False
                    break
                elif key[pygame.K_d] and xhero < wk - 1 and array[room][0][yhero][xhero + 1] != 1:
                    if occup(1, 0):
                        xhero += 1
                    sstep.play()
                    flag1 = False
                    break
                # ожидание
                elif key[pygame.K_SPACE]:
                    flag1 = False
                    break
    # вычисление пошаговых действий (добавление маны)
    if mpcount < mpmax:
        mpcount += mpregen
        if mpcount > mpmax:
            mpcount = mpmax

    # кадр после нашего хода
    screen.fill(pygame.Color("black"))
    for i in range(hk):
        for j in range(wk):
            x, y = ksize(j, i)
            if array[room][0][i][j] >= 100:
                screen.blit(adoor, (x, y))
            elif array[room][0][i][j] == 1:
                screen.blit(awall, (x, y))
            elif array[room][0][i][j] == 0:
                screen.blit(afloor, (x, y))
            if 100 <= array[room][2][i][j] < 1000:
                screen.blit(ahill, (x, y))
            elif array[room][2][i][j] >= 1000:
                screen.blit(aenemy1, (x, y))
    screen.blit(ahero, (ksize(xhero, yhero)))
    lvmark = textfont.render(text0 + str(room + 1), True, white, black)
    screen.blit(lvmark, (wk * wight + (wk + 3) * margin, 1 * height + 2 * margin))
    hpmark = textfont.render(text1 + str(hpcount) + '/' + str(hpmax), True, white, black)
    screen.blit(hpmark, (wk * wight + (wk + 3) * margin, 2 * height + 3 * margin))
    nnmark = textfont.render(text2 + str(nncount) + '/' + str(nnmax), True, white, black)
    screen.blit(nnmark, (wk * wight + (wk + 3) * margin, 3 * height + 4 * margin))
    mpmark = textfont.render(text3 + str(mpcount) + '/' + str(mpmax), True, white, black)
    screen.blit(mpmark, (wk * wight + (wk + 3) * margin, 4 * height + 5 * margin))
    pygame.display.flip()
    time.sleep(0.2)

    # выход из цикла при проигрыше
    if hpcount <= 0:
        break

    # ход каждого из врагов в этой комнате
    for k in range(len(enarray)):
        if enarray[k][1] == room:
            flag3 = False
            for ii in range(hk):
                if flag3:
                    break
                for jj in range(wk):
                    if array[room][2][ii][jj] == enarray[k][0] and array[room][2][ii][jj] >= 1000:
                        delx = jj - xhero
                        dely = ii - yhero
                        # если враг рядом с героем,то наносит урон
                        if abs(delx) + abs(dely) == 1:
                            hpcount -= enarray[k][3]
                            print('получено повреждений:', enarray[k][3])
                            sdamage.play()
                            flag3 = True
                            break
                        # шаг врага
                        else:
                            if dely >= 0:
                                dy = -1
                            else:
                                dy = 1
                            if delx >= 0:
                                dx = -1
                            else:
                                dx = 1
                            if abs(dely) >= abs(delx):
                                if occup2(jj, ii + dy):
                                    array[room][2][ii + dy][jj] = array[room][2][ii][jj]
                                    array[room][2][ii][jj] = 0
                                    flag3 = True
                                    break
                                elif occup2(jj + dx, ii):
                                    array[room][2][ii][jj + dx] = array[room][2][ii][jj]
                                    array[room][2][ii][jj] = 0
                                    flag3 = True
                                    break
                                elif occup2(jj - dx, ii):
                                    array[room][2][ii][jj - dx] = array[room][2][ii][jj]
                                    array[room][2][ii][jj] = 0
                                    flag3 = True
                                    break
                                elif occup2(jj, ii - dy):
                                    array[room][2][ii - dy][jj] = array[room][2][ii][jj]
                                    array[room][2][ii][jj] = 0
                                    flag3 = True
                                    break
                            else:
                                if occup2(jj + dx, ii):
                                    array[room][2][ii][jj + dx] = array[room][2][ii][jj]
                                    array[room][2][ii][jj] = 0
                                    flag3 = True
                                    break
                                elif occup2(jj, ii + dy):
                                    array[room][2][ii + dy][jj] = array[room][2][ii][jj]
                                    array[room][2][ii][jj] = 0
                                    flag3 = True
                                    break
                                elif occup2(jj, ii - dy):
                                    array[room][2][ii - dy][jj] = array[room][2][ii][jj]
                                    array[room][2][ii][jj] = 0
                                    flag3 = True
                                    break
                                elif occup2(jj - dx, ii):
                                    array[room][2][ii][jj - dx] = array[room][2][ii][jj]
                                    array[room][2][ii][jj] = 0
                                    flag3 = True
                                    break
                        sstep.play()
                        # новый кадр,если враг совершил действие
                        screen.fill(pygame.Color("black"))
                        for i in range(hk):
                            for j in range(wk):
                                x, y = ksize(j, i)
                                if array[room][0][i][j] >= 100:
                                    screen.blit(adoor, (x, y))
                                elif array[room][0][i][j] == 1:
                                    screen.blit(awall, (x, y))
                                elif array[room][0][i][j] == 0:
                                    screen.blit(afloor, (x, y))
                                if 100 <= array[room][2][i][j] < 1000:
                                    screen.blit(ahill, (x, y))
                                elif array[room][2][i][j] >= 1000:
                                    screen.blit(aenemy1, (x, y))
                        screen.blit(ahero, (ksize(xhero, yhero)))
                        lvmark = textfont.render(text0 + str(room + 1), True, white, black)
                        screen.blit(lvmark, (wk * wight + (wk + 3) * margin, 1 * height + 2 * margin))
                        hpmark = textfont.render(text1 + str(hpcount) + '/' + str(hpmax), True, white, black)
                        screen.blit(hpmark, (wk * wight + (wk + 3) * margin, 2 * height + 3 * margin))
                        nnmark = textfont.render(text2 + str(nncount) + '/' + str(nnmax), True, white, black)
                        screen.blit(nnmark, (wk * wight + (wk + 3) * margin, 3 * height + 4 * margin))
                        mpmark = textfont.render(text3 + str(mpcount) + '/' + str(mpmax), True, white, black)
                        screen.blit(mpmark, (wk * wight + (wk + 3) * margin, 4 * height + 5 * margin))
                        pygame.display.flip()
                        time.sleep(0.2)

# экран при проигрыше
screen.fill(pygame.Color("black"))
gover1 = textfont1.render('GAME OVER', True, white, black)
screen.blit(gover1, (160, 150))
gover2 = textfont.render('НАЖМИТЕ "SPACE", ЧТОБЫ ПЕРЕЙТИ В', True, white, black)
screen.blit(gover2, (200, 250))
gover3 = textfont.render('ВК СООБЩЕСТВО ЭТОЙ ИГРЫ', True, white, black)
screen.blit(gover3, (220, 320))
pygame.display.flip()

# ожидание перехода в сообщество
flag4 = True
while flag4:
    for event in pygame.event.get():
        # выход из игры
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # нажатие клавиш
        elif event.type == pygame.KEYDOWN:
            key = pygame.key.get_pressed()
            # переход
            if key[pygame.K_SPACE]:
                os.system('start ' + '')
                flag4 = False
            elif key[pygame.K_ENTER]:
                flag4 = False

# последний кадр и выход из игры
screen.fill(pygame.Color("black"))
gover1 = textfont1.render('СПАСИБО ЗА ИГРУ!', True, white, black)
screen.blit(gover1, (160, 150))
time.sleep(5)
pygame.quit()
sys.exit()

# протестировать,добавить таблицу в правом нижнем углу о полученном и нанесённом уроне
# нанесено/получено повреждений

# ветвление комнат, генерацию последовательности сложности комнат

# далее сделать "ии" врагов на основе поиска в графе в ширину, добавить это в основной игры цикл, добавить им атаки.
# реализовать это перебором всех врагов в комнате и применение к ним функции

# реализовать босса в последней комнате

# реализовать несколько "сюжетных" картинок

# добавить финальную игру
