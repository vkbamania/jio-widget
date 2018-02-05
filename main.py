# import json
from jio import getjiodata
from local import getlocaljiodata
import socket

REMOTE_SERVER = "jiofi.local.html"
def is_connected(hostname):
    try:
        host = socket.gethostbyname(hostname)
        s = socket.create_connection((host, 80), 2)
        return True
    except:
        pass
    return False

if is_connected(REMOTE_SERVER):
    localdata = getlocaljiodata()
    onnetdata = getjiodata()
else:
    print ("Connect to JioFi")

print ("localdata :" +localdata+  ", onnetdata : " + onnetdata)
