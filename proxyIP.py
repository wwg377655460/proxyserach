#!/usr/bin/python
# coding:utf-8

import urllib2,user_agents
from bs4 import BeautifulSoup



# url = 'http://www.xicidaili.com/nn'
# user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36'  
# cookie = '_free_proxy_session=BAh7B0kiD3Nlc3Npb25faWQGOgZFVEkiJTgxN2FlNWY3MjcxNjA5MjQ0MWYyNTc0ZDNjZjMyOGEyBjsAVEkiEF9jc3JmX3Rva2VuBjsARkkiMVJSYWtFN0pPQ25ZVGRRaHdzZnk2UWRuRXhhbURBVFNzUVVlYjU1Rm14TE09BjsARg%3D%3D--fb56197e4fb21f9a28fb16a0fe131d8b8e7185e5; CNZZDATA4793016=cnzz_eid%3D2082111554-1447387757-null%26ntime%3D1447387757';

# headers = { 'User-Agent' : user_agent , 'Cookie': cookie}   
# req = urllib2.Request(url,"", headers)  
ip = []
flag = 0
def getips(urls):
	print("begin")
	url = 'http://www.xicidaili.com' + urls
	user_agent = 'Mozilla/5.0'  
	# cookie = '_free_proxy_session=BAh7B0kiD3Nlc3Npb25faWQGOgZFVEkiJTgxN2FlNWY3MjcxNjA5MjQ0MWYyNTc0ZDNjZjMyOGEyBjsAVEkiEF9jc3JmX3Rva2VuBjsARkkiMVJSYWtFN0pPQ25ZVGRRaHdzZnk2UWRuRXhhbURBVFNzUVVlYjU1Rm14TE09BjsARg%3D%3D--fb56197e4fb21f9a28fb16a0fe131d8b8e7185e5; CNZZDATA4793016=cnzz_eid%3D2082111554-1447387757-null%26ntime%3D1447387757';
	# accept = "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8";
	# headers = { 'User-Agent' : user_agent ,'coolie':cookie, 'Accept': accept, 'Upgrade-Insecure-Requests': 1, 'Connection': 'keep-alive'}   
	
	req = urllib2.Request(url)  
	req.add_header('User-Agent', user_agent)
	response = urllib2.urlopen(req)  
	the_page = response.read() 
	soup=BeautifulSoup(the_page)
	# soup=BeautifulSoup(open('1.html'))
	# print soup
	
	port = []
	dics = {}
	list=soup.find_all('tr')
	for i in list:
		td = BeautifulSoup(str(i))
		td1 = td.find_all('td')
		td1 = td1[1:]
		k = 0;
		for j in td1:
			if k==1:
				s1 = j.string
			if k==2:
				s1 = s1+":"+j.string
				global dics
				dics['http'] = s1;
				global ip
				ip.append(dics)
				s1 = ""
				dics = {}
			k = k + 1
			

	# print ip
		# print i.get_text()
		# s = BeautifulSoup(str(i))
		# s1 = s.find('td').contents[0]
		# global ip
		# print s1


	user_agent = 'Mozilla/5.0'  
	req = urllib2.Request(url)  
	req.add_header('User-Agent', user_agent)
	response = urllib2.urlopen(req)  
	the_page = response.read() 
	soup=BeautifulSoup(the_page)

	# print the_page
	print "---------------"
	global flag
	if flag>10:
		return
	print flag
	flag = flag + 1
	ml=soup.select('a[rel=next]')
	# print str(ml)
	hrefs = BeautifulSoup(str(ml))
	select_a = hrefs.select('a')
	if(len(select_a)>=1):
		# print select_a[0].contents[0]
		urls = "/nn/" + str(select_a[0].contents[0])
		# print urls
		getips(urls)
	else:
		exit()




		

# getips()
getips('/nn/1')





