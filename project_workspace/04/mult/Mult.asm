//Function:
//Multiplication: The inputs of this program are the current values stored in R0 and R1 (i.e. the two top RAM locations). The program computes the product R0*R1 and stores the result in R2.  

//Comments:
//We assume (in this program) that R0>=  0, R1>=  0, and  R0*R1<32768. Your program need not test these conditions, but rather assume that they hold.  The supplied Mult.tst  and Mult.cmp  scripts will test your program on several representative data values.

//Notes (from me):
//You can only assign -1,0,1 directly to M, otherwise you have to load the numebr to A (with @), assign that to the data register (D) , and then load the appropriate register, and assign that value to it. This is a dual function of the A register, both as an address (reference) or data (value), so the same register is accessed with A or D.

//there might be a better way to implement this, but this one works, for now. (though multiplication is a pretty important function)


//starting from scratch.

//Initialization
//Clear register 2 (this is very important, otherwise results are continually added to it.:
@R2
M=0
        
//simple loop
@i
M=1
(LOOP)
//loop header
@i
D=M
@R0
D=D-M
@END
D;JGT
//end loop header
//loop body
@R1
D=M
@R2
M=M+D

//end loop body
//loop footer
//increment i
@i
M=M+1
@LOOP
0;JMP
//end loop footer

//End Program.
(END)
@END
0;JMP

