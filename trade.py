from Send import Send
from Receive import Receive
import numpy as np
import time

mySender = Send()
myReceiver = Receive()

def getAskVolume(data):
    return float(data[4])

def getBidVolume(data):
    return float(data[2])

def getAskPrice(data):
    return float(data[3])

def getBidPrice(data):
    return float(data[1])


#def getBidVolume(data)
SP_STOCKS = 0
ESX_STOCKS = 0

SPstatus = "RUN"
SPtimer = 0
ESXstatus = "RUN"
ESXtimer = 0

while True:
    myReceiver.buildHistorical()
    pastESXdata = myReceiver.ESXhistorical[-20:-10]
    pastSPdata = myReceiver.SPhistorical[-20:-10]

    currentESXdata = myReceiver.ESXhistorical[-10:]
    currentSPdata = myReceiver.SPhistorical[-10:]

    askPriceESX = getAskPrice(myReceiver.ESXhistorical[-1])
    bidPriceESX = getBidPrice(myReceiver.ESXhistorical[-1])
    askPriceSP = getAskPrice(myReceiver.SPhistorical[-1])
    bidPriceSP = getBidPrice(myReceiver.SPhistorical[-1])

    print(len(myReceiver.ESXhistorical))

    if len(pastSPdata) == 10:

        pastESXaskVolume = np.array([getAskVolume(row) for row in pastESXdata])
        pastSPaskVolume = np.array([getAskVolume(row) for row in pastSPdata])
        pastESXbidVolume = np.array([getBidVolume(row) for row in pastESXdata])
        pastSPbidVolume = np.array([getBidVolume(row) for row in pastSPdata])
        pastESXscore = sum(pastESXbidVolume - pastESXaskVolume)
        pastSPscore =  sum(pastSPbidVolume - pastSPaskVolume)

        currentESXaskVolume = np.array([getAskVolume(row) for row in currentESXdata])
        currentSPaskVolume = np.array([getAskVolume(row) for row in currentSPdata])
        currentESXbidVolume = np.array([getBidVolume(row) for row in currentESXdata])
        currentSPbidVolume = np.array([getBidVolume(row) for row in currentSPdata])
        currentESXscore = sum (currentESXbidVolume - currentESXaskVolume)
        currentSPscore = sum (currentSPbidVolume - currentSPaskVolume)

        THRESHOLD = 1.25
        RISK = 1000

        if ESXstatus != "WAIT":
            if currentESXscore < 0:
                if sum(pastESXaskVolume) != 0:
                    volatilityDelta = sum(currentESXaskVolume) / sum (pastESXaskVolume)
                else:
                    volatilityDelta = 1.5

                if volatilityDelta >= THRESHOLD:
                    stocksToSell = int(RISK * (volatilityDelta - 1))
                    mySender.placeOrder("SELL", "ESX-FUTURE", bidPriceESX - 1, stocksToSell)
                    print(mySender.getConfirmation())
                    ESXstatus = "WAIT"
        
            if currentESXscore > 0:
                if sum(pastESXaskVolume) != 0:
                    volatilityDelta = sum(currentESXbidVolume) / sum (pastESXbidVolume)
                else:
                    volatilityDelta = 1.5

                if volatilityDelta >= THRESHOLD:
                    stocksToBuy = int(RISK * (volatilityDelta - 1))
                    mySender.placeOrder("BUY", "ESX-FUTURE", askPriceESX + 1, stocksToBuy)
                    print(mySender.getConfirmation())
                    ESXstatus = "WAIT"

        if SPstatus != "WAIT":
            if currentSPscore < 0:
                if sum(pastSPaskVolume) != 0:
                    volatilityDelta = sum(currentSPaskVolume) / sum (pastSPaskVolume)
                else:
                    volatilityDelta = 1.5

                if volatilityDelta >= THRESHOLD:
                    stocksToSell = int(RISK * (volatilityDelta - 1))
                    mySender.placeOrder("SELL", "SP-FUTURE", bidPriceSP - 1, stocksToSell)
                    print(mySender.getConfirmation())
                    SPstatus = "WAIT"

            if currentSPscore > 0:
                if sum(pastSPaskVolume) != 0:
                    volatilityDelta = sum(currentSPbidVolume) / sum (pastSPbidVolume)
                else:
                    volatilityDelta = 1.5

                if volatilityDelta >= THRESHOLD:
                    stocksToBuy = int(RISK * (volatilityDelta - 1))
                    mySender.placeOrder("BUY", "SP-FUTURE", askPriceSP + 1, stocksToBuy)
                    print(mySender.getConfirmation())
                    SPstatus = "WAIT"

        if SPtimer == 5:
            SPstatus = "RUN"
            SPtimer = 0

        if SPstatus == "WAIT":
            SPtimer += 1

        if ESXtimer == 5:
            ESXstatus = "RUN"
            ESXtimer = 0

        if ESXstatus == "WAIT":
            ESXtimer += 1

        print("SP Wait Time: ", SPtimer)
        print("ESX Wait Time: ", ESXtimer)

        

    



 
    
    
