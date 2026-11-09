.NOLIST
    ;Настройки
.NOLISTMACRO

.586
.model flat,stdcall        

 c_msvcrt typedef PROTO C :VARARG   ;для вызова функций из msvcrt.dll

 option casemap:none
 option NoKeyWord: <c str>          ;не служебные имена
 option NoScoped                    ;метки не локализуются в процедурах
 option proc:private                ;процедуры не общедоступные по умолчанию  
.LIST