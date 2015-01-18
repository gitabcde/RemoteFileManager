import socket
import rfmutil
import sys
client = socket.create_connection(("127.0.0.1",sys.argv[1]))
while(True):
	print('input command for excution')
	cmdstr=raw_input()
	print('cmdstr is '+cmdstr)
	if(cmdstr.endswith('get',0,3)):
		print('command type:get')
		client.send(cmdstr+'\n')
		rfmutil.GetFileFromSocket(client,cmdstr.split(' ')[1]+'-get')
	if(cmdstr.endswith('put',0,3)):
		print('command type:put')
		client.send(cmdstr+'\n')
		rfmutil.SendFileToSocket(client,cmdstr.split(' ')[1])
client.close()
