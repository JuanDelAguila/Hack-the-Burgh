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


fig = plt.figure()
ax = plt.axes()
#ax.plot(timeSeries, bidPriceSeries, label = "BID")
#ax.plot(timeSeries, askPriceSeries, label = "ASK")
ax.plot(timeSeries, averagePriceSeries, label = "AVERAGE")
ax.scatter(tradeTimeSeries, tradePriceSeries, s = 0.00005 * np.array(tradeVolumeSeries) ** 2,color = 'r',label = "TRADES")
plt.legend()
plt.show()
        