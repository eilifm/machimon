import time
import ujson
import pprint
from collections import deque
from numpy import array, sum, mean
import numpy as np
from numpy_ringbuffer import RingBuffer

def is_important(s):
    s = ujson.loads(s)
    # if s['data']['cpu']['percent'] < 20:
    if s['ts'] > 1508704656766310:
        return s

#filtered_list = list(filter(is_important, open('log.json', "r")))
#
#print(len(filtered_list))

def main():
    window = RingBuffer(capacity=100, dtype=(float, 4))
    with open("log.json", "r") as data_file:
        for line in data_file:
            data = ujson.loads(line)
            if data['data']['cpu']['percent'] < 50:
                window.append([data['data']['cpu']['percent'], data['ts'], 0, 0])
                print(np.mean(window, 0)[0])
                #print(window)
                #print(data['data']['cpu']['percent'])
                #print(len(window))
                #print(mean(array(window), 0))
                #time.sleep(.1)

main()
