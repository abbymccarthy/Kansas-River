import numpy as np
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
plt.plot(x, y, color='green') 
# naming the y axis 
plt.ylabel('Water Levels (m)')
# giving a title to my graph 
plt.title('Field Measurements')
#limiting number of ticks displayed on x axis <-- Apparently needs something?
ax = df.plot(x_compat=True)
ax.xaxis.set_major_locator(mdates.MonthLocator())
# function to show the plot
plt.show()

# KGS Index Well
df = pd.read_csv('KGS_Index_Well_m.CSV',names=headers)
# x axis values
x = df['Date']
# y axis values
y = df['Water Levels (m)']
# plot
plt.plot(x, y, color='purple') 
plt.ylabel('Water Levels (m)')
# giving a title to my graph 
plt.title('KGS Index Well')
#limiting number of ticks displayed on x axis
plt.MaxNLocator(10)
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
# naming the axis   
plt.ylabel('Water Levels (m)')
# giving a title to my graph 
plt.title('USGS Daily Data')
#limiting number of ticks displayed on x axis
plt.MaxNLocator(10)
# function to show the plot
plt.show()

#All lines on the same graph <-- looks weird right now
df = pd.read_csv('Field_measurements_m.CSV',names=headers)
x1 = df['Date']
y1 = df['Water Levels (m)']
plt.plot(x1, y1, color='green', label = "Field Measurements")
# line 2 points 
df = pd.read_csv('KGS_Index_Well_m.CSV',names=headers)
x2 = df['Date']
y2 = df['Water Levels (m)']
plt.plot(x2, y2, color='purple', label = "KGS Index Well")
# line 3 points 
df = pd.read_csv('USGS_Daily_Data_m.CSV',names=headers)
x3 = df['Date']
y3 = df['Water Levels (m)']
plt.plot(x3, y3, label = "USGS Daily Data")
# naming the y axis 
plt.ylabel('Water Levels (m)')
# giving a title to my graph 
plt.title('Well Data')
#limiting number of ticks displayed on x axis <-- Apparently needs something?
plt.MaxNLocator(10)
# plot legend
plt.legend() 
# function to show the plot
plt.show()

df.plot(figsize=(15,4))
plt.show()
df.plot(subplots=True, figsize=(15,6))
plt.show()


