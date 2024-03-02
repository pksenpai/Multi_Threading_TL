from time import sleep, perf_counter
from threading import Thread


"""\_____[Orginal]_____/"""
start = perf_counter()

def show(name):
    print(f"Start {name}")
    sleep(3)
    print(f"End {name}")

show('One')
show('Two')

end = perf_counter()
print(f"{round(end - start)}s") # 6 sec


"""\_____[way01]_____/"""  
start = perf_counter()

def show(name):
    print(f'Start {name}')
    sleep(3)
    print(f'End {name}')

t1 = Thread(target=show, args=('One',))
t2 = Thread(target=show, args=('Two',))

""" start threading """
t1.start()
t2.start()

""" wait to finish thread """
t1.join()
t2.join()


end = perf_counter()
print(f"{round(end - start)}s") # 3 sec


"""\_____[way02]_____/""" 
