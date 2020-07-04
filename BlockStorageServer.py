#!/usr/bin/python36

import cgi
import subprocess as sp

print("content-type: text/html")
print("")

print("hi")
form = cgi.FieldStorage() 

#diskspace = form.getvalue('diskspace')

partitionname= form.getvalue('partitionname')
print("You have provided /dev/%s",partitionname)

#print("You have provided %s",diskspace)  => You can do it after you are able to provide the downloadable and executable file to the provider.

res = sp.getstatusoutput("sudo ansible-playbook iscsiserver.yml --extra-vars='target_name={0} partition_name={1}'".format(uname,partitionname))

if res[0]==0:
	print("Your partition is successfully provided by you.")

