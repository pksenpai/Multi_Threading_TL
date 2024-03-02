""" Daemon thread """ 
from time import sleep, perf_counter
from threading import Thread
import sys


"""\_____[way01]_____/"""  
start = perf_counter()

def show(name):
    print(f'Start {name}!')
    sleep(3)
    print(f'End {name}!')

""" object create """
# Change the daemon to True and see what happens
t1 = Thread(target=show, args=('One',), daemon=False)
t2 = Thread(target=show, args=('Two',), daemon=False)
# Tip: daemon is False by default!
# Tip: if you wanna use daemon you have to use this before start()!

""" start threading """
t1.start()
t2.start()

""" check daemonization """
print(t1.isDaemon)
print(t2.isDaemon)

""" wait to finish thread """
# commented for test daemon
# t1.join()
# t2.join()

end = perf_counter()
print(f"{round(end - start)}s")

sys.exit()
# Tip: If the daemon param is false -> exit() waits for the end of all threads
print('exited? No!')


"""\_____[way02]_____/"""
# Comment way01 to see test way02 :3
start = perf_counter()

def show(name):
    print(f'Start {name}!')
    sleep(3)
    print(f'End {name}!')

""" object create """
t1 = Thread(target=show, args=('One',))
t2 = Thread(target=show, args=('Two',))
# Tip: daemon is False by default!

""" daemon setter """
# Change the daemon to True and see what happens
t1.setDaemon(False)
t1.setDaemon(False)
# Tip: if you wanna use daemon you have to use this before start()!

""" start threading """
t1.start()
t2.start()

""" check daemonization """
print(t1.isDaemon)
print(t2.isDaemon)

""" wait to finish thread """
# commented for test daemon
# t1.join()
# t2.join()

end = perf_counter()
print(f"{round(end - start)}s")

sys.exit()
# Tip: If the daemon param is false -> exit() waits for the end of all threads
print('exited? No!')
