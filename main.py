from remote import *

myremote = Remote('192.168.1.6','D0-DF-9A-0A-CD-66','UN60D8000')
myremote.connect()
myremote.sendkey('KEY_VOLUP')
myremote.close()