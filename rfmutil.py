import socket
import io
import sys

BUFFERSIZE=8096	
RESPONESTRING='ok'
MSGEND='\n'
COMMANDPARAMSPLIT=' '
def DebugOutput(msg):
	if __debug__:
		print(msg)

def GetFileFromSocket(in_socket,params):
	fdfile=io.open(params[1],'ab')
	infomsg=WaitExtInfoMsg(in_socket)
	length=int(infomsg)
	SendResponeMsg(in_socket)
	while(length>0):
		filebuffer=in_socket.recv(BUFFERSIZE)
		length-=len(filebuffer)
		DebugOutput("fielbuffer's length is "+str(len(filebuffer)))
		DebugOutput("get's  "+filebuffer)
		fdfile.write(filebuffer)
	fdfile.close()

def SendFileToSocket(in_socket,params):
	fdfile=io.open(params[0],'rb')
	fdfile.seek(0,io.SEEK_END)
	length=fdfile.tell()
	fdfile.seek(0,io.SEEK_SET)
	SendExtInfoMsg(in_socket,str(length))
	WaitResponeMsg(in_socket)
	while(True):
		filebuffer=fdfile.read(BUFFERSIZE)
		if(len(filebuffer)==0):
			break
		DebugOutput("send's "+filebuffer)
		in_socket.sendall(filebuffer)
	fdfile.close()

def SendCommandMsg(in_socket,command):
	in_socket.sendall(command+MSGEND)
	
def WaitCommandMsg(in_socket):
	cmdstr=''
	while(True):
		cmdstr+=in_socket.recv(BUFFERSIZE)
		if cmdstr.endswith(MSGEND):
			cmdstr=cmdstr.split(MSGEND)[0]
			break
	return cmdstr			

def SendResponeMsg(in_socket):
	in_socket.sendall(RESPONESTRING+MSGEND)
	
def WaitResponeMsg(in_socket):
	respcmdstr=''
	while(True):
		respcmdstr+=in_socket.recv(BUFFERSIZE)
		if respcmdstr.endswith(MSGEND):
			respcmdstr=respcmdstr.split(MSGEND)[0]
			DebugOutput('respone:'+respcmdstr)
			break
	return respcmdstr	

def SendExtInfoMsg(in_socket,info):
	in_socket.sendall(info+MSGEND)

def WaitExtInfoMsg(in_socket):
	infomsg=''
	while(True):
		infomsg+=in_socket.recv(BUFFERSIZE)
		if(infomsg.endswith(MSGEND)):
			infomsg=infomsg.split(MSGEND)[0]
			DebugOutput('InfoMsg is:'+infomsg)
			break
	return infomsg

