'''
-Race condition:
    It is an interference between the work of threads 
    and it happens when two or more threads work 
    on the same resource shard.(You need to run 
    the code several times to see the result)
    
-Thread safe:
    It is true that the probability of this problem happening is low,
    but this problem can be prevented by using thread Safe,
    which means you have to define the Treads in such a way 
    that they respect each other's activity. 
    Subsequent threads must wait until 
    the previous thread has completed its work.
    so we can use Lock :)
    
-Dead lock:
    When we lock the program twice in a row without releasing it,
    the program is blocked and deadlock occurs.
    for example use lock.acquire() then use lock.acquire() again
    without use lock.release() after first lock, deadlock will happens!
    
    -recommend use context manager.

-Atomic:
    An atomic action is one that effectively happens all at once.
    An atomic action cannot stop in the middle: it either happens completely,
    or it doesn't happen at all. No side effects of an atomic action are visible 
    until the action is complete.
    
    -Tip: thread safe is an atomic action!
'''
"""\_____[Lock]_____/"""
from threading import Thread, Lock


num = 0
lock = Lock() # tread safe with Lock

def add():
    global num
    lock.acquire() # lock
    if lock.locked():
        print('locked!<0>')

    for _ in range(100000):
        num += 1

    lock.release() # unlock
    if not lock.locked():
        print('unlocked!>-<')

    
def subtract():
    global num
    lock.acquire() # lock
    if lock.locked():
        print('locked!<0>')

    for _ in range(100000):
        num -= 1

    lock.release() # unlock
    if not lock.locked():
        print('unlocked!>-<')

t1 = Thread(target=add)
t2 = Thread(target=subtract)

t1.start()
t2.start()

t1.join()
t2.join()

print(num)
print('Done!')

"""\_____[Lock but use context manager]_____/"""

def add():
    global num
    with lock:
        for _ in range(100000):
            num += 1

def subtract():
    global num
    with lock:
        for _ in range(100000):
            num -= 1

t1 = Thread(target=add)
t2 = Thread(target=subtract)

t1.start()
t2.start()

t1.join()
t2.join()

print(num)
print('Done!')
