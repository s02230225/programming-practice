INCLUDE settings.inc
INCLUDE io2023.inc
.STACK 4096
.DATA
ccF dd 0
zzF dd 0
ooF dd 0
ssF dd 0
qwerty db 'cf of sf zf', 0
.CODE
qqq macro
local ccc, Nn
	Nn=0
	PUSHFD
	PUSHFD
	POP EAX
	MOV ECX, 16
	
	for n ,<0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15>
		ROR EAX, 1
		mov edx, 0
		if (n eq 0)
			adc edx, 0
			mov ccF, edx
		ENDIF
		if (n eq 6)
			adc edx, 0
			mov ssF, edx
		ENDIF
		if (n eq 7)
			adc edx, 0
			mov ssF, edx
		ENDIF
		if (n eq 11)
			adc edx, 0
			outi edx
		ENDIF
	endm
	outstr offset qwerty
	newline
	outu ccF
	outu ooF
	outu ssF
	outu zzF
	newline
	popfd
endm


OUTFFF MACRO
	FOR I, <0,6,7,11>
		PUSHFD
		PUSHFD
		POP EAX
		MOV EBX, 0
		ROR EAX, I
		ADC EBX, 0
		OUTI EBX
		POPFD
	ENDM
ENDM
start:
mov Dl, 255
add Dl, 129
qqq
	exit
END start
