#!/usr/bin/python2

import commands as sp

print("content-type: text/html")
print("")

print("<u><b><h1> Welcome to our paas service </h1></u></b>")

print("""
<form action='docker_paas_setup.py'>
Select your Platform
<select name='paasname'>
<option>python2</option>
<option>python3</option>
</select>
</br>
<input type='submit' />
</form>
""")


