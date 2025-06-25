; 8085 Program - Add Numbers Using Counter and Memory

; 1. Addition of numbers from 1 to 10 using counter
MVI C, 0AH        ; Initialize counter C with 10
MVI A, 00H        ; Clear Accumulator

LOOP1:
ADD C             ; Add value of C to Accumulator
DCR C             ; Decrement counter
JNZ LOOP1         ; Repeat until C becomes 0
STA 0000H         ; Store result at memory location 0000H

; 2. Addition of any 10 numbers stored in memory starting at 0001H
MVI A, 00H        ; Clear Accumulator
MVI C, 0AH        ; Counter = 10
LXI H, 0001H      ; Point HL to memory start

LOOP2:
ADD M             ; Add memory content to Accumulator
INX H             ; Move to next memory location
DCR C             ; Decrement counter
JNZ LOOP2         ; Repeat until C = 0
STA 000BH         ; Store result at memory location 000BH

; 3. Add 10 hexadecimal bytes and store FFH at 2080H if sum overflows
MVI A, 00H        ; Clear Accumulator
MVI C, 0AH        ; Counter = 10
LXI H, 0001H      ; Point HL to memory start

LOOP3:
ADD M             ; Add memory content to Accumulator
INX H             ; Next memory location
DCR C             ; Decrement counter
JNZ LOOP3         ; Loop until all 10 bytes are added
JC LOOP4          ; If carry (overflow), jump to LOOP4
STA 2080H         ; If no overflow, store result at 2080H
HLT

LOOP4:
MVI A, 0FFH       ; Overflow → load FFH
STA 2080H         ; Store FFH at 2080H

HLT
