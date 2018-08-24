import sys #access to system parameters https://docs.python.org/3/library/sys.html
import pandas as pd #collection of functions for data processing and analysis modeled after R dataframes with SQL like features
import matplotlib #collection of functions for scientific and publication-ready visualization
import numpy as np #foundational package for scientific computing
import scipy as sp #collection of functions for scientific computing and advance mathematics
import sklearn #collection of machine learning algorithms
import matplotlib.pyplot as plt
import Visualization.api_get_data as api
import requests
plt.style.use('seaborn-whitegrid')
#To se more columns in output window
desired_width=320
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns',10)

#Read data
data_raw_station = pd.read_csv('C:/Users/UPS1FE/PycharmProjects/carFleet/dataset/example_sprit_cut_station.csv', sep=';')
data_raw_prices = pd.read_csv('C:/Users/UPS1FE/PycharmProjects/carFleet/dataset/example_sprit_cut_prices.csv', sep=';')

#to play with data we'll create a copy
data1 = data_raw_prices.copy(deep = True)
data2 = data_raw_station.copy(deep = True)
data_cleaner = [data1]

#preview data
#print(data_raw_prices.info())
#print (data_raw_station.info())

print('Columns with null values in price data set:\n', data1.isnull().sum())
print("-"*10)
print('Columns with null values in station data set:\n', data2.isnull().sum())
print("-"*10)

no_place = data2[data2['PLACE'].isnull()]
#print(no_place['NAME'])
#print("-"*10)
no_place = data2[data2['POST_CODE'].isnull()]
#print(no_place['NAME'])

#Deleting irrelevant columns and incomplete rows. I chose to delete rows because they were very less in number
drop_column = ['HOUSE_NUMBER']
data2.drop(drop_column, axis=1, inplace = True)
data2.drop([40, 135, 597, 711], inplace = True)
#print(data2.info())
#print("-"*10)
#print('Columns with null values in station data set:\n', data2.isnull().sum())

#Convert DATE_CHANGED
data1_copy = data1.copy(deep = True)
data1_copy['DATE_CHANGED'] = pd.to_datetime(data1_copy['DATE_CHANGED'])
data1_copy.index = data1_copy['DATE_CHANGED']
maxDf = data1_copy.resample('M').max()
minDf = data1_copy.resample('M').min()
print("Max value of Diesel per month \n", maxDf['DIESEL'])
print("Min value of Diesel per month \n", minDf['DIESEL'])
print("Max value of E5 per month /n", maxDf['E5'])
print("Min value of E5 per month /n", minDf['E5'])
print("Max value of E10 per month /n", maxDf['E10'])
print("Min value of E10 per month /n", minDf['E10'])

#maxDf.drop([maxDf['STID'], maxDf['DATE_CHANGED'], maxDf['CHANGED']],inplace= True)
#print(maxDf.head())

no_brand = data2[data2['BRAND'].isnull()]
#print((no_brand['ID']).index)

data2_copy = data2.copy(deep = True)
data2_copy.drop((no_brand['ID']).index, inplace= True)
print(data1_copy.info())
print(data2_copy.info())
print('Total number of locations: ', len(data2.PLACE.unique()))
print('Total number of Brands: ', len(data2.BRAND.unique()))
print('Number of unique station in data2' ,len(data2.ID.unique()))
print('Number of unique station in data1' ,len(data1.STID.unique()))

data1_copy.groupBy


#fig = plt.figure()
#data1.plot(x='STID', y='E5')
#data1.plot(x='DATE_CHANGED', y='E5')
#data1.plot(x='STID', y='E10')
#data1.plot(x='STID', y='DIESEL')
data1_copy.plot(x='DATE_CHANGED', y='DIESEL')
data1_copy.plot(x='DATE_CHANGED', y='E5')
data1_copy.plot(x='DATE_CHANGED', y='E10')
plt.show()


'''
Using API call we can fill the missing data values
for i in (no_brand['ID']).values:
    id = 'i'
    try:
        api.getDetailData(id)
    except:
        print('Exception occur: ', sys.exc_info()[0])
        raise
'''