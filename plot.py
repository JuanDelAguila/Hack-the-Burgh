import numpy as np 
import matplotlib.pyplot as plt

def askPrice(data, index):
    data = [float(row[3]) for row in data if row[0] == index]
    return data

def bidPrice(data, index):
    data = [float(row[1]) for row in data if row[0] == index]
    return data

sp = np.load("receiver500.npy")
ASKsp = askPrice(sp, "SP-FUTURE")
BIDsp = bidPrice(sp, "SP-FUTURE")
xsp = np.arange(len(ASKsp))

print(ASKsp)


'''
esx = np.load("receiver500.npy")
esx = filterByIndex(esx, "ESX-FUTURE")
xesx = np.arange(len(esx))
'''
fig = plt.figure()
ax = plt.axes()
ax.plot(xsp, ASKsp, 'r', label = "ASK")
ax.plot(xsp, BIDsp, 'b', label = "BID")
plt.legend()
plt.show()

