;Головной модуль

INCLUDE settings.inc
INCLUDE io2023.inc

EXTRN N:abs, a:dword, T:byte
EXTERN P1@0: PROC

PUBLIC start

.STACK 4096
.DATA 
Frst DB "Hello!",0
Last DB "Bye!",0

.CODE
start: 
     OUTSTR offset Frst
     NEWLINE
     OUTU N
     NEWLINE
     OUTU a
     NEWLINE
     OUTSTR offset T
     NEWLINE
     CALL P1@0
     OUTU a
     NEWLINE
     OUTSTR offset Last
     NEWLINE
    EXIT
end start
