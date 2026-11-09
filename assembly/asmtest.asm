INCLUDE settings.inc
INCLUDE io2023.inc
.STACK 4096
.DATA
x dd 0
.CODE
tts:
	outi eax
	newline
	exit
START:
	lea eax, x
	mov dword ptr [eax], tts
	jmp dword ptr [eax]
	


END START
