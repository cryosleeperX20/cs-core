; 8085 Program - Multiply and Divide Using Repetitive Addition/Subtraction

; a. Multiply the contents of memory location 3040H and 3041H
; Result stored in 3042H (LSB) and 3043H (MSB)
; Method: Repetitive Addition

LXI H, 3041H      ; Point HL to 3041H
MOV B, M          ; Load multiplier into B
LXI H, 3040H      ; Point HL to 3040H
MOV C, M          ; Load multiplicand into C
MVI A, 00H        ; Clear Accumulator
MVI D, 00H        ; D will store high byte if needed

LOOP1:
ADD B             ; A = A + B (accumulate)
JNC SKIP_INR      ; If no carry, skip incrementing D
INR D             ; If carry, increment high byte

SKIP_INR:
DCR C             ; Decrement loop counter
JNZ LOOP1         ; Repeat until multiplicand times

LXI H, 3042H      ; Point to store result
MOV M, A          ; Store LSB
INX H             ; Point to 3043H
MOV M, D          ; Store MSB
HLT

; b. Divide content of B by C and store result in D
; Method: Repetitive Subtraction

MVI B, 09H        ; Dividend
MVI C, 03H        ; Divisor
MOV A, B          ; Copy dividend into A
MVI D, 00H        ; Quotient counter

DIV_LOOP:
SUB C             ; A = A - C
JC DONE           ; If A < C, stop
INR D             ; Increment quotient
JMP DIV_LOOP      ; Repeat

DONE:
HLT
