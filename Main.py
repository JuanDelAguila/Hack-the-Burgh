from Receive import Receive
from Send import Send
import numpy as np

receiver = Receive()
sender = Send()

SP = "SP-FUTURE"
ESX = "ESX-FUTURE"

#sender.placeOrder()
#print(sender.getConfirmation())

#receiver.getBidPrice(ESX)
i = 0
'''
while i < 500:
    receiver.buildHistorical()
    i += 1
    print(i)

print(receiver.historical)
np.save("receiver500.npy", receiver.historical)
'''
while True:
    print(receiver.getData())