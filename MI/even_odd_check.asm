; 8085 Program - Check Even or Odd Number
; The number is stored in register B
; If number is even → Accumulator (A) = 00H
; If number is odd  → Accumulator (A) = 01H

MVI B, 0DAH      ; Load the number (DAH = 218 decimal) into register B
MOV A, B         ; Copy B into Accumulator A
ANI 01H          ; Perform bitwise AND with 01H (check least significant bit)
                 ; Result: 
                 ; - If LSB is 0 → number is even → A = 00H
                 ; - If LSB is 1 → number is odd  → A = 01H

HLT              ; Halt the program
