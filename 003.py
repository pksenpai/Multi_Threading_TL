""" current_thread & enumerate """
from time import sleep, perf_counter
from threading import Thread, current_thread, enumerate


"""\_____[current_thread & enumerate]_____/"""  
start = perf_counter()

def show(name):
    print(f'Start {name}!')
    
    # show all alive threads
    print(enumerate())
    
    # thread1 & thread2 repr
    print(current_thread()) 

    # thread1 & thread2 _name
    # print(current_thread().getName())
    
    # thread1 & thread2 id
    # print(current_thread().ident)
        
    sleep(3)
    print(f'End {name}!')

""" object create """
# Tip: you can chage the self._name of Thread class with name param!
t1 = Thread(target=show, args=('One',), name='First')
t2 = Thread(target=show, args=('Two',), name='Second')

""" start threading """
t1.start()
t2.start()
print(current_thread()) # MainThread

""" wait to finish thread """
t1.join()
t2.join()

end = perf_counter()
print(f"{round(end - start)}s")
