import socket
import threading
from queue import Queue

target = "localhost"
queue = Queue()
open_ports = []
threads = []


def port_scanner(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target, port))
        return True
    except:
        return False


def queue_filler(port_list):
    for port in port_list:
        queue.put(port)


def worker():
    while not queue.empty():
        port = queue.get()
        if port_scanner(port):
            print(f"Port {port} is open!")
            open_ports.append(port)
        else:
            pass


port_list = range(1, 9000)
queue_filler(port_list)

for i in range(1000):
    n_thread = threading.Thread(target=worker)
    threads.append(n_thread)

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

print(f"open ports = {open_ports}")
print(f"total of {len(open_ports)} ports are open")




