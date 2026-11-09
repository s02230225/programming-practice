# добавление библиотек
import pygame
import random
import time
import sys


# перевод из координат массива в координаты окна
def ksize(xx, yy, xy):
    global wight, height, margin
    xx1 = xx * wight + (xx + 1) * margin
    yy1 = yy * height + (yy + 1) * margin
    if xy:
        global dxhero, dyhero
        return xx1 + dxhero, yy1 + dyhero
    else:
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


# атака героя
def attack(xat, yat, at):
    global array, enarray, room, nncount, nnmax, bossscore, bosshp
    num = array[room][2][yat][xat]
    for j in range(len(enarray)):
        if enarray[j][0] == num:
            if enarray[j][0] == bossscore:
                bosshp -= at
            if enarray[j][2] < at:
                s = 'нанесено повреждений:' + str(at - enarray[j][2])
                textprint(s)
            else:
                s = 'нанесено повреждений:' + str(at)
                textprint(s)
            enarray[j][2] -= at
            if enarray[j][2] <= 0:
                nncount += enarray[j][4]
                array[room][1][yat][xat] = 2
                if nncount > nnmax:
                    nncount = nnmax
                enarray.pop(j)
                array[room][2][yat][xat] = 0
                break


# перерасчёт маны после нашего хода
def process():
    global status, mpcount, mpregen, mpmax
    status = -1
    if mpcount < mpmax:
        mpcount += mpregen
        if mpcount > mpmax:
            mpcount = mpmax


# обновление текстового окна
def textprint(s):
    global textarray
    textarray.append(s)
    if len(textarray) > 18:
        textarray.pop(0)


# расчёт снятия маны при хардкоре
def uhk():
    global hardcore, mpcount, hardmp1
    if hardcore:
        mpcount -= hardmp1
        if mpcount < 0:
            mpcount = 0


# расчёт восполнения маны при хардкоре
def uhkregen():
    global hardcore, mpcount, mpregen, mpmax
    if hardcore:
        mpcount += 3 * mpregen
        if mpcount > mpmax:
            mpcount = mpmax


