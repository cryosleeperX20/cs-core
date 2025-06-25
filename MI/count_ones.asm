; 8085 Program - Count Number of 1's in D Register
; Result (count of 1s) is stored in B register

MVI D, 12H        ; Load D with the number (e.g., 12H = 00010010B)
MOV A, D          ; Copy D to Accumulator for bitwise rotation
MVI C, 08H        ; Set bit counter (8 bits to check)
MVI B, 00H        ; Initialize result register B to 0

LOOP1:
RLC               ; Rotate Accumulator left, MSB → CY
JC LOOP2          ; If carry is set (bit = 1), go to LOOP2
DCR C             ; Decrement bit counter
JNZ LOOP1         ; Repeat if bits remain
HLT               ; Halt after 8 bits checked

LOOP2:
INR B             ; Increment count of 1s
DCR C             ; Decrement bit counter
JNZ LOOP1         ; Repeat if bits remain
HLT
