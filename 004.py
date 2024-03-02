from time import sleep
# from threading import Thread
from concurrent.futures import ThreadPoolExecutor


def show(name):
    print(f'Start {name}!')
    sleep(3)
    print(f'End {name}!')

with ThreadPoolExecutor(max_workers=2) as exc:
    names = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven']
    exc.map(show, names)
"""
Tip: The kernel schedules the execution time of the threads,
    so there is no order in the completion of the threads!
"""

print('Done!!! :D')