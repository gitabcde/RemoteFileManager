import socket
import rfmutil
import sys
client = socket.create_connection((sys.argv[1],sys.argv[2]))
while(True):
	print('input command for excution')
	cmdstr=raw_input()
	if(cmdstr.endswith('quit',0,4)):
		break
	rfmutil.DebugOutput('cmdstr is '+cmdstr)
	if(cmdstr.endswith('get',0,3)):
		rfmutil.DebugOutput('command type:get')
		rfmutil.SendCommandMsg(client,cmdstr)
		rfmutil.DebugOutput('send get command')
		rfmutil.WaitResponeMsg(client)
		rfmutil.DebugOutput('begin to recive data')
		rfmutil.GetFileFromSocket(client,cmdstr.split(' ')[1]+'-get')
	if(cmdstr.endswith('put',0,3)):
		rfmutil.DebugOutput('command type:put')
		rfmutil.SendCommandMsg(client,cmdstr)
		rfmutil.DebugOutput('send put command')
		rfmutil.WaitResponeMsg(client)
		rfmutil.DebugOutput('begin to send data')
		rfmutil.SendFileToSocket(client,cmdstr.split(' ')[1])
client.close()
