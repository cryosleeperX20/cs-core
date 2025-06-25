; 8085 Program - Find Minimum and Maximum from 2 or 10 Numbers

; 1. Find the minimum of two 8-bit numbers stored at 0001H and 0002H
LXI H, 0001H      ; Point HL to 0001H
MOV A, M          ; Load first number into A
INX H             ; Point to 0002H
MOV B, M          ; Load second number into B
CMP B             ; Compare A with B
JC MIN            ; If A < B, A is minimum
INX H             ; Point to result location (0003H)
MOV M, B          ; Store B as minimum
HLT

MIN:
INX H             ; Point to result location (0003H)
MOV M, A          ; Store A as minimum
HLT

; 2. Find the maximum number from a block of 10 bytes starting at 0004H
LXI H, 0004H      ; Point HL to first data
SUB A             ; Clear Accumulator
MVI C, 0AH        ; Counter = 10
MOV A, M          ; Load first value into A

LOOP1:
INX H             ; Next memory location
CMP M             ; Compare A with current memory
DCR C             ; Decrement counter
JZ STORE          ; If 10 bytes processed, store result
JC LOOP2          ; If current memory > A, jump to LOOP2
JMP LOOP1         ; Else continue

LOOP2:
MOV B, A          ; Backup current max to B
MOV A, M          ; Load new max into A
JMP LOOP1

STORE:
STA 0010H         ; Store max at 0010H
HLT

; 3. Find the minimum number from a block of 10 bytes starting at 0004H
LXI H, 0004H      ; Point HL to first data
SUB A             ; Clear Accumulator
MVI C, 0AH        ; Counter = 10
MOV A, M          ; Load first value into A

LOOP1:
INX H             ; Next memory location
CMP M             ; Compare A with current memory
DCR C             ; Decrement counter
JZ STORE          ; If 10 bytes processed, store result
JNC LOOP2         ; If A >= M, update minimum
JMP LOOP1         ; Else continue

LOOP2:
MOV B, A          ; Backup current min to B
MOV A, M          ; Load new min into A
JMP LOOP1

STORE:
STA 0010H         ; Store min at 0010H
HLT
