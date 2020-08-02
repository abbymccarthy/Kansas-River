import pandas as pd
import datetime
import csv
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
headers = ['Date','Water Levels (m)']

# field measurements
df = pd.read_csv('Field_measurements_m.CSV',names=headers)
# x axis values
x = df['Date']
# y axis values
y = df['Water Levels (m)']
# plot
plt.plot(x, y)
# naming the x axis 
plt.xlabel('Date') 
# naming the y axis 
plt.ylabel('Water Levels (m)')
# giving a title to my graph 
plt.title('Field Measurements')
# beautify the x-labels
plt.gcf().autofmt_xdate()
# function to show the plot
plt.show()

# KGS Index Well
df = pd.read_csv('KGS_Index_Well_m.CSV',names=headers)
# x axis values
x = df['Date']
# y axis values
y = df['Water Levels (m)']
# plot
plt.plot(x, y)
# naming the x axis 
plt.xlabel('Date') 
# naming the y axis 
plt.ylabel('Water Levels (m)')
# giving a title to my graph 
plt.title('Field Measurements')
# beautify the x-labels
plt.gcf().autofmt_xdate()
# function to show the plot
plt.show()

# USGS Daily Data
df = pd.read_csv('USGS_Daily_Data_m.CSV',names=headers)
# x axis values
x = df['Date']
# y axis values
y = df['Water Levels (m)']
# plot
plt.plot(x, y)
# naming the x axis 
plt.xlabel('Date') 
# naming the y axis 
plt.ylabel('Water Levels (m)')
# giving a title to my graph 
plt.title('USGS Daily Data')
# beautify the x-labels
plt.gcf().autofmt_xdate()
# function to show the plot
plt.show()
