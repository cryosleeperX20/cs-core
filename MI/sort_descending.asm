; 8085 Program - Sort Marks of 10 Students in Descending Order
; Data: [63H, 41H, 56H, 62H, 48H, 5AH, 4FH, 4CH, 56H, 56H]
; Sorting Method: Bubble Sort (Descending Order)

START:
LXI H, 0000H      ; HL points to the memory location storing number of values
MVI D, 00H        ; Clear swap flag (D)
MOV C, M          ; Load number of values into C
DCR C             ; Since comparisons = N - 1
INX H             ; Point HL to first data element

LOOP1:
MOV A, M          ; Load current value into A
INX H             ; Move to next element
CMP M             ; Compare A with next memory value
JC LOOP2          ; If next > current, no swap
JZ LOOP2          ; If equal, no swap

MOV B, M          ; Swap required → store next value in B
MOV M, A          ; Replace next value with current
DCX H             ; Move back to current
MOV M, B          ; Store next value in current
INX H             ; Move HL to next comparison start
MVI D, 01H        ; Set swap flag

LOOP2:
DCR C             ; Decrease count
JNZ LOOP1         ; Repeat inner loop
MOV A, D          ; Check if any swaps happened
CPI 01H
JZ START          ; If swaps happened, repeat outer loop

HLT               ; Halt when sorted
