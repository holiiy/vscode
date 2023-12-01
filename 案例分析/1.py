import socket
a = socket.gethostbyname(socket.gethostname())
b = socket.getfqdn(socket.gethostname())
print('ip地址:%s\n主机名:%s'%(a,b))