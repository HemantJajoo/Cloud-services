#!/usr/bin/python2

import commands as sp
import cgi

print("content-type: text/html")
print("")


form = cgi.FieldStorage()

paasname = form.getvalue("paasname")

s ="""FROM centos:latest
CMD {}
""".format(paasname)

fh = open('/var/www/cgi-bin/Project/Dockerfile', 'w')

fh.write(s)

fh.close()


cmd = "sudo docker build /var/www/cgi-bin/Project/ -t mypaas-{}:v1".format(paasname)


output = sp.getstatusoutput(cmd)

if output[0] == 0:
	print("Platform Created Successfully")

else:
	print("Error")

#print("""<iframe src="http://192.168.100.167:4200" > </iframe>""")











