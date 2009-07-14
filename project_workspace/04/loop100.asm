//Transcript of fig 4.2 p65

//Initialization:
@i
M=1
@sum
M=0
//loop
(LOOP)
//load i to M
@i
//set d=i
D=M
//load 100 to M
@100
//Set d to i - 100
D=D-A
//load the last instruction (infinite loop)
@END
//Jump to end if D > 0
D;JGT
//load i
@i
//set D=i
D=M
//load sum counter to M
@sum
//set sum counter to sum+i through M
M=D+M
//load i to M
@i
//increment i
M=M+1
//load loop
@LOOP
//branch always
0;JMP
//end
(END)
//load end
@END
//jump here infinitely.
0;JMP