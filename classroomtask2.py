class ipaddress(object):
	def __init__ (self, ipaddr, mask):
		self.ipaddr_list =  ipaddr.split(".")
		self.mask_list =  mask.split(".")

	def print_addr(self):
		for str1 in self.ipaddr_list:
			print(str1,".",end="")
		print("\t")
		for item in self.ipaddr_list:
			print(bin(int(item)),".",end= "")
		for mask1 in self.mask_list:
			print(mask1,".",end="")
		print("\t")
		for item in self.mask_list:
			print(bin(int(item)),".",end = "")


ipaddress1 = ipaddress("192.168.1.0","255.255.255.0")

ipaddress1.print_addr()
