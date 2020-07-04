#!/usr/bin/python

import commands as sp

print("content-type: text/html") 
print("")

sp.getoutput(" sudo ansible-playbook caas-ansible.yml ")

print("Container has been launched succesfully")
print("</br>")
print("Enter yourIP:5555 in your browser to access the container")
print("</br>")
print("Login Credentials")
print("</br>")
print("User:root &  Password:redhat")

