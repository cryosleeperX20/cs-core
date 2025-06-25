; 8085 Program - Calculate Sum of Odd Numbers and Count Even Numbers
; From a block of 10 data bytes starting at memory location 0001H
; Stores:
; - Count of even numbers at end of data block
; - Sum of odd numbers at the next location

LXI H, 0001H      ; Point to first data byte
MVI C, 0AH        ; Counter = 10 bytes
MVI B, 00H        ; Register B = Even count
MVI D, 00H        ; Register D = Sum of odd numbers

LOOP:
MOV A, M          ; Load current byte into A
ANI 01H           ; Mask LSB to check for odd/even
JZ EVEN           ; If result is 0 → EVEN → jump

; ODD number
MOV A, D          ; Load current odd sum into A
ADD M             ; Add current value to sum
MOV D, A          ; Update sum
INX H             ; Next data byte
DCR C             ; Decrement counter
JNZ LOOP          ; Repeat if not finished
JMP SAVE

EVEN:
INR B             ; Increment even number count
INX H             ; Next data byte
DCR C             ; Decrement counter
JNZ LOOP          ; Repeat if not finished

SAVE:
INX H             ; Move to next location (after 10 bytes)
MOV M, B          ; Store even count
INX H
MOV M, D          ; Store sum of odd numbers

HLT
