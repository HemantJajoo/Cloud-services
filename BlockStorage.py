#!/usr/bin/python36

import cgi
import subprocess as sp

print("content-type: text/html")
print('\n')

form = cgi.FieldStorage() 
uname=form.getvalue('uname')
diskspace = form.getvalue('diskspace')
matrix= form.getvalue('matrix')
ip=form.getvalue('ip')
passwd=form.getvalue('passwd')

print("<p><font size='6' color='red'>You selected {0} {1} and your IP is: {2}</font></p>".format(diskspace,matrix,ip))

fh = open('/etc/ansible/hosts','a+')
fh.write('[iscsiclient] \n{0} ansible_ssh_user=root ansible_ssh_pass={1}\n'.format(ip,passwd))
fh.close()

#print("hi")
login="yes"

cmd = sp.getstatusoutput("sudo ansible-playbook iscsiclient.yml --extra-vars='ipaddress_target=192.168.100.167 target_name={} login={}' ".format(uname,login))

#print("2")
if res[0]==0:
	print("<p><font size='5' color='red'>We have successfully added the disk to your system<br/>")
	print("You can use` it as per your convience now<br/>")
	print("Please change your root's password now<br/></font></p>")
	print("<form action='BlockStoragelogout.py'>")
	x=uname
	print("<input type='hidden' name='uname' value={0} />".format(x))
	print("<input type=submit name='logout' value='Logout'/>")
	print("</form>") 
else:
	print("Sorry we are unable to process your request")


