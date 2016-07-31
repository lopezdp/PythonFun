import socket

webSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
webSocket.connect(('www.pythonlearn.com', 80))
webSocket.send('GET http://www.pythonlearn.com/code/intro-short.txt HTTP/1.0\n\n')

while True:
	data = webSocket.recv(512)
	if(len(data) < 1):
		break
	print data.rstrip()

webSocket.close()
















