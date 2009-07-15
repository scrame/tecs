//Function:
//I/O handling: This program runs an infinite loop that listens to the keyboard input.
//When a key is pressed (any key), the program blackens the screen, i.e. writes "black" in every pixel. 
//When no key is pressed, the screen should be cleared.
      
//Comments:
//You may choose to blacken and clear the screen in any visual order, 
//as long as pressing a key continuously for long enough will result in a fully blackened screen 
//and not pressing any key for long enough will result in a cleared screen. 
//This program has a test script (Fill.tst) but no compare file,
// it should be checked visually by inspecting the simulated screen.

//clear keyboard input.
@KBD
M=0

//give pointer the corner of screen memory
@SCREEN
D=A
@pointer //offset in video memory.
M=D


//main loop:
(LOOP)

@KBD
D=M
@FILL
D;JGT
@CLEAR
0;JMP


//always loop
@LOOP
0;JMP


//screen fill
(FILL)

@pointer
D=M
A=D
M=1

@pointer
D=M
@KBD
D=A-D

@LOOP
D;JLE

@pointer
M=M+1

@LOOP
0;JMP
//end fill


(CLEAR)
@pointer
D=M
A=D
M=0

@pointer
D=M
@SCREEN
D=D-A
@LOOP
D;JLT

@pointer
M=M-1

@LOOP
0;JMP


//End clear
