from socket import socket, AF_INET, SOCK_DGRAM  # Avoids wildcard import "from socket import *"
import psutil
import threading
import pickle

# Time interval between checks in seconds
interval = 10

# Settings of client
host = "127.0.0.1"  # sets IP address of target
port = 13000        # sets port of target
address = (host, port)
# UDPSock = socket(AF_INET, SOCK_DGRAM)


# Function checking usage and sending message to other pc/server
def resource_check():
    # RAM Usage in % (float)
    memory_usage = psutil.virtual_memory()[2]

    # CPU usage (whole) in % (float)
    cpu_usage = psutil.cpu_percent(percpu=False)

    # CPU usage (per core) in % (list)
    cpu_usage_percpu = psutil.cpu_percent(percpu=True)

    # Creating messages
    mem_data = "Memory usage: %d" % memory_usage + "%"
    cpu_data = "CPU usage: %d" % cpu_usage + "%"
    cpu_single_data = "CPU usage per core: %s  ""|".join(str(x) for x in cpu_usage_percpu)

    # Sending messages to target
    UDPSock = socket(AF_INET, SOCK_DGRAM)  # Opening socket
    UDPSock.sendto(pickle.dumps(mem_data), address)
    UDPSock.sendto(pickle.dumps(cpu_data), address)
    UDPSock.sendto(pickle.dumps(cpu_single_data), address)
    print("Data sent.")
    UDPSock.close()  # Closing socket


#  Runs resource_check function in given period of time
def timer_func():
    threading.Timer(interval, timer_func).start()
    resource_check()


timer_func()
