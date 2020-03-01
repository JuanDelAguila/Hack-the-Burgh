import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset_price = pd.read_csv('market_data.csv')
dataset_price_sp = dataset_price.loc[dataset_price['Instrument'] == "SP-FUTURE"]
dataset_price_esx = dataset_price.loc[dataset_price['Instrument'] == "ESX-FUTURE"]

#print(dataset_train.head())
print(dataset_price_sp.head())
print(dataset_price_esx.head())