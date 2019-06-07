from multiprocessing import Process, Lock
from multiprocessing.sharedctypes import Array

def modify(s,d):
    d[1] = 99
    s.value = s.value.upper()

if __name__ == '__main__':
    lock = Lock()

    #shared memory
    s = Array('c', b'hello world', lock=lock)

    #a copy is made
    d = [1,2,3]

    p = Process(target=modify, args=(s,d))
    p.start()
    p.join()

    print(s.value)
    print (d)
