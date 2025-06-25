; 8085 Program - Arithmetic Operations

; A. Store 80H in the accumulator and add 20H to it

MVI A, 80H       ; Load 80H into Accumulator
ADI 20H          ; Add 20H to Accumulator (A = A + 20H)

; B. Store 80H in the accumulator and 20H in register B, then add both

MVI A, 80H       ; Load 80H into Accumulator
MVI B, 20H       ; Load 20H into Register B
ADD B            ; Add B to Accumulator (A = A + B)

; C. Store 20H in the accumulator and add it to itself

MVI A, 20H       ; Load 20H into Accumulator
ADD A            ; Add Accumulator with itself (A = A + A)

; D. Store 20H in register B, add it with itself, and store the result back in B

MVI B, 20H       ; Load 20H into Register B
MOV A, B         ; Copy B to Accumulator
ADD B            ; Add B to Accumulator (A = A + B)
MOV B, A         ; Store result back into Register B

; E. Store 80H in memory at 0001H and 20H in accumulator,
;    then add the memory value to accumulator and store result at 0002H

MVI A, 80H       ; Load 80H into Accumulator
STA 0001H        ; Store A into memory location 0001H

MVI A, 20H       ; Load 20H into Accumulator
LXI H, 0001H     ; Point HL to memory location 0001H
ADD M            ; Add content of 0001H to Accumulator

LXI H, 0002H     ; Point HL to memory location 0002H
MOV M, A         ; Store result in memory location 0002H

HLT              ; Halt the program
