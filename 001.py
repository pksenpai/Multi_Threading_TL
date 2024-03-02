from time import sleep, perf_counter
from threading import Thread


"""\_____[Orginal]_____/"""
print('without treading:')
start = perf_counter()

def show(name):
    print(f"Start {name}")
    sleep(3)
    print(f"End {name}")

""" call func """
show('One')
show('Two')

end = perf_counter()
print(f"{round(end - start)}s") # 6s


"""\_____[way01]_____/"""  
print('orginal instance way:')
start = perf_counter()

def show(name):
    print(f'Start {name}')
    sleep(3)
    print(f'End {name}')

""" object create """
t1 = Thread(target=show, args=('One',))
t2 = Thread(target=show, args=('Two',))

""" start threading """
t1.start()
t2.start()

""" wait to finish thread """
t1.join()
t2.join()


end = perf_counter()
print(f"{round(end - start)}s") # 3s


"""\_____[way02]_____/""" 
print('Override class Way:')
start = perf_counter()

def show(name, delay):
    print(f'Start {name}')
    sleep(delay)
    print(f'End {name}')

class MyThread(Thread): # inherited from Thread
    def __init__(self, name, delay):
        super().__init__()
        self.name = name
        self.delay = delay
    
    def run(self):
        show(self.name, self.delay)

""" object create """
t1 = MyThread('One', 3)
t2 = MyThread('Two', 5)
# Tip: The process takes as long with longest delay thread!
# For example, here it takes 5 seconds! coollll:p

""" start threading """
t1.start()
t2.start()

""" wait to finish thread """
t1.join()
t2.join()


end = perf_counter()
print(f"{round(end - start)}s") # 5s
