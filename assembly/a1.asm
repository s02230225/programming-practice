INCLUDE settings.inc
INCLUDE io2023.inc
.STACK 4096
.DATA
n equ 3
m equ 4
mat dd 0,1,2,3, 3,4,5,6, 6,7,8,9
.CODE
start:  mov ebx, 0
		mov ecx, 0
fori:   outi mat[ebx][ecx]
		add ecx, 4
		cmp ecx, m*4
		jl fori
		newline
		mov ecx, 0
		add ebx, m*4
		cmp ebx, n*m*4
		jl fori
		newline
		exit
END start
       
