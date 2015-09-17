#!/usr/bin/python


class Vms:

	def __init__(self, IP, range):
		self.ip = IP  
		self.cpu = range
		self.mem = range
		self.disk = range

	def getStats(self):
		return ("%s %s %s %s" %(self.ip, self.cpu, self.mem, self.disk))
#		return ("%s" %(self.ip))
