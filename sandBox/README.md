# How to Debug in python
a brief tutorial on how to debug in python.

## Import Debug tools
To debug in python you must first import the *pdb* library in the file you wwish to debug.
`import pdb`
## Using Breakpoints
A breakpoint pauses the execution of the program. The developer can insert a breakpoint on anyline of code they wish to pause the program when it reaches that line. To breakpoint in python, we use the command *pdb.set_trace()*
ff
`import pdb

x = 4`

