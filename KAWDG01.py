import numpy as np
import pandas as pd
import datetime as dt
import csv
import matplotlib.pyplot as plt
import os

# .csv files headers = ['Date','Water Levels (m)']

import matplotlib.dates as mdates
from matplotlib.dates import date2num , DateFormatter

# point code to the data.
cwd = os.chdir("/Users/abigailmccarthy/Desktop/the real desktop/thesis/KAW-DG-01_content/") 

field_data = pd.read_excel('Field_measurements.xlsx', parse_dates = ['Date'])

# figure handle to change properties more easily
field_data_fig = plt.figure(figsize = (15, 6))

plt.plot(field_data['Date'], field_data['Water Levels (m)'], color='green') 

# naming the y axis, giving title to graph
plt.ylabel('Water Levels (m)')
plt.title('Field Measurements')

field_data_fig.tight_layout() # <-- extends plot to the border of the figure window
# field_data_fig.savefig('Field Data.png', dpi = 300) # <-- to save figures as a .png file

plt.show()


#%% KGS Index Well Plot
kgs_data = pd.read_csv('KGS_Index_Well.CSV', parse_dates = ['Date'])

kgs_data_fig = plt.figure(figsize = (15,6))

plt.plot(kgs_data['Date'], kgs_data['Water Levels (m)'], color='purple') 

plt.ylabel('Water Levels (m)')
plt.title('KGS Index Well')
plt.xticks(rotation = 90)

plt.show()


#%% USGS Data Plot
usgs_data = pd.read_csv('USGS_Daily_Data.CSV', parse_dates=['Date'])

usgs_data_fig = plt.figure(figsize = (15,6))


plt.plot(usgs_data['Date'], usgs_data['Water Levels (m)']) 

plt.ylabel('Water Levels (m)')
plt.title('USGS Daily Data')

plt.show()


#%%
#stack three plots, (#rows,#columns,plot#)
plt.style.use('fivethirtyeight')
fig = plt.figure()
plt1 = fig.add_subplot(3,1,1)
plt2 = fig.add_subplot(3,1,2)
plt3 = fig.add_subplot(3,1,3)

field_data = pd.read_excel('Field_measurements.xlsx', parse_dates = ['Date'])
x1 = field_data['Date']
y1 = field_data['Water Levels (m)']
plt1.plot(x1, y1, color ='green')
plt1.set_title('Field Measurements')

kgs_data = pd.read_csv('KGS_Index_Well.CSV', parse_dates = ['Date'])
x2 = kgs_data['Date']
y2 = kgs_data['Water Levels (m)']
plt2.plot(x2, y2, color ='blue')
plt2.set_title('Index Well')

usgs_data = pd.read_csv('USGS_Daily_Data.CSV', parse_dates=['Date'])
x3 = usgs_data['Date']
y3 = usgs_data['Water Levels (m)']
plt3.plot(x3, y3, color ='purple')
plt3.set_title('USGS Daily Data')
fig.subplots_adjust(hspace=1,wspace=1)
plt.show()

#%%
#All lines on the same graph <-- looks weird right now

field_data = pd.read_excel('Field_measurements.xlsx', parse_dates = ['Date'])
x1 = field_data['Date']
y1 = field_data['Water Levels (m)']
plt.plot(x1, y1, color ='green', label = "Field Measurements")

kgs_data = pd.read_csv('KGS_Index_Well.CSV', parse_dates = ['Date'])
x2 = kgs_data['Date']
y2 = kgs_data['Water Levels (m)']
plt.plot(x2, y2, color ='blue', label = "KGS Index Well")

usgs_data = pd.read_csv('USGS_Daily_Data.CSV', parse_dates=['Date'])
x3 = usgs_data['Date']
y3 = usgs_data['Water Levels (m)']
plt.plot(x3, y3, color ='purple', label = "USGS Daily Data")
plt.show()

# naming the y axis 
plt.ylabel('Water Levels (m)')
# giving a title to my graph 
plt.title('Well Data')
#limiting number of ticks displayed on x axis <-- Apparently needs something?
plt.MaxNLocator(10)
plt.legend() 
plt.show()


