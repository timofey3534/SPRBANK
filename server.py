import socket
import time

s = socket.socket()
print ("Socketa successfully created")

port = 12345

s.bind(('', port))
print ("socket binded to %s" %(port))



s.listen(5)
print ("socket is listening")

while True:
	c, addr = s.accept()
	print ('Got connection from', addr )
	
	name = c.recv(1024).decode()


	if name == 'Pavel':
		balanceFile = open('Text.txt', 'r')
		balance = balanceFile.readline()
		c.send(balance.encode())
		
		infoFile = open('info.txt', 'a')
		named_tuple = time.localtime()
		time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)
		infoFile.write(str(addr) + ' ' + name + ' ' + balance + ' ' + str(time_string) + '\n')
		infoFile.close()
	if name == 'Ivan':
		balanceFile = open('Text.txt', 'r')
		balance = balanceFile.readline()
		balance = balanceFile.readline()
		c.send(balance.encode())
		
		infoFile = open('info.txt', 'a')
		named_tuple = time.localtime()
		time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)
		infoFile.write(str(addr) + ' ' + name + ' ' + balance + ' ' + str(time_string) + '\n')
		infoFile.close()
	if name == 'Petya':
		balanceFile = open('Text.txt', 'r')
		for i in range(3):
			balance = balanceFile.readline()
		c.send(balance.encode())
		infoFile = open('info.txt', 'a')
		
		named_tuple = time.localtime()
		time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)
		infoFile.write(str(addr) + ' ' + name + ' ' + balance + ' ' + str(time_string) + '\n')
		infoFile.close()
	else:
		c.send('Erorr'.encode())
		
		infoFile = open('info.txt', 'a')
		named_tuple = time.localtime()
		time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)
		infoFile.write(str(addr) + ' ' + name + ' no name ' + str(time_string) + '\n')
		infoFile.close()

c.close()
