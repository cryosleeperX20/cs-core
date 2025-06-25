; 8085 Program - Check if Number is Positive, Negative, or Zero
; The number is stored in register B
; Result is stored in Accumulator A as:
; - 00H → if number is Zero
; - 11H → if number is Positive
; - 22H → if number is Negative

MVI B, 0BH        ; Load number into register B (example: 0BH = +11 decimal)
MOV A, B          ; Copy number from B to Accumulator

CMA               ; Complement Accumulator
INR A             ; A = Two's complement of original value (for CMP)
CPI 00H           ; Compare with 00H
JZ zero           ; If A == 0, it's zero → jump to label 'zero'

ANI 80H           ; Mask sign bit
JZ positive       ; If sign bit is 0 → positive → jump to 'positive'
JNZ negative      ; If sign bit is 1 → negative → jump to 'negative'

zero:    
MVI A, 00H        ; A = 00H → Number is zero
JMP end

positive:    
MVI A, 11H        ; A = 11H → Number is positive
JMP end

negative:    
MVI A, 22H        ; A = 22H → Number is negative

end:
HLT               ; Halt the program
