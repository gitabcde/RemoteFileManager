#/usr/bin/python
#coding: UTF-8
import socket
import rfmutil
import sys
svrsocket=socket._socketobject()
svraddr=('127.0.0.1',int(sys.argv[1]))
svrsocket.bind(svraddr)
svrsocket.listen(5)
while(True):
	retsocket=svrsocket.accept()
	cmdstr=rfmutil.GetCommandStr(retsocket[0],'\n')
	print('cmdstr is '+cmdstr)
	if(cmdstr.endswith('get',0,3)):
		print('command type:get')
		rfmutil.SendFileToSocket(retsocket[0],cmdstr.split(' ')[1])
	if(cmdstr.endswith('put',0,3)):
		print('command type:put')
		rfmutil.GetFileFromSocket(retsocket[0],cmdstr.split(' ')[1]+'get')
	retsocket[0].close()
		

