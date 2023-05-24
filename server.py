import socket

sr = socket.socket()

print('Server socket created')

sr.bind(('server-IPv4', 9999))

sr.listen(3)

print('Server waiting for connections...')

while True:
	c, addr = sr.accept()

	print('Connected with ', addr)

	c.send(bytes('Welcome to the server', 'utf-8'))

	c.close()