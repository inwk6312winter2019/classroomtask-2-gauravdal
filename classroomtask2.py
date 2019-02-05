class ipaddress(object):
	def __init__ (self, ipaddr, mask):
		self.ipaddr_list =  ipaddr.split(".")
		self.mask_list =  mask.split(".")
	
	ClassA = range(1,127)
	ClassB = range(127, 192)
	ClassC = range(192, 224)
	
	
	
	def get_ipaddress(self):
		return ".".join(self.ipaddr_list)

	def get_mask(self):
		return ".".join(self.mask_list)
	
	def convert_ip_to_bin(self):
		self.ipaddress_bin = []
		for octet in self.ipaddr_list:
			self.ipaddress_bin.append(format(int(octet), "08b"))
			
		return self.ipaddress_bin
	
	def convert_mask_to_bin(self):
		self.mask_bin = []
		for octet in self.mask_list:
			self.mask_bin.append(format(int(octet), "08b"))
		
		return self.mask_bin
	
	def get_wildcard(self):
		self.wildcard_list = []
		for octet in self.mask_list:
			temp = 255 - int(octet)
			self.wildcard_list.append(str(temp))
		return ".".join(self.wildcard_list)
	
	def get_network(self):
		self.network_list= []
		if (int(self.ipaddr_list[0]) in self.ClassC):
			for i in range(0,int(self.wildcard_list[3])+1):
							self.network_list.append(".".join(self.ipaddr_list[:3])+"."+str(i))
				
		return self.network_list[0]
		
		
	def get_address(self):
		self.host_min = self.network_list[1]
		self.host_max = self.network_list[-2]
		self.host_broadcast = self.network_list[-1]
		print(self.host_min)
		print(self.host_max)
		print(self.host_broadcast)



ipaddress1 = ipaddress("192.168.0.1","255.255.255.0")

print(ipaddress1.get_ipaddress())
print(ipaddress1.get_mask())
print(ipaddress1.convert_ip_to_bin())
print(ipaddress1.convert_mask_to_bin())
print(ipaddress1.get_wildcard())
print(ipaddress1.get_network())


ipaddress1.get_address()
