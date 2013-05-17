'''
Author: Mohammad Al Faiyaz 
Description: Class based approach to create a remote interface for Samsung Smart TVs 
The code is a restructure of Asif Iqbal's into a class @ http://deneb.homedns.org/things/?p=232 
'''
#------------------------------------------
# TODO:
'''
* Add GNU Stuff and what not 
* Create a GUI
* Make the program remember connection settings, i.e tvip,tvtype, etc.
* Upload onto GIT or w/e 
* Add where I got a lot of this code from 
* Has to be a better way to get Mac address 
* Error checking on inputs like tvtype, conncetion issue, etc
* Error checking for constuctor, arguments must be type string 
'''

import socket 
import base64

class Remote():

	# Constructor for remote 
	# tvip,mac and tvtype must be type string 
	def __init__(self, tvip, mac, tvtype):
		#IP addresses and such for conncetions 
		self._tvip = tvip 
		self._myip = socket.gethostbyname(socket.gethostname())
		self._mac = mac # Mac address for laptop 
		# What the app reports to the tv, more info @ http://sc0ty.pl/2012/02/samsung-tv-network-remote-control-protocol/
		self.appstring = 'iphone..iapp.samsung' 
		self.tvappstring = 'iphone.%s.iapp.samsung' % (tvtype)
		# What the tv reports on screen when asking for permission 
		self.remotename = "Python Samsung Remote "
		# The socket used for connection 
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	
	# The initial connection to the tv 
	def connect(self):
		self.sock.connect((self._tvip, 55000)) # Always port 55000 from my understanding
		# Strings must be encoded in base 64  
		ipencode = base64.b64encode(self._myip) 
		macencode = base64.b64encode(self._mac)
		remoteencode = base64.b64encode(self.remotename)
		#More info on these messages can be found @ http://sc0ty.pl/2012/02/samsung-tv-network-remote-control-protocol/ 
		messagepart1 = chr(0x64) + chr(0x00) + chr(len(ipencode)) + chr(0x00) + ipencode + chr(len(macencode)) + chr(0x00) \
		+ macencode + chr(len(remoteencode)) + chr(0x00) + remoteencode;
		part1 = chr(0x00) + chr(len(self.appstring)) + chr(0x00) + self.appstring + chr(len(messagepart1)) + chr(0x00) \
		+ messagepart1;
		messagepart2 = chr(0xc8) + chr(0x00)
		part2 = chr(0x00) + chr(len(self.appstring)) + chr(0x00) + self.appstring + chr(len(messagepart2)) + chr(0x00) \
		+ messagepart2;
		self.sock.send(part1)
		self.sock.send(part2)
	
	# Sending key presses to the tv 
	def sendkey(self,key):
		messsagepart3 = chr(0x00) + chr(0x00) + chr(0x00) +chr(len(base64.b64encode(key))) + chr(0x00) + base64.b64encode(key)
		part3 = chr(0x00) + chr(len(self.appstring)) + chr(0x00) + self.appstring + chr(len(messsagepart3)) + chr(0x00) + messsagepart3
		self.sock.send(part3)
	
	# Always close socket connections!
	def close(self):
		self.sock.close()


