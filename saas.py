#!/usr/bin/python36
import cgi
import subprocess as sp
#form=cgi.FieldStorage()
#uname=form.getvalue()
#passwd=form.getvalue()
#service=form.getvalue()
uname="yu"
passwd="yu"
service="firefox"
sp.getstatusoutput("sudo su - ansible")

run_ansible=sp.getstatusoutput("sudo ansible-playbook /home/ansible/current/saas.yml --extra-values username="+ uname+"passwd="+passwd+"service="+service)




