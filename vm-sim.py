#!/usr/bin/python

import socket
import time
import sys
import random
from Vms import Vms


IP=sys.argv[1]
range=int(sys.argv[2])

vmInst = Vms(IP, random.randint(1,range))

s = socket.socket()
port = 8899
host = '127.0.0.1'

s.connect((host, port))
buf = vmInst.getStats()
s.send(buf)
s.close()
