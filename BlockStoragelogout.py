#!/usr/bin/python

import cgi
import commands as sp

print("content-type: text/html")
print('\n')


form = cgi.FieldStorage() 
uname=form.getvalue('uname')
logins="no"
cmd=sp.getstatusoutput("sudo ansible-playbook iscsiclientlogout.yml --extra-vars='ipaddress_target=192.168.100.167 target_name={} login={}' ".format(uname,logins))
if cmd[0]==0:
	print("<p><font size='6' color='red'>You are logged out successfully</font></p>")
else:
	print("Their is some error logging out")

print('''
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<button type="button" href="http://192.168.100.167/cgi-bin/"
><a href="http://192.168.100.167/cgi-bin/">Go Back</a></button>''')
