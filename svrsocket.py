#/usr/bin/python
#coding: UTF-8
import socket
import rfmutil
import sys
svrsocket=socket._socketobject()
svraddr=(sys.argv[1],int(sys.argv[2]))
svrsocket.bind(svraddr)
svrsocket.listen(5)
while(True):
	retsocket=svrsocket.accept()
	cmdstr=rfmutil.WaitCommand(retsocket[0])
	rfmutil.DebugOutput(cmdstr)
	if(cmdstr.endswith('get',0,3)):
		rfmutil.DebugOutput('command type:get')
		rfmutil.SendResponeCommand(retsocket[0])
		rfmutil.DebugOutput('send get responecommand')
		rfmutil.SendFileToSocket(retsocket[0],cmdstr.split(' ')[1])
	if(cmdstr.endswith('put',0,3)):
		rfmutil.DebugOutput('command type:put')
		rfmutil.SendResponeCommand(retsocket[0])
		rfmutil.DebugOutput('send put responecommand')
		rfmutil.GetFileFromSocket(retsocket[0],cmdstr.split(' ')[1]+'get')
	retsocket[0].close()
		

