from time import time
import sys
def make_timer(func):
    def wrapper(*args, **kargs):
        t1 = time()
        ret_val = func(*args, **kargs)
        t2 = time()
        print('Time: ',t2-t1)
        return ret_val
    return wrapper

def count_num(n):
    for i in range(n):
        for j in range(1000):
            #print(j)
            pass

count_num=make_timer(count_num)
count_num(33000)




        
    

    
