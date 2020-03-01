

#from Send import Send
#from Receive import Receive
#from candlesMod import Candle
#import numpy as np
#import time
#import datetime
'''
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

def getTradeData(data):
    return getAskPrice

#def getBidVolume(data)
SP_STOCKS = 0
ESX_STOCKS = 0

SPstatus = "RUN"
SPtimer = 0
ESXstatus = "RUN"
ESXtimer = 0

while True:


    myReceiver.buildHistorical()

    currentESXdata = myReceiver.ESXhistorical[-30:]
    currentSPdata = myReceiver.SPhistorical[-30:]

    previousESXdata = myReceiver.ESXhistorical[-60:-30]
    previousSPdata = myReceiver.SPhistorical[-60:-30]

    ppreviousESXdata = myReceiver.ESXhistorical[-90:-60]
    ppreviousSPdata = myReceiver.SPhistorical[-90:-60]


    askPriceESX = np.array([getAskPrice(row) for row in currentESXdata])
    bidPriceESX = np.array([getBidPrice(row) for row in currentESXdata])
    askPriceSP = np.array([getAskPrice(row) for row in currentSPdata])
    bidPriceSP = np.array([getBidPrice(row) for row in currentSPdata])
    averagePriceESX = float(askPriceESX + bidPriceESX) / 2
    averageClosePriceESX = (float(askPriceESX[len(askPriceESX)] - 1) + float(askPriceESX[len(bidPriceESX) -1])) /2
    averagePriceSP = float(askPriceSP + bidPriceSP) / 2
    averageClosePriceSP = (float(askPriceSP[len(askPriceSP)] - 1) + float(askPriceSP[len(bidPriceSP) - 1])) / 2

    prevAskPriceESX = np.array([getAskPrice(row) for row in previousESXdata])
    prevBidPriceESX = np.array([getBidPrice(row) for row in previousESXdata])
    prevAskPriceSP = np.array([getAskPrice(row) for row in previousSPdata])
    prevBidPriceSP = np.array([getBidPrice(row) for row in previousSPdata])
    prevAveragePriceESX = float(prevAskPriceESX + prevBidPriceESX) / 2
    prevAveragePriceSP = float(prevAskPriceSP + prevBidPriceSP) / 2
    prevAverageClosePriceESX = (float(prevAskPriceESX[len(prevAskPriceESX)] - 1) + float(prevAskPriceESX[len(prevBidPriceESX) - 1])) / 2
    prevAverageClosePriceSP = (float(prevAskPriceSP[len(prevAskPriceSP)] - 1) + float(prevAskPriceSP[len(prevBidPriceSP) - 1])) / 2

    pprevAskPriceESX = np.array([getAskPrice(row) for row in ppreviousESXdata])
    pprevBidPriceESX = np.array([getBidPrice(row) for row in ppreviousESXdata])
    pprevAskPriceSP = np.array([getAskPrice(row) for row in ppreviousSPdata])
    pprevBidPriceSP = np.array([getBidPrice(row) for row in ppreviousSPdata])
    pprevAveragePriceESX = float(pprevAskPriceESX + pprevBidPriceESX) / 2
    pprevAveragePriceSP = float(pprevAskPriceSP + pprevBidPriceSP) / 2
    pprevAverageClosePriceESX = (float(pprevAskPriceESX[len(pprevAskPriceESX)] - 1) + float(pprevAskPriceESX[len(pprevBidPriceESX) - 1])) / 2
    pprevAverageClosePriceSP = (float(pprevAskPriceSP[len(pprevAskPriceSP)] - 1) + float(pprevAskPriceSP[len(pprevBidPriceSP) - 1])) / 2


    currentESXaskVolume = np.array([getAskVolume(row) for row in currentESXdata])
    currentSPaskVolume = np.array([getAskVolume(row) for row in currentSPdata])
    currentESXbidVolume = np.array([getBidVolume(row) for row in currentESXdata])
    currentSPbidVolume = np.array([getBidVolume(row) for row in currentSPdata])
    averageESXbidVolume = float(sum(currentESXbidVolume)) / len(currentESXbidVolume)
    averageESXaskVolume = float(sum(currentESXaskVolume)) / len(currentESXaskVolume)
    averageSPbidVolume = float(sum(currentSPbidVolume)) / len(currentSPbidVolume)
    averageSPaskVolume = float(sum(currentSPaskVolume)) / len(currentSPaskVolume)

    prevESXaskVolume = np.array([getAskVolume(row) for row in previousESXdata])
    prevSPaskVolume = np.array([getAskVolume(row) for row in previousSPdata])
    prevESXbidVolume = np.array([getBidVolume(row) for row in previousESXdata])
    prevSPbidVolume = np.array([getBidVolume(row) for row in previousSPdata])
    prevESXbidVolume = float(sum(currentESXbidVolume)) / len(prevESXbidVolume)
    prevESXaskVolume = float(sum(currentESXaskVolume)) / len(prevESXaskVolume)
    prevSPbidVolume = float(sum(currentSPbidVolume)) / len(prevSPbidVolume)
    prevSPaskVolume = float(sum(currentSPaskVolume)) / len(prevSPaskVolume)

    pprevESXaskVolume = np.array([getAskVolume(row) for row in previousESXdata])
    pprevSPaskVolume = np.array([getAskVolume(row) for row in previousSPdata])
    pprevESXbidVolume = np.array([getBidVolume(row) for row in previousESXdata])
    pprevSPbidVolume = np.array([getBidVolume(row) for row in previousSPdata])
    pprevESXbidVolume = float(sum(currentESXbidVolume)) / len(pprevESXbidVolume)
    pprevESXaskVolume = float(sum(currentESXaskVolume)) / len(pprevESXaskVolume)
    pprevSPbidVolume = float(sum(currentSPbidVolume)) / len(pprevSPbidVolume)
    pprevSPaskVolume = float(sum(currentSPaskVolume)) / len(pprevSPaskVolume)


    time = str(datetime.now())


    passID_array = []



    if len(currentESXdata) == 30:
        columnsData = np.collapse(averageClosePriceESX, max(averagePriceESX), min(averagePriceESX), time, averageESXbidVolume,averageESXaskVolume)
        passID_array += (Candle(columnsData).patternID)

    if len(previousESXdata) == 30:
        columnsData = np.collapse(prevAverageClosePriceESX, max(prevAveragePriceESX), min(prevAveragePriceESX), time, prevESXbidVolume, prevESXaskVolume)
        passID_array += (Candle(columnsData).patternID)

    if len(ppreviousESXdata) == 30:
        columnsData = np.collapse(pprevAverageClosePriceESX, max(pprevAveragePriceESX), min(pprevAveragePriceESX), time, pprevESXbidVolume,pprevESXaskVolume)
        passID_array += (Candle(columnsData).patternID)

    if len(currentSPdata) == 30:
        columnsData = np.collapse(averageClosePriceSP, max(averagePriceSP), min(averagePriceSP), time, averageSPbidVolume,averageSPaskVolume)
        passID_array += (Candle(columnsData).patternID)

    if len(previousSPdata) == 30:
        columnsData = np.collapse(prevAverageClosePriceSP, max(prevAveragePriceSP), min(prevAveragePriceSP), time, prevSPbidVolume, prevSPaskVolume)
        passID_array += (Candle(columnsData).patternID)

    if len(ppreviousSPdata) == 30:
        columnsData = np.collapse(pprevAverageClosePriceSP, max(pprevAveragePriceSP), min(pprevAveragePriceSP), time, pprevSPbidVolume,pprevSPaskVolume)
        passID_array += (Candle(columnsData).patternID)

    def decision_ESX (values_ID):
        index = "ESX-FUTURE"

        all3positive = True
        positive2row = False
        dummy2positive = False
        negative2row = False
        dummy2negative = False
        all3negative = True
        value =0
        RISK = 2000 * (value)

        for i in values_ID:
            all3positive = all3positive and (i > 0)
        for i in values_ID:
            all3negative = all3negative and (i < 0)
        for i in values_ID:
            if i > 0:
                if dummy2positive == True:
                    positive2row = True
                else:
                    dummy2positive = True
            else:
                dummy2positive == False
        for i in values_ID:
            if i < 0:
                if dummy2negative == True:
                    negative2row = True
                else:
                    dummy2negative = True
            else:
                dummy2positive == False

        if all3positive:
            price = askPriceESX
            mySender.placeOrder("BUY", index, price, RISK)
        elif all3negative:
            price = bidPriceESX
            mySender.placeOrder("SELL", index, price, RISK)
        elif positive2row:
            price = askPriceESX
            mySender.placeOrder("BUY", index, price, RISK)
        elif negative2row:
            price = askPriceESX
            mySender.placeOrder("SELL", index, price, RISK)

    def decision_SP(values_ID):
        index = "SP-FUTURE"

        all3positive = True
        positive2row = False
        dummy2positive = False
        negative2row = False
        dummy2negative = False
        all3negative = True
        value = 0

        if all3positive:
            value = 1.75
        elif all3negative:
            value = 1.75
        elif positive2row:
            value = 1.1
        elif negative2row:
            value = 1.1


        for i in values_ID:
            all3positive = all3positive and (i > 0)
        for i in values_ID:
            all3negative = all3negative and (i < 0)
        for i in values_ID:
            if i > 0:
                if dummy2positive == True:
                    positive2row = True

                else:
                    dummy2positive = True
            else:
                dummy2positive == False
        for i in values_ID:
            if i < 0:
                if dummy2negative == True:
                    negative2row = True
                else:
                    dummy2negative = True
            else:
                dummy2positive == False

        if all3positive:
            value = 1.75
        elif all3negative:
            value = 1.75
        elif positive2row:
            value = 1.1
        elif negative2row:
            value = 1.1


        RISK = 2000 * (value)

        if all3positive:
            price = askPriceSP
            mySender.placeOrder("BUY", index, price, RISK)
        elif all3negative:
            price = bidPriceSP
            mySender.placeOrder("SELL", index, price, RISK)
        elif positive2row:
            price = askPriceSP
            mySender.placeOrder("BUY", index, price, RISK)
        elif negative2row:
            price = askPriceSP
            mySender.placeOrder("SELL", index, price, RISK)



    def max (arraylists):
        maximum = arraylists[0]
        for item in arraylists:
            if item > maximum:
                maximum = item


    def min (arraylists):
        maximum = arraylists[0]
        for item in arraylists:
            if item > maximum:
                maximum = item


'''

