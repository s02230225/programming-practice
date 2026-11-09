;—хема программы

INCLUDE settings.inc
INCLUDE io2023.inc
 
.STACK 4096

.DATA
FStr DB 'The program starts working.',0         
LStr DB 'The program has ended.',0

      ; переменные


.CODE
start: OUTSTR offset FStr
       NEWLINE

        ; команды
     
       OUTSTR offset LStr
       NEWLINE      
       EXIT
END start
       