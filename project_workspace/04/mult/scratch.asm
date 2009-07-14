//starting from scratch.

//first, set register 0 to 12.

@12
D=A
@R0
M=D

//now lets set r1 to 10
@10
D=A
@R1
M=D

//ok. lets clear r2 (result) -- expect to see this copied.
@0
D=A
@R2
M=D

//Now lets try setting r2 = r0 + r1
@R0
D=M
@R1
D=D+M
@R2
M=D


//ok. lets clear r2 (result) -- expect to see this copied.
@0
D=A
@R2
M=D



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