# параметры экрана
wk = 15
hk = 15
wight = height = 32
margin = 4
menusize = 300
size = (wk * wight + (wk + 1) * margin + menusize, hk * wight + (hk + 1) * margin)
fps = 30
# создание окна игры
pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("SPACE ATTACKERS")
clock = pygame.time.Clock()
# содание цветов
white = (255, 255, 255)
black = (0, 0, 0)
# импорт графики, звуков и текстов
ahero = pygame.image.load("arts/pixil-0.png")
afloor = pygame.image.load("arts/pixil-1.png")
awall = pygame.image.load("arts/pixil-2.png")
adoor = pygame.image.load("arts/pixil-3.png")
adoorclose = pygame.image.load("arts/pixil-7.png")
ahill1 = pygame.image.load("arts/pixil-4.png")
ahill2 = pygame.image.load("arts/pixil-9.png")
aenemy1 = pygame.image.load("arts/pixil-5.png")
aenemy2 = pygame.image.load("arts/pixil-6.png")
aenemy3 = pygame.image.load("arts/pixil-8.png")
afirefloor = pygame.image.load("arts/pixil-10.png")
ashatter = pygame.image.load("arts/pixil-11.png")
aboss = pygame.image.load("arts/pixil-12.png")
acap = pygame.image.load("arts/pixil-13.png")
ac2 = pygame.image.load("arts/pixil-14.png")
textfont = pygame.font.SysFont('arial', height)
textfont1 = pygame.font.SysFont('arial', 2 * height)
textfont2 = pygame.font.SysFont('arial', (margin + height) // 2)
pygame.mixer.music.load('sounds/background.mp3')
pygame.mixer.music.set_volume(1)
pygame.mixer.music.play(-1)
sstep = pygame.mixer.Sound("sounds/s0.ogg")
sjerk = pygame.mixer.Sound("sounds/s1.ogg")
shit = pygame.mixer.Sound("sounds/s2.ogg")
sshot = pygame.mixer.Sound("sounds/s3.ogg")
scirc = pygame.mixer.Sound("sounds/s4.ogg")
shill = pygame.mixer.Sound("sounds/s5.ogg")
snewroom = pygame.mixer.Sound("sounds/s6.ogg")
sdamage = pygame.mixer.Sound("sounds/s7.ogg")
sslip = pygame.mixer.Sound("sounds/s8.ogg")

# заставка игры
flag0 = True
flagscore = 0
screen.fill(pygame.Color("black"))
gstart1 = textfont1.render('SPACE ATTACKERS', True, white, black)
screen.blit(gstart1, (180, 150))
text = 'НАЖМИТЕ "SPACE", ЧТОБЫ НАЧАТЬ'
gstart2 = textfont.render(text, True, white, black)
screen.blit(gstart2, (190, 250))
pygame.display.flip()
# до начала игры
hardcore = False
while flag0:
    for event in pygame.event.get():
        # выход из игры
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # нажатие клавиш
        elif event.type == pygame.KEYDOWN:
            key = pygame.key.get_pressed()
            # заставки
            if key[pygame.K_SPACE]:
                # информация о управлении
                if flagscore == 0:
                    screen.fill(pygame.Color("black"))
                    text4 = '(W,A,S,D) - ПЕРЕДВИЖЕНИЕ'
                    gstart4 = textfont.render(text4, True, white, black)
                    screen.blit(gstart4, (100, 60))
                    text5 = '1 + (W,A,S,D) - РЫВОК'
                    gstart5 = textfont.render(text5, True, white, black)
                    screen.blit(gstart5, (100, 100))
                    text6 = '2 + (W,A,S,D) - АТАКА'
                    gstart6 = textfont.render(text6, True, white, black)
                    screen.blit(gstart6, (100, 140))
                    text7 = '3 + (W,A,S,D) - ВЫСТРЕЛ ЛАЗЕРОМ'
                    gstart7 = textfont.render(text7, True, white, black)
                    screen.blit(gstart7, (100, 180))
                    text8 = '4 - КРУГОВАЯ АТАКА'
                    gstart8 = textfont.render(text8, True, white, black)
                    screen.blit(gstart8, (100, 220))
                    text9 = 'H - ЛЕЧЕНИЕ'
                    gstart9 = textfont.render(text9, True, white, black)
                    screen.blit(gstart9, (100, 260))
                    text10 = 'E - ВЗАИМОДЕЙСТВИЕ'
                    gstart10 = textfont.render(text10, True, white, black)
                    screen.blit(gstart10, (100, 300))
                    text11 = 'SPACE - ПРОПУСК ХОДА'
                    gstart11 = textfont.render(text11, True, white, black)
                    screen.blit(gstart11, (100, 340))
                    text12 = '0 - ПЕРЕХОД НА ШАГ'
                    gstart12 = textfont.render(text12, True, white, black)
                    screen.blit(gstart12, (100, 380))
                    flagscore += 1
                    pygame.display.flip()
                # выбор уровня сложности
                elif flagscore == 1:
                    screen.fill(pygame.Color("black"))
                    text13 = 'Выберите уровень сложности:'
                    gstart13 = textfont.render(text13, True, white, black)
                    screen.blit(gstart13, (180, 130))
                    text14 = '1 - НОРМАЛЬНО'
                    gstart14 = textfont.render(text14, True, white, black)
                    screen.blit(gstart14, (200, 200))
                    text15 = '2 - "НЕДОСТАТОК ЭНЕРГИИ"'
                    gstart15 = textfont.render(text15, True, white, black)
                    screen.blit(gstart15, (200, 270))
                    flagscore += 1
                    pygame.display.flip()
                    # сюжетная картинка
                elif flagscore == 3:
                    screen.fill(pygame.Color("black"))
                    screen.blit(acap, (0, 340))
                    screen.blit(ac2, (210, 320))
                    pygame.draw.line(screen, white, [206, 340], [206, 580], 3)
                    pygame.draw.line(screen, white, [0, 340], [206, 340], 3)
                    text18 = 'Боец, тебе выдано невероятно важное задание,'
                    gstart18 = textfont.render(text18, True, white, black)
                    screen.blit(gstart18, (200, 70))
                    text19 = 'и выдан новейший костюм BT-7274. Ты должен'
                    gstart19 = textfont.render(text19, True, white, black)
                    screen.blit(gstart19, (202, 105))
                    text20 = 'проникнуть на космическую вражескую базу'
                    gstart20 = textfont.render(text20, True, white, black)
                    screen.blit(gstart20, (204, 140))
                    text20 = 'и захватить её ядро, тогда она перейдёт'
                    gstart20 = textfont.render(text20, True, white, black)
                    screen.blit(gstart20, (208, 175))
                    text21 = 'под наш контроль. Но будь осторожен,'
                    gstart21 = textfont.render(text21, True, white, black)
                    screen.blit(gstart21, (212, 210))
                    text22 = 'базу охроняют роботы и, возможно,'
                    gstart22 = textfont.render(text22, True, white, black)
                    screen.blit(gstart22, (218, 245))
                    text23 = 'кто-то ещё.'
                    gstart23 = textfont.render(text23, True, white, black)
                    screen.blit(gstart23, (228, 280))
                    flagscore += 1
                    pygame.display.flip()
                # переход в игру
                elif flagscore == 4:
                    flag0 = False
                    break
            # подтверждение уровня сложности
            elif flagscore == 2 and key[pygame.K_1]:
                screen.fill(pygame.Color("black"))
                text16 = 'Уровень сложности:'
                gstart16 = textfont.render(text16, True, white, black)
                screen.blit(gstart16, (270, 150))
                text17 = 'НОРМАЛЬНО'
                gstart17 = textfont.render(text17, True, white, black)
                screen.blit(gstart17, (310, 200))
                flagscore += 1
                pygame.display.flip()
            elif flagscore == 2 and key[pygame.K_2]:
                screen.fill(pygame.Color("black"))
                text16 = 'Уровень сложности:'
                gstart16 = textfont.render(text16, True, white, black)
                screen.blit(gstart16, (270, 150))
                text17 = '"НЕДОСТАТОК ЭНЕРГИИ"'
                gstart17 = textfont.render(text17, True, white, black)
                screen.blit(gstart17, (230, 200))
                hardcore = True
                flagscore += 1
                pygame.display.flip()

# внутренние данные
room = 0
level = 0
roomcount = 3
levelcount = 10
xdoor = hk // 2
ydoor = wk // 2
doorscore = 100
# данные врагов
hillscore1 = 10000
hills1 = 10000
hillscore2 = 20000
hills2 = 20000
enscore1 = 30000
ens1 = 30000
enscore2 = 40000
ens2 = 40000
enscore3 = 50000
ens3 = 50000
enk = 0
hillhp1 = 10
hillnn1 = 10
hillhp2 = 40
hillnn21 = 0
hillnn22 = 10
enhp1 = 30
enat1 = 10
ennn1 = 10
enhp2 = 40
enat2 = 15
ennn2 = 10
enhp3 = 40
enat3 = 20
ennn3 = 10
enmn3 = 20
# данные босса
bosshp = 400
bossscore = 100000
bossdamage = 20
bossf = False
bas = 0
bk = 0
bkk = -1
bks = 0
bse = 0
# постоянный текст
xtext = wk * wight + (wk + 3) * margin
text0 = 'ROOM: '
text1 = 'STRENGHT: '
text2 = 'NANITES: '
text3 = 'CHARGE: '
# другое
flag5 = False
tmflag = True
levelmark = 0
status = 0
tm = 0
# создание массивов данных игры
hill1array = [1, 1, 1, 1, 1, 2, 2, 2, 2, 3]
hill2array = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
en1array = [0, 1, 1, 1, 1, 2, 2, 2, 2, 2]
en2array = [0, 0, 0, 1, 1, 1, 1, 1, 2, 2]
en3array = [0, 0, 0, 0, 0, 0, 1, 1, 1, 2]
textarray = []
enarray = []
doors = []
array = [[[[0] * wk for k in range(hk)] for j in range(3)] for i in range(roomcount * levelcount + 1)]
# наполнение комнат
for m in range(levelcount):
    for n in range(roomcount):
        k = m * roomcount + n
        for i in range(hk):
            for j in range(wk):
                if i == 0 or j == 0 or i == hk - 1 or j == wk - 1:
                    array[k][0][i][j] = 1
        if n < roomcount - 1:
            array[k][0][hk - 2][xdoor] = doorscore
            doors.append([doorscore, k, xdoor, hk - 2, doorscore + 1])
            doorscore += 1
            array[k + 1][0][1][xdoor] = doorscore
            doors.append([doorscore, k + 1, xdoor, 1, doorscore - 1])
            doorscore += 1
        for i in range(hill1array[m]):
            while True:
                enx = random.randint(2, wk - 3)
                eny = random.randint(2, hk - 3)
                if array[k][2][eny][enx] == 0:
                    array[k][2][eny][enx] = hills1
                    enarray.append([hills1, k, hillhp1, 0, hillnn1])
                    hills1 += 1
                    break
        for i in range(hill2array[m]):
            while True:
                enx = random.randint(2, wk - 3)
                eny = random.randint(2, hk - 3)
                if array[k][2][eny][enx] == 0:
                    array[k][2][eny][enx] = hills2
                    hn = random.randint(1, 2)
                    if hn == 1:
                        enarray.append([hills2, k, hillhp2, 0, hillnn21])
                    if hn == 2:
                        enarray.append([hills2, k, hillhp2, 0, hillnn22])
                    hills2 += 1
                    break
        for i in range(en1array[m]):
            while True:
                enx = random.randint(4, wk - 3)
                eny = random.randint(4, hk - 3)
                if array[k][2][eny][enx] == 0:
                    array[k][2][eny][enx] = ens1
                    enarray.append([ens1, k, enhp1, enat1, ennn1])
                    ens1 += 1
                    break
        for i in range(en2array[m]):
            while True:
                enx = random.randint(4, wk - 3)
                eny = random.randint(4, hk - 3)
                if array[k][2][eny][enx] == 0:
                    array[k][2][eny][enx] = ens2
                    enarray.append([ens2, k, enhp2, enat2, ennn2])
                    ens2 += 1
                    break
        for i in range(en3array[m]):
            while True:
                enx = random.randint(4, wk - 3)
                eny = random.randint(4, hk - 3)
                if array[k][2][eny][enx] == 0:
                    array[k][2][eny][enx] = ens3
                    enarray.append([ens3, k, enhp3, enat3, ennn3])
                    ens3 += 1
                    break

    if m < levelcount - 1:
        lvldoor = random.randint(0, 2)
        array[m * roomcount + lvldoor][0][ydoor][wk - 2] = doorscore
        doors.append([doorscore, m * roomcount + lvldoor, wk - 2, ydoor, doorscore + 1])
        doorscore += 1
        array[(m + 1) * roomcount + lvldoor][0][ydoor][1] = doorscore
        doors.append([doorscore, (m + 1) * roomcount + lvldoor, 1, ydoor, doorscore - 1])
        doorscore += 1
for i in range(hk):
    for j in range(wk):
        if i == 0 or j == 0 or i == hk - 1 or j == wk - 1:
            array[-1][0][i][j] = 1
array[28][0][ydoor][wk - 2] = doorscore
doors.append([doorscore, 28, wk - 1, ydoor, doorscore + 1])
doorscore += 1
array[30][0][ydoor][1] = doorscore
doors.append([doorscore, 30, 1, ydoor, doorscore - 1])
doorscore += 1
enarray.append([bossscore, 30, bosshp, 0, 100])
array[30][2][wk // 2][hk // 2] = bossscore

# содержание массивов

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

# патроны атак босса
# воспроизводятся в обратном порядке
baarray = [[[[0] * 15 for i in range(15)] for j in range(3)] for k in range(6)]
for i in range(15):
    for j in range(15):
        # первый
        if ((i == 3 and 3 <= j <= 11) or (j == 3 and 3 <= i <= 11)) or (
                (i == 11 and 3 <= j <= 11) or (j == 11 and 3 <= i <= 11)):
            baarray[0][0][i][j] = 1
        elif ((i == 2 and 2 <= j <= 12) or (j == 2 and 2 <= i <= 12)) or (
                (i == 12 and 2 <= j <= 12) or (j == 12 and 2 <= i <= 12)):
            baarray[0][0][i][j] = 1
        elif ((i == 1 and 1 <= j <= 13) or (j == 1 and 1 <= i <= 13)) or (
                (i == 13 and 1 <= j <= 13) or (j == 13 and 1 <= i <= 13)):
            baarray[0][0][i][j] = 1
        if ((i == 5 and 5 <= j <= 9) or (j == 5 and 5 <= i <= 9)) or (
                (i == 9 and 5 <= j <= 9) or (j == 9 and 5 <= i <= 9)):
            baarray[0][1][i][j] = 1
        elif ((i == 3 and 3 <= j <= 11) or (j == 3 and 3 <= i <= 11)) or (
                (i == 11 and 3 <= j <= 11) or (j == 11 and 3 <= i <= 11)):
            baarray[0][1][i][j] = 1
        elif ((i == 1 and 1 <= j <= 13) or (j == 1 and 1 <= i <= 13)) or (
                (i == 13 and 1 <= j <= 13) or (j == 13 and 1 <= i <= 13)):
            baarray[0][1][i][j] = 1
        if ((i == 6 and 6 <= j <= 8) or (j == 6 and 6 <= i <= 8)) or (
                (i == 8 and 6 <= j <= 8) or (j == 8 and 6 <= i <= 8)):
            baarray[0][2][i][j] = 1
        elif ((i == 4 and 4 <= j <= 10) or (j == 4 and 4 <= i <= 10)) or (
                (i == 10 and 4 <= j <= 10) or (j == 10 and 4 <= i <= 10)):
            baarray[0][2][i][j] = 1
        elif ((i == 2 and 2 <= j <= 12) or (j == 2 and 2 <= i <= 12)) or (
                (i == 12 and 2 <= j <= 12) or (j == 12 and 2 <= i <= 12)):
            baarray[0][2][i][j] = 1
        # второй
        baarray[1][0][i][j] = 1
        baarray[1][1][i][j] = 1
        baarray[1][2][i][j] = 1
        if (3 <= i <= 5 and 6 <= j <= 8) or (9 <= i <= 11 and 6 <= j <= 8) or (
                3 <= j <= 5 and 6 <= i <= 8) or (9 <= j <= 11 and 6 <= i <= 8):
            baarray[1][0][i][j] = 0
            baarray[1][1][i][j] = 0
        elif i == 7 and j == 7:
            baarray[1][0][i][j] = 0
            baarray[1][1][i][j] = 0
        if 3 <= i <= 11 and 3 <= j <= 11:
            baarray[1][2][i][j] = 0
        # третий
        if i == 7 and 1 <= j <= 13:
            baarray[2][0][i][j] = 1
            baarray[2][1][i][j] = 1
        if 6 <= i <= 8 and 1 <= j <= 13:
            baarray[2][0][i][j] = 1
        if i == 7 and (1 <= j <= 3 or 11 <= j <= 13):
            baarray[2][2][i][j] = 1
        if i == 7 and j == 7:
            baarray[2][0][i][j] = 0
            baarray[2][1][i][j] = 0
        # четвёртый
        if j == 7 and 1 <= i <= 13:
            baarray[3][0][i][j] = 1
            baarray[3][1][i][j] = 1
        if 6 <= j <= 8 and 1 <= i <= 13:
            baarray[3][0][i][j] = 1
        if j == 7 and (1 <= i <= 3 or 11 <= i <= 13):
            baarray[3][2][i][j] = 1
        if i == 7 and j == 7:
            baarray[3][0][i][j] = 0
            baarray[3][1][i][j] = 0
        # пятый
        if (1 <= i <= 3 and 1 <= j <= 3) or (11 <= i <= 13 and 11 <= j <= 13):
            baarray[4][2][i][j] = 1
        if (1 <= i <= 5 and 1 <= j <= 5) or (9 <= i <= 13 and 9 <= j <= 13):
            baarray[4][1][i][j] = 1
        if (1 <= i <= 7 and 1 <= j <= 7) or (7 <= i <= 13 and 7 <= j <= 13):
            baarray[4][0][i][j] = 1
        if i == 7 and j == 7:
            baarray[4][0][i][j] = 0
        # шестой
        if (11 <= i <= 13 and 1 <= j <= 3) or (1 <= i <= 3 and 11 <= j <= 13):
            baarray[5][2][i][j] = 1
        if (9 <= i <= 13 and 1 <= j <= 5) or (1 <= i <= 5 and 9 <= j <= 13):
            baarray[5][1][i][j] = 1
        if 1 <= j <= 7 <= i <= 13 or 1 <= i <= 7 <= j <= 13:
            baarray[5][0][i][j] = 1
        if i == 7 and j == 7:
            baarray[5][0][i][j] = 0

#######################################################################################################################

# обычный уровень сложности
if not hardcore:
    # переменные в игре
    # данные героя
    xhero = 1
    yhero = 1
    dxhero = 0
    dyhero = 0
    hpmax = 100
    hpcount = 80
    hpregen = 10
    mpmax = 50
    mpcount = 50
    mpregen = 5
    nncount = 50
    nnmax = 100
    jlength = 3
    jprice = 30
    athp = 20
    circhp = 10
    shhp = 10
    shlength = 3
    shprice = 20

    # основной цикл игры
    while True:
        # получение входящих нажатий
        for event in pygame.event.get():
            # выход из игры
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # нажатие клавиш
            elif event.type == pygame.KEYDOWN:
                key = pygame.key.get_pressed()
                # промежуточное нажатие для некоторых действий
                if status != -1:
                    if key[pygame.K_1]:
                        status = 3
                    elif key[pygame.K_2]:
                        status = 1
                    elif key[pygame.K_3]:
                        status = 2
                    elif key[pygame.K_0]:
                        status = 0
                    # шаг
                    elif key[pygame.K_w] and status == 0 and 0 < yhero and array[room][0][yhero - 1][xhero] != 1:
                        if occup(0, -1):
                            yhero -= 1
                        sstep.play()
                        process()
                    elif key[pygame.K_s] and status == 0 and yhero < hk - 1 and array[room][0][yhero + 1][xhero] != 1:
                        if occup(0, 1):
                            yhero += 1
                        sstep.play()
                        process()
                    elif key[pygame.K_a] and status == 0 and 0 < xhero and array[room][0][yhero][xhero - 1] != 1:
                        if occup(-1, 0):
                            xhero -= 1
                        sstep.play()
                        process()
                    elif key[pygame.K_d] and status == 0 and xhero < wk - 1 and array[room][0][yhero][xhero + 1] != 1:
                        if occup(1, 0):
                            xhero += 1
                        sstep.play()
                        process()
                    # атака
                    if status == 1 and key[pygame.K_w]:
                        attack(xhero, yhero - 1, athp)
                        shit.play()
                        process()
                    elif status == 1 and key[pygame.K_s]:
                        attack(xhero, yhero + 1, athp)
                        shit.play()
                        process()
                    elif status == 1 and key[pygame.K_a]:
                        attack(xhero - 1, yhero, athp)
                        shit.play()
                        process()
                    elif status == 1 and key[pygame.K_d]:
                        attack(xhero + 1, yhero, athp)
                        shit.play()
                        process()
                    # выстрел
                    elif status == 2 and key[pygame.K_w] and mpcount >= shprice:
                        for i in range(1, shlength + 1):
                            attack(xhero, yhero - i, shhp)
                        mpcount -= shprice + mpregen
                        sshot.play()
                        process()
                    elif status == 2 and key[pygame.K_s] and mpcount >= shprice:
                        for i in range(1, shlength + 1):
                            attack(xhero, yhero + i, shhp)
                        mpcount -= shprice + mpregen
                        sshot.play()
                        process()
                    elif status == 2 and key[pygame.K_a] and mpcount >= shprice:
                        for i in range(1, shlength + 1):
                            attack(xhero - i, yhero, shhp)
                        mpcount -= shprice + mpregen
                        sshot.play()
                        process()
                    elif status == 2 and key[pygame.K_d] and mpcount >= shprice:
                        for i in range(1, shlength + 1):
                            attack(xhero + i, yhero, shhp)
                        mpcount -= shprice + mpregen
                        sshot.play()
                        process()
                    # рывок
                    elif status == 3 and key[pygame.K_w] and mpcount >= jprice and jlength - 1 < yhero and \
                            array[room][0][yhero - jlength][xhero] != 1:
                        if occup(0, -jlength):
                            yhero -= jlength
                            mpcount -= jprice + mpregen
                        sjerk.play()
                        process()
                    elif status == 3 and key[pygame.K_s] and mpcount >= jprice and yhero < hk - jlength and \
                            array[room][0][yhero + jlength][xhero] != 1:
                        if occup(0, jlength):
                            yhero += jlength
                            mpcount -= jprice + mpregen
                        sjerk.play()
                        process()
                    elif status == 3 and key[pygame.K_a] and mpcount >= jprice and jlength - 1 < xhero and \
                            array[room][0][yhero][xhero - jlength] != 1:
                        if occup(-jlength, 0):
                            xhero -= jlength
                            mpcount -= jprice + mpregen
                        sjerk.play()
                        process()
                    elif status == 3 and key[pygame.K_d] and mpcount >= jprice and xhero < hk - jlength and \
                            array[room][0][yhero][xhero + jlength] != 1:
                        if occup(jlength, 0):
                            xhero += jlength
                            mpcount -= jprice + mpregen
                        sjerk.play()
                        process()
                    # круговая атака
                    elif key[pygame.K_4]:
                        attack(xhero - 1, yhero - 1, circhp)
                        attack(xhero - 1, yhero, circhp)
                        attack(xhero - 1, yhero + 1, circhp)
                        attack(xhero, yhero - 1, circhp)
                        attack(xhero, yhero + 1, circhp)
                        attack(xhero + 1, yhero - 1, circhp)
                        attack(xhero + 1, yhero, circhp)
                        attack(xhero + 1, yhero + 1, circhp)
                        scirc.play()
                        process()
                    # лечение
                    elif key[pygame.K_h] and nncount >= hpregen and hpcount != hpmax:
                        if nncount >= hpregen:
                            nncount -= hpregen
                            hpcount += hpregen
                        else:
                            hpcount += nncount
                            nncount = 0
                        if hpcount > hpmax:
                            hpcount = hpmax
                        shill.play()
                        process()
                    # взаимодействие
                    elif key[pygame.K_e]:
                        if array[room][0][yhero][xhero] >= 100 and enk == 0 and not bossf:
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
                        process()
                    # ожидание
                    elif key[pygame.K_SPACE]:
                        sslip.play()
                        process()

                # действие босса
                if status == -1 and bossf:
                    # получение патрона атаки босса
                    if bkk == -1:
                        while bk == bks:
                            bk = random.randint(0, len(baarray) - 1)
                        bks = bk
                        bkk = len(baarray[bk]) - 1
                    for ii in range(hk):
                        for jj in range(wk):
                            if array[room][1][ii][jj] == 1:
                                if xhero == jj and yhero == ii:
                                    hpcount -= bossdamage
                                    ss = 'получено повреждений:' + str(bossdamage)
                                    textprint(ss)
                                    sdamage.play()
                                array[room][1][ii][jj] = 0
                    for ii in range(hk):
                        for jj in range(wk):
                            if baarray[bk][bkk][ii][jj] == 1:
                                array[room][1][ii][jj] = 1
                    if bse == 11:
                        bse = 0
                        rxy = random.randint(0, 4)
                        if rxy == 0:
                            array[30][2][1][1] = ens1
                            enarray.append([ens1, 30, enhp1, enat1, ennn1])
                            ens1 += 1
                        elif rxy == 1:
                            array[30][2][hk - 2][wk - 2] = ens1
                            enarray.append([ens1, 30, enhp1, enat1, ennn1])
                            ens1 += 1
                        elif rxy == 2:
                            array[30][2][1][wk - 2] = ens1
                            enarray.append([ens1, 30, enhp1, enat1, ennn1])
                            ens1 += 1
                        elif rxy == 3:
                            array[30][2][hk - 2][1] = ens1
                            enarray.append([ens1, 30, enhp1, enat1, ennn1])
                            ens1 += 1
                    bse += 1
                    bkk -= 1
                # действие обычных врагов
                if status == -1:
                    enk = 0
                    for k in range(len(enarray)):
                        if enarray[k][1] == room:
                            flag3 = False
                            for ii in range(hk):
                                for jj in range(wk):
                                    if array[room][2][ii][jj] == enarray[k][0] and 100000 > array[room][2][ii][jj] \
                                            >= 30000:
                                        enk += 1
                                        delx = jj - xhero
                                        dely = ii - yhero
                                        # если враг рядом с героем,то наносит урон
                                        if abs(delx) + abs(dely) == 1:
                                            hpcount -= enarray[k][3]
                                            ss = 'получено повреждений:' + str(enarray[k][3])
                                            textprint(ss)
                                            if enarray[k][0] >= 50000:
                                                mpcount -= enmn3
                                                if mpcount < 0:
                                                    mpcc = mpcount
                                                    mpcount = 0
                                                    ss = 'потеряно энергии:' + str(enmn3 - mpcc)
                                                    textprint(ss)
                                                else:
                                                    ss = 'потеряно энергии:' + str(enmn3)
                                                    textprint(ss)
                                            sdamage.play()
                                        # шаг врага если он далеко
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
                                                elif occup2(jj + dx, ii):
                                                    array[room][2][ii][jj + dx] = array[room][2][ii][jj]
                                                    array[room][2][ii][jj] = 0
                                                elif occup2(jj - dx, ii):
                                                    array[room][2][ii][jj - dx] = array[room][2][ii][jj]
                                                    array[room][2][ii][jj] = 0
                                                elif occup2(jj, ii - dy):
                                                    array[room][2][ii - dy][jj] = array[room][2][ii][jj]
                                                    array[room][2][ii][jj] = 0
                                            else:
                                                if occup2(jj + dx, ii):
                                                    array[room][2][ii][jj + dx] = array[room][2][ii][jj]
                                                    array[room][2][ii][jj] = 0
                                                elif occup2(jj, ii + dy):
                                                    array[room][2][ii + dy][jj] = array[room][2][ii][jj]
                                                    array[room][2][ii][jj] = 0
                                                elif occup2(jj, ii - dy):
                                                    array[room][2][ii - dy][jj] = array[room][2][ii][jj]
                                                    array[room][2][ii][jj] = 0
                                                elif occup2(jj - dx, ii):
                                                    array[room][2][ii][jj - dx] = array[room][2][ii][jj]
                                                    array[room][2][ii][jj] = 0
                                        sstep.play()
                                        # отрисовка кадра, когда враг сделал действие
                                        screen.fill(pygame.Color("black"))
                                        for i in range(hk):
                                            for j in range(wk):
                                                x, y = ksize(j, i, False)
                                                if array[room][0][i][j] >= 100 and enk == 0 and not bossf:
                                                    screen.blit(adoor, (x, y))
                                                else:
                                                    screen.blit(adoorclose, (x, y))
                                                if array[room][0][i][j] == 1:
                                                    screen.blit(awall, (x, y))
                                                elif array[room][0][i][j] == 0:
                                                    screen.blit(afloor, (x, y))
                                                if array[room][1][i][j] == 1:
                                                    screen.blit(afirefloor, (x, y))
                                                elif array[room][1][i][j] == 2:
                                                    screen.blit(ashatter, (x, y))
                                                if hillscore1 <= array[room][2][i][j] < hillscore2:
                                                    screen.blit(ahill1, (x, y))
                                                elif hillscore2 <= array[room][2][i][j] < enscore1:
                                                    screen.blit(ahill2, (x, y))
                                                elif enscore1 <= array[room][2][i][j] < enscore2:
                                                    screen.blit(aenemy1, (x, y))
                                                elif enscore2 <= array[room][2][i][j] < enscore3:
                                                    screen.blit(aenemy2, (x, y))
                                                elif enscore3 <= array[room][2][i][j] < bossscore:
                                                    screen.blit(aenemy3, (x, y))
                                                elif array[room][2][i][j] == bossscore:
                                                    screen.blit(aboss, (x, y))
                                        pygame.draw.line(screen, white, [546, 550], [546, 0], 3)
                                        pygame.draw.line(screen, white, [546, 191], [846, 191], 3)
                                        for tx in range(len(textarray)):
                                            text000 = textarray[-tx - 1]
                                            tmark = textfont2.render(text000, True, white, black)
                                            txx = (wk + 0.25) * wight + (wk + 3) * margin
                                            screen.blit(tmark,
                                                        (txx, (5.25 + 0.5 * tx) * height + (7 + 0.5 * tx) * margin))
                                        screen.blit(ahero, (ksize(xhero, yhero, True)))
                                        level = room // roomcount + 1
                                        text00 = text0 + (str(level) + "-" + str(room % roomcount + 1))
                                        lvmark = textfont.render(text00, True, white, black)
                                        screen.blit(lvmark, (xtext, 1 * height + 2 * margin))
                                        hpmark = textfont.render(text1 + str(hpcount) + '/' + str(hpmax), True, white,
                                                                 black)
                                        screen.blit(hpmark, (xtext, 2 * height + 3 * margin))
                                        nnmark = textfont.render(text2 + str(nncount) + '/' + str(nnmax), True, white,
                                                                 black)
                                        screen.blit(nnmark, (xtext, 3 * height + 4 * margin))
                                        mpmark = textfont.render(text3 + str(mpcount) + '/' + str(mpmax), True, white,
                                                                 black)
                                        screen.blit(mpmark, (xtext, 4 * height + 5 * margin))
                                        pygame.display.flip()
                                        time.sleep(0.15)
                                        flag3 = True
                                        break
                                if flag3:
                                    break
                    status = 0
        # уникальные действия
        tm += 1
        if tm > fps / 1.5:
            tm = 0
            if tmflag:
                tmflag = False
                dyhero = -2
            else:
                tmflag = True
                dyhero = 1
        if hpcount <= 0:
            break
        if bosshp <= 0:
            flag5 = True
        if room == 30:
            bossf = True
        if level == 2 and levelmark == 0:
            textprint("обнаружен новый тип врагов")
            levelmark = 1
        elif level == 4 and levelmark == 1:
            textprint("обнаружен новый тип врагов")
            levelmark = 2
        elif level == 7 and levelmark == 2:
            textprint("обнаружен новый тип врагов")
            levelmark = 3
        elif level == 9 and levelmark == 3:
            textprint("вы чувствуете, что близки")
            levelmark = 4
        elif level == 11 and levelmark == 4:
            textprint("охраняется злобным ИИ")
            textprint("обноружено ядро, но оно")
            levelmark = 5
        if flag5:
            break
        # отрисовка всех кадров, кроме после действия врага
        screen.fill(pygame.Color("black"))
        for i in range(hk):
            for j in range(wk):
                x, y = ksize(j, i, False)
                if array[room][0][i][j] >= 100 and enk == 0 and not bossf:
                    screen.blit(adoor, (x, y))
                else:
                    screen.blit(adoorclose, (x, y))
                if array[room][0][i][j] == 1:
                    screen.blit(awall, (x, y))
                elif array[room][0][i][j] == 0:
                    screen.blit(afloor, (x, y))
                if array[room][1][i][j] == 1:
                    screen.blit(afirefloor, (x, y))
                elif array[room][1][i][j] == 2:
                    screen.blit(ashatter, (x, y))
                if hillscore1 <= array[room][2][i][j] < hillscore2:
                    screen.blit(ahill1, (x, y))
                elif hillscore2 <= array[room][2][i][j] < enscore1:
                    screen.blit(ahill2, (x, y))
                elif enscore1 <= array[room][2][i][j] < enscore2:
                    screen.blit(aenemy1, (x, y))
                elif enscore2 <= array[room][2][i][j] < enscore3:
                    screen.blit(aenemy2, (x, y))
                elif enscore3 <= array[room][2][i][j] < bossscore:
                    screen.blit(aenemy3, (x, y))
                elif array[room][2][i][j] == bossscore:
                    screen.blit(aboss, (x, y))
        pygame.draw.line(screen, white, [546, 550], [546, 0], 3)
        pygame.draw.line(screen, white, [546, 191], [846, 191], 3)
        for tx in range(len(textarray)):
            text000 = textarray[-tx - 1]
            tmark = textfont2.render(text000, True, white, black)
            txx = (wk + 0.25) * wight + (wk + 3) * margin
            screen.blit(tmark, (txx, (5.25 + 0.5 * tx) * height + (7 + 0.5 * tx) * margin))
        screen.blit(ahero, (ksize(xhero, yhero, True)))
        text00 = text0 + (str(room // roomcount + 1) + "-" + str(room % roomcount + 1))
        lvmark = textfont.render(text00, True, white, black)
        screen.blit(lvmark, (xtext, 1 * height + 2 * margin))
        hpmark = textfont.render(text1 + str(hpcount) + '/' + str(hpmax), True, white, black)
        screen.blit(hpmark, (xtext, 2 * height + 3 * margin))
        nnmark = textfont.render(text2 + str(nncount) + '/' + str(nnmax), True, white, black)
        screen.blit(nnmark, (xtext, 3 * height + 4 * margin))
        mpmark = textfont.render(text3 + str(mpcount) + '/' + str(mpmax), True, white, black)
        screen.blit(mpmark, (xtext, 4 * height + 5 * margin))
        pygame.display.flip()
        clock.tick(fps)

#######################################################################################################################

# хардкор
else:
    # переменные в игре
    # данные героя
    xhero = 1
    yhero = 1
    dxhero = 0
    dyhero = 0
    hpmax = 100
    hpcount = 80
    hpregen = 10
    mpmax = 100
    mpcount = 100
    mpregen = 5
    nncount = 50
    nnmax = 100
    jlength = 3
    jprice = 30
    athp = 20
    circhp = 10
    shhp = 10
    shlength = 3
    shprice = 20
    hardmp1 = 10
    # основной цикл игры
    while True:
        # получение входящих нажатий
        for event in pygame.event.get():
            # выход из игры
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # нажатие клавиш
            elif event.type == pygame.KEYDOWN:
                key = pygame.key.get_pressed()
                # промежуточное нажатие для некоторых действий
                if status != -1:
                    if status != -1:
                        if key[pygame.K_1]:
                            status = 3
                        elif key[pygame.K_2]:
                            status = 1
                        elif key[pygame.K_3]:
                            status = 2
                        elif key[pygame.K_0]:
                            status = 0
                        # шаг
                        elif key[pygame.K_w] and status == 0 and 0 < yhero and array[room][0][yhero - 1][xhero] != 1 \
                                and mpcount >= hardmp1:
                            if occup(0, -1):
                                yhero -= 1
                            sstep.play()
                            process()
                            uhk()
                        elif key[pygame.K_s] and status == 0 and yhero < hk - 1 and array[room][0][yhero + 1][
                            xhero] != 1 \
                                and mpcount >= hardmp1:
                            if occup(0, 1):
                                yhero += 1
                            sstep.play()
                            process()
                            uhk()
                        elif key[pygame.K_a] and status == 0 and 0 < xhero and array[room][0][yhero][xhero - 1] != 1 \
                                and mpcount >= hardmp1:
                            if occup(-1, 0):
                                xhero -= 1
                            sstep.play()
                            process()
                            uhk()
                        elif key[pygame.K_d] and status == 0 and xhero < wk - 1 and array[room][0][yhero][
                            xhero + 1] != 1 \
                                and mpcount >= hardmp1:
                            if occup(1, 0):
                                xhero += 1
                            sstep.play()
                            process()
                            uhk()
                        # атака
                        if status == 1 and key[pygame.K_w] and mpcount >= hardmp1:
                            attack(xhero, yhero - 1, athp)
                            shit.play()
                            process()
                            uhk()
                        elif status == 1 and key[pygame.K_s] and mpcount >= hardmp1:
                            attack(xhero, yhero + 1, athp)
                            shit.play()
                            process()
                            uhk()
                        elif status == 1 and key[pygame.K_a] and mpcount >= hardmp1:
                            attack(xhero - 1, yhero, athp)
                            shit.play()
                            process()
                            uhk()
                        elif status == 1 and key[pygame.K_d] and mpcount >= hardmp1:
                            attack(xhero + 1, yhero, athp)
                            shit.play()
                            process()
                            uhk()
                        # выстрел
                        elif status == 2 and key[pygame.K_w] and mpcount >= shprice + hardmp1:
                            for i in range(1, shlength + 1):
                                attack(xhero, yhero - i, shhp)
                            mpcount -= shprice + mpregen
                            sshot.play()
                            process()
                            uhk()
                        elif status == 2 and key[pygame.K_s] and mpcount >= shprice + hardmp1:
                            for i in range(1, shlength + 1):
                                attack(xhero, yhero + i, shhp)
                            mpcount -= shprice + mpregen
                            sshot.play()
                            process()
                            uhk()
                        elif status == 2 and key[pygame.K_a] and mpcount >= shprice + hardmp1:
                            for i in range(1, shlength + 1):
                                attack(xhero - i, yhero, shhp)
                            mpcount -= shprice + mpregen
                            sshot.play()
                            process()
                            uhk()
                        elif status == 2 and key[pygame.K_d] and mpcount >= shprice + hardmp1:
                            for i in range(1, shlength + 1):
                                attack(xhero + i, yhero, shhp)
                            mpcount -= shprice + mpregen
                            sshot.play()
                            process()
                            uhk()
                        # рывок
                        elif status == 3 and key[pygame.K_w] and mpcount >= jprice + hardmp1 and jlength - 1 < yhero \
                                and array[room][0][yhero - jlength][xhero] != 1:
                            if occup(0, -jlength):
                                yhero -= jlength
                                mpcount -= jprice + mpregen
                            sjerk.play()
                            process()
                            uhk()
                        elif status == 3 and key[
                            pygame.K_s] and mpcount >= jprice + hardmp1 and yhero < hk - jlength and \
                                array[room][0][yhero + jlength][xhero] != 1:
                            if occup(0, jlength):
                                yhero += jlength
                                mpcount -= jprice + mpregen
                            sjerk.play()
                            process()
                            uhk()
                        elif status == 3 and key[pygame.K_a] and mpcount >= jprice + hardmp1 and jlength - 1 < xhero \
                                and array[room][0][yhero][xhero - jlength] != 1:
                            if occup(-jlength, 0):
                                xhero -= jlength
                                mpcount -= jprice + mpregen
                            sjerk.play()
                            process()
                            uhk()
                        elif status == 3 and key[pygame.K_d] and mpcount >= jprice and xhero < hk - jlength and \
                                array[room][0][yhero][xhero + jlength] != 1:
                            if occup(jlength, 0):
                                xhero += jlength
                                mpcount -= jprice + mpregen
                            sjerk.play()
                            process()
                            uhk()
                        # круговая атака
                        elif key[pygame.K_4] and mpcount >= hardmp1:
                            attack(xhero - 1, yhero - 1, circhp)
                            attack(xhero - 1, yhero, circhp)
                            attack(xhero - 1, yhero + 1, circhp)
                            attack(xhero, yhero - 1, circhp)
                            attack(xhero, yhero + 1, circhp)
                            attack(xhero + 1, yhero - 1, circhp)
                            attack(xhero + 1, yhero, circhp)
                            attack(xhero + 1, yhero + 1, circhp)
                            scirc.play()
                            process()
                            uhk()
                        # лечение
                        elif key[pygame.K_h] and nncount >= hpregen and hpcount != hpmax:
                            if nncount >= hpregen:
                                nncount -= hpregen
                                hpcount += hpregen
                            else:
                                hpcount += nncount
                                nncount = 0
                            if hpcount > hpmax:
                                hpcount = hpmax
                            shill.play()
                            process()
                        # взаимодействие
                        elif key[pygame.K_e]:
                            if array[room][0][yhero][xhero] >= 100 and enk == 0:
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
                            process()
                        # ожидание
                        elif key[pygame.K_SPACE]:
                            sslip.play()
                            process()
                            uhkregen()

                # действие босса
                if status == -1 and bossf:
                    # получение патрона атаки босса
                    if bkk == -1:
                        while bk == bks:
                            bk = random.randint(0, len(baarray) - 1)
                        bks = bk
                        bkk = len(baarray[bk]) - 1
                    for ii in range(hk):
                        for jj in range(wk):
                            if array[room][1][ii][jj] == 1:
                                if xhero == jj and yhero == ii:
                                    hpcount -= bossdamage
                                    ss = 'получено повреждений:' + str(bossdamage)
                                    textprint(ss)
                                    sdamage.play()
                                array[room][1][ii][jj] = 0
                    for ii in range(hk):
                        for jj in range(wk):
                            if baarray[bk][bkk][ii][jj] == 1:
                                array[room][1][ii][jj] = 1
                    if bse == 11:
                        bse = 0
                        rxy = random.randint(0, 4)
                        if rxy == 0:
                            array[30][2][1][1] = ens1
                            enarray.append([ens1, 30, enhp1, enat1, ennn1])
                            ens1 += 1
                        elif rxy == 1:
                            array[30][2][hk - 2][wk - 2] = ens1
                            enarray.append([ens1, 30, enhp1, enat1, ennn1])
                            ens1 += 1
                        elif rxy == 2:
                            array[30][2][1][wk - 2] = ens1
                            enarray.append([ens1, 30, enhp1, enat1, ennn1])
                            ens1 += 1
                        elif rxy == 3:
                            array[30][2][hk - 2][1] = ens1
                            enarray.append([ens1, 30, enhp1, enat1, ennn1])
                            ens1 += 1
                    bse += 1
                    bkk -= 1
                # действие обычных врагов
                if status == -1:
                    enk = 0
                    for k in range(len(enarray)):
                        if enarray[k][1] == room:
                            flag3 = False
                            for ii in range(hk):
                                for jj in range(wk):
                                    if array[room][2][ii][jj] == enarray[k][0] and 100000 > array[room][2][ii][jj] \
                                            >= 30000:
                                        enk += 1
                                        delx = jj - xhero
                                        dely = ii - yhero
                                        # если враг рядом с героем,то наносит урон
                                        if abs(delx) + abs(dely) == 1:
                                            hpcount -= enarray[k][3]
                                            ss = 'получено повреждений:' + str(enarray[k][3])
                                            textprint(ss)
                                            if enarray[k][0] >= 50000:
                                                mpcount -= enmn3
                                                if mpcount < 0:
                                                    mpcc = mpcount
                                                    mpcount = 0
                                                    ss = 'потеряно энергии:' + str(enmn3 - mpcc)
                                                    textprint(ss)
                                                else:
                                                    ss = 'потеряно энергии:' + str(enmn3)
                                                    textprint(ss)
                                            sdamage.play()
                                        # шаг врага если он далеко
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
                                                elif occup2(jj + dx, ii):
                                                    array[room][2][ii][jj + dx] = array[room][2][ii][jj]
                                                    array[room][2][ii][jj] = 0
                                                elif occup2(jj - dx, ii):
                                                    array[room][2][ii][jj - dx] = array[room][2][ii][jj]
                                                    array[room][2][ii][jj] = 0
                                                elif occup2(jj, ii - dy):
                                                    array[room][2][ii - dy][jj] = array[room][2][ii][jj]
                                                    array[room][2][ii][jj] = 0
                                            else:
                                                if occup2(jj + dx, ii):
                                                    array[room][2][ii][jj + dx] = array[room][2][ii][jj]
                                                    array[room][2][ii][jj] = 0
                                                elif occup2(jj, ii + dy):
                                                    array[room][2][ii + dy][jj] = array[room][2][ii][jj]
                                                    array[room][2][ii][jj] = 0
                                                elif occup2(jj, ii - dy):
                                                    array[room][2][ii - dy][jj] = array[room][2][ii][jj]
                                                    array[room][2][ii][jj] = 0
                                                elif occup2(jj - dx, ii):
                                                    array[room][2][ii][jj - dx] = array[room][2][ii][jj]
                                                    array[room][2][ii][jj] = 0
                                        sstep.play()
                                        # отрисовка кадра, когда враг сделал действие
                                        screen.fill(pygame.Color("black"))
                                        for i in range(hk):
                                            for j in range(wk):
                                                x, y = ksize(j, i, False)
                                                if array[room][0][i][j] >= 100 and enk == 0 and not bossf:
                                                    screen.blit(adoor, (x, y))
                                                else:
                                                    screen.blit(adoorclose, (x, y))
                                                if array[room][0][i][j] == 1:
                                                    screen.blit(awall, (x, y))
                                                elif array[room][0][i][j] == 0:
                                                    screen.blit(afloor, (x, y))
                                                if array[room][1][i][j] == 1:
                                                    screen.blit(afirefloor, (x, y))
                                                elif array[room][1][i][j] == 2:
                                                    screen.blit(ashatter, (x, y))
                                                if hillscore1 <= array[room][2][i][j] < hillscore2:
                                                    screen.blit(ahill1, (x, y))
                                                elif hillscore2 <= array[room][2][i][j] < enscore1:
                                                    screen.blit(ahill2, (x, y))
                                                elif enscore1 <= array[room][2][i][j] < enscore2:
                                                    screen.blit(aenemy1, (x, y))
                                                elif enscore2 <= array[room][2][i][j] < enscore3:
                                                    screen.blit(aenemy2, (x, y))
                                                elif enscore3 <= array[room][2][i][j] < bossscore:
                                                    screen.blit(aenemy3, (x, y))
                                                elif array[room][2][i][j] == bossscore:
                                                    screen.blit(aboss, (x, y))
                                        pygame.draw.line(screen, white, [546, 550], [546, 0], 3)
                                        pygame.draw.line(screen, white, [546, 191], [846, 191], 3)
                                        for tx in range(len(textarray)):
                                            text000 = textarray[-tx - 1]
                                            tmark = textfont2.render(text000, True, white, black)
                                            txx = (wk + 0.25) * wight + (wk + 3) * margin
                                            screen.blit(tmark,
                                                        (txx, (5.25 + 0.5 * tx) * height + (7 + 0.5 * tx) * margin))
                                        screen.blit(ahero, (ksize(xhero, yhero, True)))
                                        level = room // roomcount + 1
                                        text00 = text0 + (str(level) + "-" + str(room % roomcount + 1))
                                        lvmark = textfont.render(text00, True, white, black)
                                        screen.blit(lvmark, (xtext, 1 * height + 2 * margin))
                                        hpmark = textfont.render(text1 + str(hpcount) + '/' + str(hpmax), True, white,
                                                                 black)
                                        screen.blit(hpmark, (xtext, 2 * height + 3 * margin))
                                        nnmark = textfont.render(text2 + str(nncount) + '/' + str(nnmax), True, white,
                                                                 black)
                                        screen.blit(nnmark, (xtext, 3 * height + 4 * margin))
                                        mpmark = textfont.render(text3 + str(mpcount) + '/' + str(mpmax), True, white,
                                                                 black)
                                        screen.blit(mpmark, (xtext, 4 * height + 5 * margin))
                                        pygame.display.flip()
                                        time.sleep(0.15)
                                        flag3 = True
                                        break
                                if flag3:
                                    break
                    status = 0
        # уникальные действия
        tm += 1
        if tm > fps / 1.5:
            tm = 0
            if tmflag:
                tmflag = False
                dyhero = -2
            else:
                tmflag = True
                dyhero = 1
        if hpcount <= 0:
            break
        if bosshp <= 0:
            flag5 = True
        if room == 30:
            bossf = True
        if level == 2 and levelmark == 0:
            textprint("обнаружен новый тип врагов")
            levelmark = 1
        elif level == 4 and levelmark == 1:
            textprint("обнаружен новый тип врагов")
            levelmark = 2
        elif level == 7 and levelmark == 2:
            textprint("обнаружен новый тип врагов")
            levelmark = 3
        elif level == 9 and levelmark == 3:
            textprint("вы чувствуете, что близки")
            levelmark = 4
        elif level == 11 and levelmark == 4:
            textprint("охраняется злобным ИИ")
            textprint("обноружено ядро, но оно")
            levelmark = 5
        if flag5:
            break
        # отрисовка всех кадров, кроме после действия врага
        screen.fill(pygame.Color("black"))
        for i in range(hk):
            for j in range(wk):
                x, y = ksize(j, i, False)
                if array[room][0][i][j] >= 100 and enk == 0 and not bossf:
                    screen.blit(adoor, (x, y))
                else:
                    screen.blit(adoorclose, (x, y))
                if array[room][0][i][j] == 1:
                    screen.blit(awall, (x, y))
                elif array[room][0][i][j] == 0:
                    screen.blit(afloor, (x, y))
                if array[room][1][i][j] == 1:
                    screen.blit(afirefloor, (x, y))
                elif array[room][1][i][j] == 2:
                    screen.blit(ashatter, (x, y))
                if hillscore1 <= array[room][2][i][j] < hillscore2:
                    screen.blit(ahill1, (x, y))
                elif hillscore2 <= array[room][2][i][j] < enscore1:
                    screen.blit(ahill2, (x, y))
                elif enscore1 <= array[room][2][i][j] < enscore2:
                    screen.blit(aenemy1, (x, y))
                elif enscore2 <= array[room][2][i][j] < enscore3:
                    screen.blit(aenemy2, (x, y))
                elif enscore3 <= array[room][2][i][j] < bossscore:
                    screen.blit(aenemy3, (x, y))
                elif array[room][2][i][j] == bossscore:
                    screen.blit(aboss, (x, y))
        pygame.draw.line(screen, white, [546, 550], [546, 0], 3)
        pygame.draw.line(screen, white, [546, 191], [846, 191], 3)
        for tx in range(len(textarray)):
            text000 = textarray[-tx - 1]
            tmark = textfont2.render(text000, True, white, black)
            txx = (wk + 0.25) * wight + (wk + 3) * margin
            screen.blit(tmark, (txx, (5.25 + 0.5 * tx) * height + (7 + 0.5 * tx) * margin))
        screen.blit(ahero, (ksize(xhero, yhero, True)))
        text00 = text0 + (str(room // roomcount + 1) + "-" + str(room % roomcount + 1))
        lvmark = textfont.render(text00, True, white, black)
        screen.blit(lvmark, (xtext, 1 * height + 2 * margin))
        hpmark = textfont.render(text1 + str(hpcount) + '/' + str(hpmax), True, white, black)
        screen.blit(hpmark, (xtext, 2 * height + 3 * margin))
        nnmark = textfont.render(text2 + str(nncount) + '/' + str(nnmax), True, white, black)
        screen.blit(nnmark, (xtext, 3 * height + 4 * margin))
        mpmark = textfont.render(text3 + str(mpcount) + '/' + str(mpmax), True, white, black)
        screen.blit(mpmark, (xtext, 4 * height + 5 * margin))
        pygame.display.flip()
        clock.tick(fps)

#######################################################################################################################

# после завершения игрового процесса
if flag5:
    # экран при выигрыше
    screen.fill(pygame.Color("black"))
    gover1 = textfont1.render('YOU WIN!!!', True, white, black)
    screen.blit(gover1, (240, 150))
    pygame.display.flip()
else:
    # экран при проигрыше
    screen.fill(pygame.Color("black"))
    gover1 = textfont1.render('GAME OVER', True, white, black)
    screen.blit(gover1, (240, 150))
    pygame.display.flip()

# кадры после завершения игры
flag4 = True
flag6 = False
flag7 = False
while flag4:
    for event in pygame.event.get():
        # выход из игры
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # нажатие клавиш
        elif event.type == pygame.KEYDOWN:
            key = pygame.key.get_pressed()
            # отображение информации о завершении игры
            if key[pygame.K_SPACE] and not flag6:
                if flag5 and not hardcore:
                    screen.fill(pygame.Color("black"))
                    gover2 = textfont.render('Вы прошли игру на сложности нормально.', True, white, black)
                    screen.blit(gover2, (140, 150))
                    pygame.display.flip()
                    flag6 = True
                elif not flag5 and not hardcore:
                    screen.fill(pygame.Color("black"))
                    gover2 = textfont.render('Вы НЕ прошли игру на сложности нормально.', True, white, black)
                    screen.blit(gover2, (130, 150))
                    pygame.display.flip()
                    flag6 = True
                elif flag5 and hardcore:
                    screen.fill(pygame.Color("black"))
                    gover2 = textfont.render('Вы прошли игру на сложности "недостаток энергии".', True, white, black)
                    screen.blit(gover2, (120, 150))
                    pygame.display.flip()
                    flag6 = True
                elif not flag5 and hardcore:
                    screen.fill(pygame.Color("black"))
                    gover2 = textfont.render('Вы НЕ прошли игру на сложности "недостаток энергии".', True, white,
                                             black)
                    screen.blit(gover2, (110, 150))
                    pygame.display.flip()
                    flag6 = True
            elif key[pygame.K_SPACE] and flag6:
                screen.fill(pygame.Color("black"))
                gover10 = textfont1.render('СПАСИБО ЗА ИГРУ!', True, white, black)
                screen.blit(gover10, (170, 180))
                pygame.display.flip()
                flag7 = True
            elif key[pygame.K_SPACE] and flag7:
                flag4 = False

# последний кадр и выход из игры
pygame.quit()
sys.exit()
