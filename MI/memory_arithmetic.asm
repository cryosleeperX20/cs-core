; 8085 Program - Memory-Based Arithmetic Operations

; A. Add two bytes stored in memory and store the result in the next memory location
; Data at: 0001H and 0002H
; Result stored at: 0003H

LXI H, 0001H     ; Point HL to memory location 0001H
MOV A, M         ; Load value from 0001H into Accumulator
INX H            ; Increment HL to 0002H
MOV B, M         ; Load value from 0002H into B
ADD B            ; A = A + B
INX H            ; Increment HL to 0003H
MOV M, A         ; Store result (A) at 0003H

; B. Subtract content at 2001H from 2002H and store result at 2003H
; A = [2002H] - [2001H]
; Result stored at: 2003H

LXI H, 2001H     ; Point HL to memory location 2001H
MOV A, M         ; Load value from 2001H into Accumulator
INX H            ; Increment HL to 2002H
MOV B, M         ; Load value from 2002H into B
SUB B            ; A = A - B (i.e., 2001H - 2002H)
INX H            ; Increment HL to 2003H
MOV M, A         ; Store result at 2003H

HLT              ; Halt the program
