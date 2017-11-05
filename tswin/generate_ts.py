import numpy as np
import datetime as dt
import pandas as pd
from numpy_ringbuffer import RingBuffer

dates = pd.date_range('2017-01-01', '2017-09-30', freq='H')
int_range = range(len(dates))

history = []
past_window = RingBuffer(72)


def weighted_bool(weight: float):
    if np.random.random() < weight:
        return True
    else:
        return False

def event(i, past):
    output = [i, False, False, False, weighted_bool(.5)]
    intersting_past = past[0:np.random.randint(1,70)]

    try:
        if sum(intersting_past[:,4]) > 20:
            output[3] = True

        if sum(intersting_past[:,3]) > 10:
            output[2] = False

    except IndexError:
        pass

    return output

for period in int_range:
#    print(period)
    e = event(period, past_window)
    history.append(e)
    past_window.append(e[1::])
    #print(past_window)

print(history)

