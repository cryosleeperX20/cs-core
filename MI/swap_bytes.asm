; 8085 Program to Swap Two Bytes Stored in Memory
; Demonstrating 4 different methods

; Method 1: Using LXI and MOV Instructions
; 20H is at memory location 0000H
; ABH is at memory location 0001H

LXI H, 0001H     ; Point HL to 0001H
MOV A, M         ; Load ABH from 0001H into A
LXI H, 0000H     ; Point HL to 0000H
MOV B, M         ; Load 20H from 0000H into B
MOV M, A         ; Store ABH at 0000H
LXI H, 0001H     ; Point HL to 0001H
MOV M, B         ; Store 20H at 0001H

; Method 2: Using LDAX and STAX Instructions
; 20H is at memory location 0003H
; ABH is at memory location 0004H

LXI H, 0003H     ; Point HL to 0003H
MOV D, M         ; Copy 20H to D
LXI B, 0004H     ; Point BC to 0004H
LDAX B           ; Load ABH into A from memory[BC]
MOV M, A         ; Store ABH at 0003H
MOV A, D         ; Move 20H to A
STAX B           ; Store 20H into 0004H

; Method 3: Using LDA and STA Instructions
; 20H is at memory location 0005H
; ABH is at memory location 0006H

LDA 0005H        ; Load 20H from 0005H into A
MOV B, A         ; Copy A to B
LDA 0006H        ; Load ABH from 0006H into A
MOV D, A         ; Copy A to D
MOV A, B         ; Load 20H back into A
STA 0006H        ; Store 20H at 0006H
MOV A, D         ; Load ABH into A
STA 0005H        ; Store ABH at 0005H

; Method 4: Using XCHG Instruction
; 20H is at memory location 0007H
; ABH is at memory location 0008H

LXI H, 0007H     ; Point HL to 0007H
LXI D, 0008H     ; Point DE to 0008H
MOV A, M         ; Load 20H from 0007H into A
XCHG             ; Exchange HL and DE
MOV B, M         ; Load ABH from 0008H into B
MOV M, A         ; Store 20H at 0008H
XCHG             ; Exchange HL and DE again
MOV M, B         ; Store ABH at 0007H

HLT              ; Halt the program
