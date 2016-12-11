# How to Debug in python
a brief tutorial on how to debug in python.

## Import Debug tools
To debug in python you must first import the *pdb* library in the file you wish to debug.

`import pdb`
## Using Breakpoints
A breakpoint pauses the execution of the program. The developer can insert a breakpoint on anyline of code they wish to pause the program when it reaches that line. To breakpoint in python, we use the command *pdb.set_trace()*

```python
import pdb 
x = 4
pdb.set_trace() #<-- Program will pause when it reaches here
print "This won't print yet!"
```
After reaching the line: `pdb.set_trace()` the program will pause and an interactive python shell will appear. By entering 's' as a command, you can step through the code line by line. There are additional commands and typing 'help' should display all commands. The rest is for you to find out :-)
