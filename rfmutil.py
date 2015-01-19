import socket
import io
import sys

buffersize=1000	
def GetFileFromSocket(in_socket,recv_filename):
	fdfile=io.open(recv_filename,'ab')
	while(1):
		filebuffer=in_socket.recv(buffersize)
		if(len(filebuffer)==0):
			break;
		print("get's  ",filebuffer)
		fdfile.write(filebuffer)
	fdfile.flush()
	fdfile.close()

def SendFileToSocket(in_socket,send_filename):
	fdfile=io.open(send_filename,'rb')
	while(1):
		filebuffer=fdfile.read(buffersize)
		if(len(filebuffer)==0):
			break;
		print("send's ",filebuffer)
		in_socket.sendall(filebuffer)
	fdfile.close()
def GetCommandStr(in_socket,in_endchar):
	cmdstr=''
	while(1):
		cmdstr+=in_socket.recv(100)
		if(cmdstr.endswith(in_endchar)):
			cmdstr=cmdstr.split(in_endchar)[0]
			break;
	return cmdstr			
	
	
