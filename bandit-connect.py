import os
# ssh username @ host -p port number

host = "bandit.labs.overthewire.org"
port = "2220"
username = str(input("username: ")) 

connect = "ssh {}@{} -p {}".format(username, host, port)

os.system(connect)