#/usr/bin/python
#coding: UTF-8
import socket
import rfmutil
import sys
import thread

def svrthreadfun(retsocket,kargs):
	print(kargs)
	while(True):
		cmdstr=rfmutil.WaitCommandMsg(retsocket)
		if(cmdstr.endswith('quit',0,4)):
			break
		rfmutil.DebugOutput(cmdstr)
		if(cmdstr.endswith('get',0,3)):
			rfmutil.DebugOutput('command type:get')
			rfmutil.SendResponeMsg(retsocket)
			rfmutil.DebugOutput('send get responecommand')
			rfmutil.SendFileToSocket(retsocket,cmdstr.split(' ')[1:])
		if(cmdstr.endswith('put',0,3)):
			rfmutil.DebugOutput('command type:put')
			rfmutil.SendResponeMsg(retsocket)
			rfmutil.DebugOutput('send put responecommand')
			rfmutil.GetFileFromSocket(retsocket,cmdstr.split(' ')[1:])
	retsocket[0].close()
	thread.exit_thread()



svrsocket=socket._socketobject()
svraddr=(sys.argv[1],int(sys.argv[2]))
svrsocket.bind(svraddr)
svrsocket.listen(5)
while(True):
	retsocket=svrsocket.accept()
	thread.start_new_thread(svrthreadfun,(retsocket[0],'kargs'))
