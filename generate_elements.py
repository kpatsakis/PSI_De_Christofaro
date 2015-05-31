#!/usr/bin/python
###Generate elements###

import random

#now let's create some elements for the server and the client
server_elements=[str(random.randrange(2**200)) for i in range(1000)]
client_elements=[str(random.randrange(2**200)) for i in range(100)]

#to be sure that we have some common elements in both of them,
#we add some of the server's elements in the client's set
client_elements+=server_elements[:50]

txtclient=",".join(client_elements)
txtsrv=",".join(server_elements)

fclient=open("client_elements.txt","w")
fclient.write(txtclient)
fclient.close()

fsrv=open("srv_elements.txt","w")
fsrv.write(txtsrv)
fsrv.close()