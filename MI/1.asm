
; Question 1 

; Store the data byte 32H into memory location 2000H.

	MVI A , 32H ; Load the data in Accumulator 
	STA 2000H; Store the Value in Accumulator at 2000H

; 10H is stored in register B and BCH is stored in register H. Swap the values of B and H Register.
	MVI B , 10H; Store 10H in B Register
	MVI H , 0BCH; Store BCH in  H Register
	MOV C , B ; Store B in C Temporarily
	MOV B , H ; H --> B 
	MOV H , C ; C --> H
	HLT ; Halt the Program
	