'''
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
                average = THRESHOLD * sum ([getAskVolume(row) for row in pastESXdata]) / len(pastESXdata)
                currentAverage  = sum (currentESXaskVolume) / len(currentESXaskVolume)
                volatilityDelta = currentAverage / average

                if currentAverage >= average:
                    stocksToSell = int(RISK *volatilityDelta)
                    mySender.placeOrder("SELL", "ESX-FUTURE", bidPriceESX - 1, stocksToSell)
                    print(mySender.getConfirmation())
                    ESXstatus = "WAIT"
        
            if currentESXscore > 0:
                average = THRESHOLD * sum ([getBidVolume(row) for row in pastESXdata]) / len(pastESXdata)
                currentAverage  = sum (currentESXbidVolume) / len(currentESXbidVolume)
                volatilityDelta = currentAverage / average

                if currentAverage >= average:
                    stocksToBuy = int(RISK*volatilityDelta)
                    mySender.placeOrder("BUY", "ESX-FUTURE", askPriceESX + 1, stocksToBuy)
                    print(mySender.getConfirmation())
                    ESXstatus = "WAIT"

        if SPstatus != "WAIT":
            if currentSPscore < 0:
                average = THRESHOLD * sum ([getAskVolume(row) for row in pastSPdata]) / len(pastSPdata)
                currentAverage  = sum (currentSPaskVolume) / len(currentSPaskVolume)
                volatilityDelta = currentAverage / average

                if volatilityDelta >= THRESHOLD:
                    stocksToSell = int(RISK * volatilityDelta)
                    mySender.placeOrder("SELL", "SP-FUTURE", bidPriceSP - 1, stocksToSell)
                    print(mySender.getConfirmation())
                    SPstatus = "WAIT"

            if currentSPscore > 0:
                average = THRESHOLD * sum ([getBidVolume(row) for row in pastSPdata]) / len(pastSPdata)
                currentAverage  = sum (currentSPbidVolume) / len(currentSPbidVolume)
                volatilityDelta = currentAverage / average

                if currentAverage >= average:
                    stocksToBuy = int(RISK * volatilityDelta)
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
        
'''