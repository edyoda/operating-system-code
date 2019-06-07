import os 
from time import sleep
  
def process_create(): 
    a = 1
    n = os.fork() 
    print ('Hello')
  
    # n greater than 0  means parent process 
    if n > 0: 
        print("Parent process and id is : ", os.getpid()) 
        while True:
            sleep(5)
            print (a)
  
    # n equals to 0 means child process 
    else: 
        a = 99
        print("Child process and id is : ", os.getpid()) 
        while True:
            pass
          
# Driver code 
process_create() 
