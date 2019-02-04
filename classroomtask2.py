class ipaddress(object):
	def __init__ (self, ipaddr, mask):
		self.ipaddr_list =  ipaddr.split(".")
		self.mask_list =  mask.split(".")

	def print_addr(self):
		for item in self.ipaddr_list:
			print(item,bin(int(item)),sep="\t", end =".")

		for item in self.mask_list:
			print(item,bin(int(item)), sep ="\t",end = ".")


ipaddress1 = ipaddress("192.168.1.0","255.255.255.0")

ipaddress1.print_addr()
