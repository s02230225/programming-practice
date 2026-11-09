;Головной модуль

INCLUDE settings.inc
INCLUDE io2023.inc

EXTERN ABS1@0: PROC

PUBLIC start

.STACK 4096
.DATA 
Frst DB "Hello!",0
Last DB "Bye!",0
   X DD -123
.CODE
start: 
     OUTSTR offset Frst
     NEWLINE

     PUSH offset X
     CALL ABS1@0
     OUTI X
     NEWLINE

     OUTSTR offset Last
     NEWLINE
    EXIT
end start
