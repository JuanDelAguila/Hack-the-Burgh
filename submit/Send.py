import socket

# inputting an empty string makes the server listen to requests coming from other computers on the network 
class Send (object):
    def __init__(self):
        self.MY_IP = ""
        self.UDP_IP = '35.179.45.135'
        self.UDP_PORT = 8001
        self.sock = socket.socket(socket.AF_INET, # Internet
                        socket.SOCK_DGRAM) # UDP
        self.sock.bind((self.MY_IP, self.UDP_PORT))


    def placeOrder (self, action, index, price, volume):
        ORDER = "TYPE=ORDER|USERNAME=Team31|PASSWORD=W5rqx2HT|FEEDCODE=" + index + "|ACTION=" + action + "|PRICE=" + str(price) + "|VOLUME=" + str(volume)
        MESSAGE = bytes(ORDER, 'utf-8')
        self.sock.sendto(MESSAGE, (self.UDP_IP, self.UDP_PORT))

    def getConfirmation (self):
        data, addrs = self.sock.recvfrom(1024) # buffer size is 1024 bytes
        data = data.decode('utf-8')
        return data