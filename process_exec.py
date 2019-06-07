import os 
  
def process_create(): 
    n = os.fork() 
  
    # n greater than 0  means parent process 
    if n > 0: 
        print("Parent process and id is : ", os.getpid()) 
  
    # n equals to 0 means child process 
    else: 
        print("Child process and id is : ", os.getpid()) 
        prog = 'print("The sum of 5 and 10 is", (5+10))'
        exec(prog)
          
# Driver code 
process_create() 
