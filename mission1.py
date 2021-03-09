import time
from itertools import cycle
import threading


class Thread(threading.Thread):
    pass


class TrafficLight:
    def __init__(self, __colors):
        self.__colors = __colors

    def run(self):
        for color, delay in cycle(self.__colors.items()):
            print(f' {color}')
            time.sleep(delay)


t = TrafficLight({'Red': 7, 'Yellow': 2, 'Green': 10})
t.run()
