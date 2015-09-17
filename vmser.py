#!/usr/bin/python

import socket
import time
import os.path
import sys


runtime =  int(sys.argv[1]) * 10 

print "Stats Aggregation Server started with runtime %d" %runtime

s = socket.socket()
host = "127.0.0.1"
port = 8899
s.bind((host, port))
s.listen(5)
starttime = time.time()
iplist = []
while ((time.time() - starttime) < runtime):
	c, addr = s.accept()
	str = c.recv(1024)
	list = str.split()
	c.close()
	file = list[0] + ".log"
	if not (os.path.isfile(file)):
		iplist.append(list[0])
	fo = open(file, "a")
	fo.write(str)
	fo.write("\n")
	fo.close()
print "           VM stats Report and Reclamation Recommendation"
for ip in iplist:
	file = open(ip + ".log")
	line = file.readline()
	i = 0
	mem = 0
	cpu = 0
	disk = 0
	while line:
		i = i + 1
		list = line.split()
	 	cpu = cpu + int(list[1])
		mem = mem + int(list[2])
		disk = disk + int(list[3])	
		line = file.readline()
	file.close()
	cpu_ave = cpu / i
	mem_ave = mem / i
	disk_ave = disk / i
	print "ip %s cpu_ave %d mem_ave %d disk_ave %d" %(ip, cpu_ave, mem_ave, disk_ave)
	if cpu_ave <= 10 and mem_ave <= 10 and disk_ave <= 10:
		print "    Reclaim VM IP %s for under usage" %ip
