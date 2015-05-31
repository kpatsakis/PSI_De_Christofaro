#! /usr/bin/python
from StringIO import StringIO
import random
from time import time
import gmpy
import hashlib
import urllib
import urllib2
import json

e=2**16+1

def hash_int(x):
    return int(hashlib.sha256(str(x)).hexdigest(),16)

#read server's public key
fin=open("srv.key")
n=fin.read()
n=int(n.strip())
fin.close()
url = 'http://localhost:5000'

#read elements
fin=open("client_elements.txt","r")
vals=fin.read().strip()
fin.close()
client_elements=vals.split(",")

for i in range(len(client_elements)):
	client_elements[i]=int(client_elements[i])
hc=[hash_int(i) for i in client_elements]

m_A=[]
rs=[]
for i in hc:
	r=random.randrange(n)
	rs.append(r)
	obf=(pow(r, e,n)*i)%n
	m_A.append(str(obf))
vals=",".join(m_A)
print "Sending records to server"

params = urllib.urlencode({'params': vals})
response = urllib2.urlopen(url, params).read()
print "Received records from server!"
response=response.strip()
response=response.split("|")

client_elements=response[0].split(",")
for i in range(len(client_elements)):
	client_elements[i]=int(client_elements[i])

serv_elements=response[1].split(",")
for i in range(len(serv_elements)):
	serv_elements[i]=int(serv_elements[i])

for i in range(len(client_elements)):
     client_elements[i]=hash_int((client_elements[i]*gmpy.invert(rs[i],n))%n)

#now let's count the common elements
cnt=0
for i in client_elements:
    if i in serv_elements:
        cnt+=1
print "common elements:", cnt
