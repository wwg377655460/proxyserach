

def insert(ips):
	fp = open("ips.txt",'a') 
	fp.writelines(str(ips))
	print str(ips) + "-------------------------"
	fp.flush()
	fp.close() 
