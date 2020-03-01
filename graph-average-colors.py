import csv
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np

my_day = "03/01/2020 "

TIME = 0
INDEX = 1
BIDPRICE = 2
BIDVOLUME = 3
ASKPRICE = 4
ASKVOLUME = 5
SIDE = 2
PRICE = 3
VOLUME = 4


timeSeries = []
averagePriceSeries = []
bidPriceSeries = []
askPriceSeries = []
askVolumeSeries = []
bidVolumeSeries = []

tradeTimeSeries = []
tradePriceSeries = []
tradeVolumeSeries = []

currentIndex = "ESX-FUTURE"
with open('market_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count != 0:
            time = datetime.strptime(my_day + row[TIME], "%m/%d/%Y %H:%M:%S")
            index = row[INDEX]
            bidPrice = float(row[BIDPRICE])
            bidVolume = float(row[BIDVOLUME])
            askPrice = float(row[ASKPRICE])
            averagePrice = (bidPrice + askPrice) / 2
            askVolume = float(row[ASKVOLUME])
            if index == currentIndex:
                timeSeries += [time]
                bidVolumeSeries += [bidVolume]
                averagePriceSeries += [averagePrice]
                bidPriceSeries += [bidPrice]
                askPriceSeries += [askPrice]
        line_count += 1

with open('trades.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count != 0:
            time = datetime.strptime(my_day + row[TIME], "%m/%d/%Y %H:%M:%S")
            index = row[INDEX]
            side = row[SIDE]
            price = float(row[PRICE])
            volume = float(row[VOLUME])
            if index == currentIndex:
                tradeTimeSeries += [time]
                tradePriceSeries += [price]
                tradeVolumeSeries += [volume]
        line_count += 1

def findAverage (time):
    try:
        pos = timeSeries.index(time)
        average = averagePriceSeries[pos]
        return average
    except Exception:
        return False


tradeVolumeAboveAverage = []
tradeTimeAboveAverage = []
closingPriceAboveAverage = []
tradeVolumeBellowAverage = []
tradeTimeBellowAverage = []
closingPriceBellowAverage = []

for i in range (0, len(tradeTimeSeries)):
    time = tradeTimeSeries[i]
    averagePrice = findAverage(time)
    if averagePrice != False:
        volume = tradeVolumeSeries[i]
        closingPrice = tradePriceSeries[i]
        averagePrice = findAverage(time)
        if closingPrice >= averagePrice:
            tradeTimeAboveAverage += [time]
            tradeVolumeAboveAverage += [volume]
            closingPriceAboveAverage += [closingPrice]
        else:
            tradeTimeBellowAverage += [time]
            tradeVolumeBellowAverage += [volume]
            closingPriceBellowAverage += [closingPrice]
    

def normalize(v):
    norm = np.linalg.norm(v)
    if norm == 0: 
       return v
    return v / norm

fig = plt.figure()
ax = plt.axes()
#ax.plot(timeSeries, bidPriceSeries, label = "BID")
#ax.plot(timeSeries, askPriceSeries, label = "ASK")
ax.plot(timeSeries, averagePriceSeries, label = "AVERAGE")
#ax.scatter(tradeTimeSeries, tradePriceSeries, s = 0.00005 * np.array(tradeVolumeSeries) ** 2,color = 'r',label = "TRADES")
#ax.scatter(tradeTimeBellowAverage, closingPriceBellowAverage, s = 0.00001 * np.array(tradeVolumeBellowAverage) ** 2, color = 'r', label = "BELLOW AVERAGE")
ax.vlines(tradeTimeBellowAverage, closingPriceBellowAverage + -20 * normalize(np.array(tradeVolumeBellowAverage) ** 2) , closingPriceBellowAverage, color = 'r', label = "BELLOW AVERAGE", linewidth = 2)
#ax.scatter(tradeTimeAboveAverage, closingPriceAboveAverage, s = 10 * normalize(np.array(tradeVolumeAboveAverage) ** 2), color = 'g', label = "ABOVE AVERAGE")
ax.vlines(tradeTimeAboveAverage, closingPriceAboveAverage, closingPriceAboveAverage + 20 * normalize(np.array(tradeVolumeAboveAverage) ** 2), color = 'g', label = "ABOVE AVERAGE", linewidth = 2)
plt.legend()
plt.show()


