; 8085 Program - 1's and 2's Complement Operations

; a. Find the 1's complement of the number at memory location 2000H
; Store result at B000H

LDA 2000H         ; Load value from 2000H into Accumulator
CMA               ; Take 1's complement
STA B000H         ; Store result at B000H

; b. Find the 2's complement of the number at memory location A000H
; Store result at B001H

LDA A000H         ; Load value from A000H into Accumulator
CMA               ; 1's complement
INR A             ; Add 1 → 2's complement
STA B001H         ; Store result at B001H

; c. Convert 5 bytes from memory starting at 6001H into 2's complement
; Store result starting at 9001H

MVI A, 00H        ; Clear Accumulator
MVI C, 05H        ; Counter for 5 bytes
LXI H, 6001H      ; Source address
LXI D, 9001H      ; Destination address

ALP:
MOV A, M          ; Load byte from source
CMA               ; 1's complement
INR A             ; 2's complement
XCHG              ; HL <-> DE (point to destination)
MOV M, A          ; Store result
XCHG              ; DE <-> HL (restore source)
INX H             ; Next source
INX D             ; Next destination
DCR C             ; Decrement counter
JNZ ALP           ; Repeat for 5 bytes

HLT
