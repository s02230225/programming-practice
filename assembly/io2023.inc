.NOLIST

;Панфёров А.А., с небольшими изменениями от Бордаченковой Е.А.


.NOLISTMACRO

; настройки для использования C-библиотеки

includelib msvcrt.lib

COMMENT *
  ----------------------------------
    exit [ i ] ; код возврата
    outstr { r32 | offset S } ; до нулевого байта
    outi { r32 | m32 | i32 }
    outu { r32 | m32 | i32 }
    newline
    outchar { r8 | m8 | i8 }
    inchar { r8 | m8 }
    inint { r32 | m32 }
  ---------------------------------- *

extern _exit: PROC
extern printf: PROC
extern scanf: PROC
extern putchar: PROC
extern getchar: PROC

EXIT    EQU <exit>
OUTSTR  EQU <outstr>
OUTI    EQU <outi>
OUTU    EQU <outu>
NEWLINE EQU <newline>
OUTCHAR EQU <outchar>
INCHAR  EQU <inchar>
ININT   EQU <inint>

exit macro retval:=<0>
    push retval
    call _exit
endm

invoke_printf macro fmt,data
    push eax
    push ecx
    push edx
    push fmt
    push data
    lea eax,[esp+4]
    push eax
    call printf
    add esp, 12
    pop edx
    pop ecx
    pop eax
endm

outstr macro message
    invoke_printf 's%', message
endm

outi macro i32
    invoke_printf 'i%', i32
endm

outu macro u32
    invoke_printf 'u%', u32
endm

newline macro
    outchar 10
endm

outchar macro c
    push eax
    push ecx
    push edx
    mov al, c
    movzx eax, al
    push eax
    call putchar
    add esp, 4
    pop edx
    pop ecx
    pop eax
endm

invoke_scanf macro fmt,dst,typ
    local no_error
  if (.type dst) and 10h ; dst is register
    push eax ; reserve memory (on stack) for result
  endif
    push eax
    push ecx
    push edx
  if (.type dst) and 10h
    lea eax, [esp+12] 
  else
    lea eax, dst
  endif
    push fmt
    mov edx, esp ; edx=offset fmt
    push eax     ; eax=offset dst
    push edx
    call scanf
    add esp, 12  ; clear stack: params(=8) + fmt(=4)
    test eax,eax
    jnz no_error
    ; incorrect input => halt
    int 3
no_error:
    pop edx
    pop ecx
    pop eax
  if (.type dst) and 10h
    mov dst, typ ptr [esp]
    add esp, 4
  endif
endm

inint macro x
    invoke_scanf 'd%',x,dword
endm

inchar macro dst
  if @InStr(1,<[AL][AH][al][ah][Al][Ah][aL][aH]>,<[dst]>) GE 1
    push eax ; reserve memory (on stack) for result
  endif
    push eax
    push ecx
    push edx
    call getchar
    pop edx
    pop ecx
  if @InStr(1,<[AL][AH][al][ah][Al][Ah][aL][aH]>,<[dst]>) GE 1
    mov byte ptr [esp+4], al
    pop eax
    mov dst, byte ptr [esp]
    add esp,4
  else
    mov dst, al
    pop eax
  endif
endm

.LIST
