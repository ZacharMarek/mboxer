#!/usr/bin/env python3
import socket
import os
import sys
import signal
import hashlib
import re


def nacit(txt):
	cislo=""
	hlav=""
	
	txt=txt.strip()
	
	if not txt.isascii(): #chcem True
		return (hlav, cislo)
	if (txt[0].find(":")!=-1): #nesmie obsahovat 
		return	(hlav, cislo)
	if (txt[0].find("/")!=-1):
		return (hlav,cislo)
	
	if txt.isspace(): 
		return (hlav, cislo)
	else:
	hlav = txt[0]
	cislo = txt[1]	
		
	return(hlava, cislo)
		
#problem bude urcite tu a to v nacitavani ale neviem ako inac by som mal fuknciu nacit opravit aby vyplnilo premenne hlav a cislo

def WRITE_met(hdr,nac_sub):
	stav_cislo = 100
  	stav_popis ="OK"
  	hlava = ""
  	obsah = ""

		#m=hashlib.md5()
     	
	try:
		obsah=nac_sub.read(int(hdr["Content-length"]))
	 	h_obsah = hashlib.md5(obsah.encode()).hexdigest()
		
	 with	
	 	open(f'{hdr["Mailbox"]}/{h_obsah}',"w") as file:
		file.write(obsah)
	 	
	 #ak chyba header alebo su zle zadane hodnoty
	 
	except NameError:
		stav_ cislo, stav_popis =(200, 'bad request')
	except ValueError:
		stav_ cislo, stav_popis =(200, 'bad request')
	except KeyError:
		stav_ cislo, stav_popis =(200, 'bad request')	
	except FileExistsError:
		stav_cislo, stav_popis =(203, 'No such mailbox')
	except FileNotFoundError:
		stav_cislo, stav_popis =(203, 'No such mailbox')
	return stav_cislo, stav_popis, hlava, obsah # nenastala chyba
	 #connected_socket.send(b'PONG\n')
	 
def READ_met(hdr):
	stav_cislo = 100
  	stav_popis ="OK"
  	hlava = ""
  	obsah = ""
  	
  	try:
  		with open(f'{hdr["Mailbox"]}/{headers["Message"}') as file:
  			obsah = file.read()
  			hlava = (f'Content-length:{len(obsah)}\n')
  			
  	#nepripustne hodnoty
  	except KeyError:
  		stav_cislo, stav_popis=(200, 'bad request')
  	except FileNotFoundError:
  		stav_cislo, stav_popis=(201, 'bad request')
  	except OSError:
  		stav_cislo, stav_popis=(202, 'bad request')	
  	return (stav_cislo, stav_popis, hlava, obsah)
  		 #connected_socket.send(b'PONG\n')
  		 
 def LS_met(hdr):
 	stav_cislo = 100
  	stav_popis = "OK"
  	hlava = ""
  	obsah = "" 	
  	x=""
  	
  try:
  	x= os.listdir(hdr["Mailbox"])
  	hlava=(f'Number-of-messager:{len(x)}\n')
  	obsah= "\n".join(x) + "\n"	
  	
  	except KeyError:
  		stav_cislo, stav_popis=(200, 'bad request')
  	except FileNotFoundError:
  		stav_cislo, stav_popis=(203, 'no such mailbox')	
  	return (stav_cislo, stav_popis, hlava, obsah)	
  		 #connected_socket.send(b'PONG\n')
  	
  	
  			

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind(('',9999))
signal.signal(signal.SIGCHLD,signal.SIG_ING)
s.listen(5)

#metoda=""

while True:
	connected_socket,address=s.accept()
	print(f'spojenie z {address}')
	pid_chld=os.fork()
	if pid_chld==0:
		s.close()
		f=connected_socket.makefile('rw') #chybs utf8 
		while True:
			zoz_hl={}
			hlava = ""
  			obsah = "" 
			
			metoda=f.readline().strip()
				if not metoda:
					break
			txt=f.readline() #nacitanie txtu
		
		  while (txt !="\n")
		hlav, cislo = nacit(txt)
		zoz_hl[hlav]=vset_hlav
		txt=f.readline()
		
		#metody
		printf("metoda : ",metoda)
		
		if metoda=='WRITE':
		stav_cislo, stav_popis, hlava, obsah = WRITE_met(hdr,f)
		
		elif metoda=='READ':
		stav_cislo, stav_popis, hlava, obsah = READ_met(hdr)
		
		elif metoda== 'LS':
		stav_cislo, stav_popis, hlava, obsah = LS_met(hdr)
		
		else:
			stav_cislo, stav_popis=(204,'unknow method')
		 
		f.write(f'{stav_cislo }{stav_popis }\n')
		f.write(hlava '\n' obsah)
		f.flush()
		sys.exit(0)
		
		
			
		#connected_socket.send(b'PONG\n')
		print(f'{address} uzavrel spojenie')
		sys.exit(0)
	else:
		connected_socket.close()			

