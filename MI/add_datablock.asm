; 8085 Program - Add a Set of Current Readings from Memory
; Data starts at XX50H and ends with 00H
; Result (16-bit sum) is stored at XX70H (LSB) and XX71H (MSB)

LXI H, 0050H      ; Point HL to starting address (e.g., XX50H)
MVI B, 00H        ; Lower byte of sum (LSB)
MVI C, 00H        ; Higher byte of sum (MSB)

LOOP1:
MOV A, M          ; Load current reading into A
CPI 00H           ; Check for end marker (00H)
JZ STORE          ; If end of data, jump to STORE

ADD B             ; Add A to B (B = B + A)
JNC SKIP_CARRY    ; If no carry, skip incrementing C
INR C             ; If carry from B, increment higher byte

SKIP_CARRY:
MOV B, A          ; Store result back to B
INX H             ; Move to next memory location
JMP LOOP1         ; Repeat

STORE:
LXI H, 0070H      ; Point HL to XX70H
MOV M, B          ; Store LSB at XX70H
INX H             ; Point to XX71H
MOV M, C          ; Store MSB at XX71H

HLT
