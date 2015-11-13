#coding: utf-8

import urllib  
import urllib2 
import time

import urllib2,re,time,urllib,proxyIP,insertip,random,user_agents

url = 'http://xxx'

user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'  

proxyIP.getips("/nn/1")
headers = { 'User-Agent' : user_agent }   
j = 0
print("开始刷了")
for i in range(100):
	proxy_ip =random.choice(proxyIP.ip) #在proxy_list中随机取一个ip
	print proxy_ip
	proxy_support = urllib2.ProxyHandler(proxy_ip)
	opener = urllib2.build_opener(proxy_support,urllib2.HTTPHandler)

	req = urllib2.Request(url,"", headers)  
	
	urllib2.install_opener(opener)
	
	# print "ok ------------------"
	try:
		response = urllib2.urlopen(req, timeout=2)  
		the_page = response.read() 
	except:
		print "error"
		continue
	print "ok --------------"
	global j
	j = j + 1
	insertip.insert(proxy_ip)
	time.sleep(2)

print "error is" + str(100 - j) + " ok is " + str(j) 






