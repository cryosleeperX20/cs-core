; 8085 Program - Store and Swap Operations

; Task 1: Store the data byte 32H into memory location 2000H

MVI A, 32H       ; Load 32H into Accumulator
STA 2000H        ; Store contents of Accumulator into memory location 2000H

; Task 2: Swap values of registers B and H
; Initially, B = 10H and H = BCH

MVI B, 10H       ; Load 10H into register B
MVI H, 0BCH      ; Load BCH into register H
MOV C, B         ; Temporarily store B into C
MOV B, H         ; Copy H into B
MOV H, C         ; Copy original B from C into H

HLT              ; Halt the program
