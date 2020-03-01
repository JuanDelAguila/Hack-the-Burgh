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
askPriceSeries = []
bidPriceSeries = []
askVolumeSeries = []
bidVolumeSeries = []

timeSeries1 = []
askPriceSeries1 = []
bidPriceSeries1 = []
askVolumeSeries1 = []
bidVolumeSeries1 = []

tradeTimeAskSeries = []
tradeTimeBidSeries = []
tradePriceBidSeries = []
tradePriceAskSeries = []
tradeVolumeBidSeries = []
tradeVolumeAskSeries = []

tradeTimeAskSeries1 = []
tradeTimeBidSeries1 = []
tradePriceBidSeries1 = []
tradePriceAskSeries1 = []
tradeVolumeBidSeries1 = []
tradeVolumeAskSeries1 = []

currentIndex = "ESX-FUTURE"
f = open('market_data.csv')
csv_reader = csv.reader(f, delimiter=',')
line_count = 0
for row in csv_reader:
    if line_count != 0:
        time = datetime.strptime(my_day + row[TIME], "%m/%d/%Y %H:%M:%S")
        index = row[INDEX]
        bidPrice = float(row[BIDPRICE])
        bidVolume = float(row[BIDVOLUME])
        askPrice = float(row[ASKPRICE])
        askVolume = float(row[ASKVOLUME])
        if index == currentIndex:
            timeSeries += [time]
            bidPriceSeries += [bidPrice]
            bidVolumeSeries += [bidVolume]
            askPriceSeries += [askPrice]
    line_count += 1
f.close()

f = open('trades.csv')
csv_reader = csv.reader(f, delimiter=',')
line_count = 0
for row in csv_reader:
    if line_count != 0:
        time = datetime.strptime(my_day + row[TIME], "%m/%d/%Y %H:%M:%S")
        index = row[INDEX]
        side = row[SIDE]
        price = float(row[PRICE])
        volume = float(row[VOLUME])
        if index == currentIndex:
            if side == "ASK":
                tradeTimeAskSeries += [time]
                tradePriceAskSeries += [price]
                tradeVolumeAskSeries += [volume]
            else:
                tradeTimeBidSeries += [time]
                tradePriceBidSeries += [price]
                tradeVolumeBidSeries += [volume]
    line_count += 1
f.close()

currentIndex = "SP-FUTURE"
f = open('market_data.csv')
csv_reader = csv.reader(f, delimiter=',')
line_count = 0
for row in csv_reader:
    if line_count != 0:
        time = datetime.strptime(my_day + row[TIME], "%m/%d/%Y %H:%M:%S")
        index = row[INDEX]
        bidPrice = float(row[BIDPRICE])
        bidVolume = float(row[BIDVOLUME])
        askPrice = float(row[ASKPRICE])
        askVolume = float(row[ASKVOLUME])
        if index == currentIndex:
            timeSeries1 += [time]
            bidPriceSeries1 += [bidPrice]
            bidVolumeSeries1 += [bidVolume]
            askPriceSeries1 += [askPrice]
    line_count += 1
f.close()

f = open('trades.csv')
csv_reader = csv.reader(f, delimiter=',')
line_count = 0
for row in csv_reader:
    if line_count != 0:
        time = datetime.strptime(my_day + row[TIME], "%m/%d/%Y %H:%M:%S")
        index = row[INDEX]
        side = row[SIDE]
        price = float(row[PRICE])
        volume = float(row[VOLUME])
        if index == currentIndex:
            if side == "ASK":
                tradeTimeAskSeries1 += [time]
                tradePriceAskSeries1 += [price]
                tradeVolumeAskSeries1 += [volume]
            else:
                tradeTimeBidSeries1 += [time]
                tradePriceBidSeries1 += [price]
                tradeVolumeBidSeries1 += [volume]
    line_count += 1
f.close()

fig = plt.figure()
ax = plt.axes()
ax.plot(timeSeries, bidPriceSeries, label = "BID - ESX")
ax.plot(timeSeries, askPriceSeries, label = "ASK - ESX")
ax.scatter(tradeTimeBidSeries, np.array(tradePriceBidSeries), s = 0.000005 * np.array(tradeVolumeBidSeries) ** 2, label = "BID - ESX")
ax.scatter(tradeTimeAskSeries, np.array(tradePriceAskSeries), s = 0.000005 * np.array(tradeVolumeAskSeries) ** 2 ,label = "ASK - ESX")
ax.plot(timeSeries1, np.array(bidPriceSeries1)+500, label = "BID - SP")
ax.plot(timeSeries1, np.array(askPriceSeries1)+500, label = "ASK - SP")
ax.scatter(tradeTimeBidSeries1, np.array(tradePriceBidSeries1)+500, s = 0.000005 * np.array(tradeVolumeBidSeries) ** 2, label = "BID - SP")
ax.scatter(tradeTimeAskSeries1, np.array(tradePriceAskSeries1)+500, s = 0.000005 * np.array(tradeVolumeAskSeries) ** 2 ,label = "ASK - SP")

plt.legend()
plt.show()