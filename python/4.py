import pygame
import sys
import os



def ksize(xx, yy):
    global wight, height, margin
    xx1 = xx * wight + (xx + 1) * margin
    yy1 = yy * height + (yy + 1) * margin
    return xx1, yy1


wk = hk = 15
wight = height = 32
margin = 4
menusize = 256
size = (wk * wight + (wk + 1) * margin + menusize, hk * wight + (hk + 1) * margin)

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("my game")

xhero = 1
yhero = 1
jlength = 2
jlprice = 25
lvcount = 1
hpcount = 100
mpcount = 50
mpregen = 5
nncount = 0
array0 = [[0] * wk for i in range(hk)]
for i in range(hk):
    for j in range(wk):
        if i == 0 or j == 0 or i == hk - 1 or j == wk - 1:
            array0[i][j] = 2
pygame.display.flip()

while True:
    flag1 = True
    while flag1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                key = pygame.key.get_pressed()
                os.system('start ' + 'https://www.youtube.com/watch?v=dQw4w9WgXcQ')
                if key[pygame.K_q]:
                    if key[pygame.K_w]:
                        flag1 = False
                        break
                    elif key[pygame.K_s]:
                        flag1 = False
                        break
                    elif key[pygame.K_a]:
                        flag1 = False
                        break
                    elif key[pygame.K_d]:
                        flag1 = False
                        break

                elif key[pygame.K_e] and mpcount >= jlprice:
                    if key[pygame.K_w]:
                        mpcount -= jlprice + mpregen
                        flag1 = False
                        break
                    elif key[pygame.K_s]:
                        mpcount -= jlprice + mpregen
                        flag1 = False
                        break
                    elif key[pygame.K_a] and jlength < xhero and array0[xhero - 1 - jlength][yhero] != 2:
                        xhero -= 1 + jlength
                        mpcount -= jlprice + mpregen
                        flag1 = False
                        break
                    elif key[pygame.K_d] and xhero < hk - 1 - jlength and array0[xhero + 1 + jlength][yhero] != 2:
                        xhero += 1 + jlength
                        mpcount -= jlprice + mpregen
                        flag1 = False
                        break

                elif key[pygame.K_LSHIFT] and mpcount >= jlprice:
                    if key[pygame.K_w]:
                        mpcount -= jlprice + mpregen
                        flag1 = False
                        break
                    elif key[pygame.K_s]:
                        mpcount -= jlprice + mpregen
                        flag1 = False
                        break
                    elif key[pygame.K_a]:
                        mpcount -= jlprice + mpregen
                        flag1 = False
                        break
                    elif key[pygame.K_d]:
                        mpcount -= jlprice + mpregen
                        flag1 = False
                        break

                elif key[pygame.K_z]:
                    flag1 = False
                    break

                elif key[pygame.K_x]:
                    flag1 = False
                    break

                elif key[pygame.K_w] and 0 < yhero and array0[xhero][yhero - 1] != 2:
                    yhero -= 1
                    flag1 = False
                    break
                elif key[pygame.K_s] and yhero < hk - 1 and array0[xhero][yhero + 1] != 2:
                    yhero += 1
                    flag1 = False
                    break
                elif key[pygame.K_a] and 0 < xhero and array0[xhero - 1][yhero] != 2:
                    xhero -= 1
                    flag1 = False
                    break
                elif key[pygame.K_d] and xhero < wk - 1 and array0[xhero + 1][yhero] != 2:
                    xhero += 1
                    flag1 = False
                    break
                elif key[pygame.K_SPACE]:
                    flag1 = False
                    break
                elif key[pygame.K_c]:
                    flag1 = False
                    break
    if mpcount < 50:
        mpcount = mpcount + mpregen
    screen.fill(pygame.Color("black"))
    pygame.display.flip()