import requests
import json
import psutil
import time

def cpu_dict():
    cpu_output = {
        "cores": psutil.cpu_count(),
        "ll": psutil.cpu_stats(),
        "percent": psutil.cpu_percent()
    }
    return cpu_output


def memory_dict():
    mem_data = psutil.virtual_memory()
    monitor_dict = {
        "total_memory": mem_data[0],
        "total_available": mem_data[1],
        "memory_percent": mem_data[2],
        "used": mem_data[3],
        "free": mem_data[4],
        "active": mem_data[5]
    }
    return monitor_dict


def generate_status():
    status = {
        "cpu": cpu_dict(),
        "memory": memory_dict()
    }
    return status

for i in range(100000):
    time.sleep(.001)
    r = requests.post("http://127.0.0.1:5000/post", json=generate_status())
    print(r.json(), i)