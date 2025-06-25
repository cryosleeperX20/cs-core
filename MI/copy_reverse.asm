; 8085 Program - Copy and Reverse Copy a Block of Data

; a. Copy 10 bytes from memory starting at 2050H to 3050H

LXI H, 2050H      ; Source start address
LXI D, 3050H      ; Destination start address
MVI C, 0AH        ; Counter = 10

COPY_LOOP:
MOV A, M          ; Load byte from source
XCHG              ; Swap HL <-> DE to point to destination
MOV M, A          ; Store byte at destination
INX H             ; Move destination pointer
XCHG              ; Restore source pointer to HL
INX H             ; Move to next source byte
DCR C             ; Decrement counter
JNZ COPY_LOOP     ; Repeat until all 10 bytes are copied

HLT


; b. Reverse copy 6 bytes from XX55H–XX5AH to XX80H–XX85H

LXI H, 2255H      ; Source start address
LXI D, 2285H      ; Destination end address (for reverse copy)
MVI C, 06H        ; Counter = 6

REV_LOOP:
MOV A, M          ; Load byte from source
XCHG              ; HL <-> DE (destination)
MOV M, A          ; Store byte in destination
XCHG              ; Restore HL (source)
DCX D             ; Move destination backward
INX H             ; Move source forward
DCR C             ; Decrement counter
JNZ REV_LOOP      ; Repeat until 6 bytes copied

HLT
