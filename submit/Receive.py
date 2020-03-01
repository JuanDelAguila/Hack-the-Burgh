import socket
import numpy as np

class Receive (object):
    def __init__(self):
        MY_IP = ""
        MESSAGE = bytes("TYPE=SUBSCRIPTION_REQUEST", 'utf-8')
        UDP_IP = '35.179.45.135'
        UDP_PORT = 7001
        self.sock = socket.socket(socket.AF_INET, # Internet
                            socket.SOCK_DGRAM) # UDP
        self.sock.bind((MY_IP, UDP_PORT))
        self.sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
        self.ESXhistorical = np.array([[]])
        self.SPhistorical = np.array([[]])

    def getData(self):
        data, addrs = self.sock.recvfrom(1024) # buffer size is 1024 bytes
        data = data.decode('utf-8')
        return data

    def buildHistorical (self):
        spData = False
        esxData = False
        INDEX = 1
        BIDPRICE = 2
        BIDVOLUME = 3
        ASKPRICE = 4
        ASKVOLUME = 5
        while (esxData != True or spData != True):
            dataType = ""
            while (dataType != "PRICE"):
                data = self.getData()
                params = data.split("|")
                dataType = params[0].split("=")[1]
            index = self.getParams(params, INDEX)
            bidPrice = float(self.getParams(params, BIDPRICE))
            bidVolume = float(self.getParams(params, BIDVOLUME))
            askPrice = float(self.getParams(params, ASKPRICE))
            askVolume = float(self.getParams(params, ASKVOLUME))
            insertion = np.array([[index, bidPrice, bidVolume, askPrice, askVolume]])
            if index == "SP-FUTURE":
                if len(self.SPhistorical[0]) == 0:
                    self.SPhistorical = insertion
                else:
                    self.SPhistorical = np.append(self.SPhistorical,insertion, axis=0)
                spData = True
            else:
                if len(self.ESXhistorical[0]) == 0:
                    self.ESXhistorical = insertion
                else:
                    self.ESXhistorical = np.append(self.ESXhistorical,insertion, axis=0)
                esxData = True



    def getParams(self, params, index):
        return params[index].split("=")[1]

            
    

