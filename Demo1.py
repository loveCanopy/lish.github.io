__author__ = 'Sherlock'
#coding=utf-8
url="http://jandan.net/ooxx"
import urllib.request
import random
import urllib.parse
l1=['121.42.158.116:80','182.90.3.204:80','49.66.189.70:8080','150.255.174.58:8090','182.90.80.207:8123']
proxy_support=urllib.request.ProxyHandler({'http':random.choice(l1)})
opener=urllib.request.build_opener(proxy_support)
urllib.request.install_opener(opener)
head={}
head['User-Agent']="Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.82 Safari/537.36"
req=urllib.request.Request(url,head)
reponse=urllib.request.urlopen(url)
html=reponse.read().decode('utf-8')
print(html)
