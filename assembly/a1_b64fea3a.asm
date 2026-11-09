; Вспомогательный модуль

INCLUDE settings.inc

PUBLIC a, T, N
PUBLIC P1

EXTRN start:near

N = 1

.DATA
a dd 80000000h
T db 'Text from other module.',0
Lbl dd start
.CODE
P1 PROC
   MOV a, 125
   RET
P1 ENDP

end 