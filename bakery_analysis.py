# -*- coding: utf-8 -*-
"""Bakery Analysis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VXx4qWm-AvlFnRXYi92Q6mWpWioLSHuB
"""



"""#importing libraries

"""

import pandas as pd
import matplotlib.pyplot as plt

df= pd.read_csv("/content/Bakery.csv")
df.head(10)

"""#dataframe summary

"""

df.info()

"""#Description of the data in the DataFrame"""

df.describe()

"""#Data Cleaning

"""

if df.duplicated().sum() > 0:
    print('Duplicates are present')
else:
    print('No duplicates exist')

df.duplicated()

df.drop_duplicates(inplace = True)
df.head()

#checking if duplicates are dropped

if df.duplicated().any():
    print('Duplicates still exist')
else:
    print('No duplicates exist')

df

item_count = df["Items"].value_counts().reset_index()
print(item_count)

rename_columns = item_count.rename(columns = {'index':'item_list','items':'Frequency'})
print(item_count)

rename_columns = item_count.rename(columns = {'index':'item list','Items':'Frequency'})
print(rename_columns)

#ploting a horizontal bar
items = rename_columns["item list"]
frequency = rename_columns["Frequency"]

fig, ax = plt.subplots(figsize=(10, 50))
ax.barh(items, frequency)


ax.set_title('Item Frequency Analysis')
ax.set_xlabel('Frequency')
ax.set_ylabel('Items')

plt.show()

#Day frequency analysis
daypart_frequency = df['Daypart'].value_counts().reset_index()
print(daypart_frequency)

renamed_daypart = daypart_frequency.rename(columns = {'index':'Daypart','Daypart':'No of transactions'})
print(renamed_daypart)

#ploting a bar graph
day_part = renamed_daypart["Daypart"]
count = renamed_daypart["No of transactions"]

fig, ax = plt.subplots(figsize=(8, 6))
ax.bar(day_part, count)


ax.set_title('Daypart Analysis')
ax.set_xlabel('Daypart')
ax.set_ylabel(' Total No of Transactions')

plt.show()



df

#converting the DateTime column to determine data type
df['DateTime']=pd.to_datetime(df['DateTime'])

#create a date column
df['Date']=df['DateTime'].dt.date

#create Time column
df['Time']=df['DateTime'].dt.time

df

#determine specific date
start_date = '2016-10-30'
end_date = '2016-12-31'

#filter the dataset
filtered_df = df[(df['DateTime']>= start_date) & (df['DateTime']<= end_date)]

#calculate count of transactions in the filtered dataset
transaction_count = filtered_df.shape[0]

print('Total Number of transactions:',transaction_count)

import datetime

start_date = datetime.datetime.strptime('2016-10-30 09:58:11','%Y-%m-%d %H:%M:%S')
end_date = datetime.datetime.strptime('2017-09-04 15:04:24','%Y-%m-%d %H:%M:%S')
filtered_df = df[(df['DateTime']>= start_date) & (df['DateTime']<= end_date)]
transaction_count = len(filtered_df)

print('Total Number of transactions:',transaction_count)

#cummulative transaction growth over time

df['DateTime'] = pd.to_datetime(df['DateTime'])

df = df.sort_values('Date')

df['CumulativeCount'] = df['TransactionNo'].cumsum()

df

#creating the figure
fig,ax = plt.subplots(figsize = (10,6))

#fill our area with a color
ax.fill_between(df['Date'],df['CumulativeCount'], color='skyblue',alpha=0.7)

ax.plot(df['Date'],df['CumulativeCount'])

ax.set_title('cumulative transaction count over time')
ax.set_xlabel('Date')
ax.set_ylabel('Cummulative Count')
plt.xticks(rotation = 45)

df

#month sales analysis
df['Month'] = df['DateTime'].dt.month
df['Year'] = df['DateTime'].dt.year
monthly_sales = df.groupby(['Year','Month'])['TransactionNo'].sum().reset_index()

print(monthly_sales)

#separate monthly sales data for each year

sales_2016 = monthly_sales[monthly_sales['Year']==2016]
sales_2017 = monthly_sales[monthly_sales['Year']==2017]

#create and separate the bargraphs for each year
fig,(ax1,ax2)=plt.subplots(2,1,figsize=(10,10))

#Bar graphs for 2016 sales
ax1.bar(sales_2016['Month'],sales_2016['TransactionNo'])
ax1.set_xticks(range(1,13))
ax1.set_xticklabels(['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])
ax1.set_title('Month Sales Analysis - 2016')
ax1.set_xlabel('Month')
ax1.set_ylabel('Total Sales')

#Bar graphs for 2017 sales
ax2.bar(sales_2017['Month'],sales_2016['TransactionNo'])
ax2.set_xticks(range(1,13))
ax2.set_xticklabels(['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])
ax2.set_title('Month Sales Analysis - 2017')
ax2.set_xlabel('Month')
ax2.set_ylabel('Total Sales')

plt.tight_layout()

plt.show()

#sales trend analysis

sales_data = df[['DateTime','TransactionNo']]

sales_data.set_index('DateTime',inplace = True)

monthly_sales = sales_data.resample('M').sum()

plt.figure(figsize=(10,6))
plt.plot(monthly_sales.index,monthly_sales['TransactionNo'])
plt.title('Sales Trend Analysis')
plt.xlabel('Time')
plt.ylabel('Sales')

plt.show()