import socket
import io
import sys

BUFFERSIZE=8096	
RESPONESTRING='\n'
COMMANDEND='\n'
COMMANDSPLIT=' '
def DebugOutput(msg):
	if __debug__:
		print(msg)

def GetFileFromSocket(in_socket,recv_filename):
	fdfile=io.open(recv_filename,'ab')
	while(True):
		filebuffer=in_socket.recv(BUFFERSIZE)
		if(len(filebuffer)==0):
			break
		DebugOutput("get's  "+filebuffer)
		fdfile.write(filebuffer)
	fdfile.close()

def SendFileToSocket(in_socket,send_filename):
	fdfile=io.open(send_filename,'rb')
	while(True):
		filebuffer=fdfile.read(BUFFERSIZE)
		if(len(filebuffer)==0):
			break
		DebugOutput("send's "+filebuffer)
		in_socket.sendall(filebuffer)
	fdfile.close()

def SendCommand(in_socket,command):
	in_socket.sendall(command+COMMANDEND)
	
def WaitCommand(in_socket):
	cmdstr=''
	while(True):
		cmdstr+=in_socket.recv(BUFFERSIZE)
		if cmdstr.endswith(COMMANDEND):
			cmdstr=cmdstr.split(COMMANDEND)[0]
			break
	return cmdstr			

def SendResponeCommand(in_socket):
	in_socket.sendall(RESPONESTRING)
	
def WaitResponeCommand(in_socket):
	respcmdstr=''
	while(True):
		respcmdstr+=in_socket.recv(BUFFERSIZE)
		if respcmdstr.endswith(RESPONESTRING,0,1):
			break

