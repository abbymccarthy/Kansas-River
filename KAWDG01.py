import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

# .csv files headers = ['Date','Water Levels (m)']

# point code to the data.
cwd = os.chdir("/Users/abigailmccarthy/Desktop/the real desktop/thesis/KAW-DG-01_content/") 

field_data = pd.read_excel('Field_measurements.xlsx', parse_dates = ['Date'])

# figure handle to change properties more easily
field_data_fig = plt.figure(figsize = (15, 6))

plt.plot(field_data['Date'], field_data['Water Levels (m)'], color='green') 

plt.ylabel('Water Levels (m)')
plt.title('Field Measurements')

field_data_fig.tight_layout() # <-- extends plot to the border of the figure window
# field_data_fig.savefig('Field Data.png', dpi = 300) # <-- to save figures as a .png file
plt.show()

#%% KGS Index Well Plot
import pandas as pd

kgs_data = pd.read_csv('KGS_Index_Well.CSV', parse_dates = ['Date'])

kgs_data_fig = plt.figure(figsize = (15,6))

plt.plot(kgs_data['Date'], kgs_data['Water Levels (m)'], color='purple') 

plt.ylabel('Water Levels (m)')
plt.title('KGS Index Well')
plt.xticks(rotation = 90)

plt.show()

#%% 
#rolling mean filter for Index Well Plot
test_windows=kgs_data.iloc[:,1].rolling(20).mean()
test_windows.plot(figsize = (15,6), color='purple')
plt.ylabel('Water Levels (m)')
plt.title('KGS Index Well Filtered')
plt.xticks(rotation = 90)
plt.show()

#%% USGS Daily Data Plot
import pandas as pd

usgs_data = pd.read_csv('USGS_Daily_Data.CSV', parse_dates=['Date'])

usgs_data_fig = plt.figure(figsize = (15,6))

plt.plot(usgs_data['Date'], usgs_data['Water Levels (m)']) 

plt.ylabel('Water Levels (m)')
plt.title('USGS Daily Data Filtered')
plt.show()

#%% 
#rolling mean filter for Index Well Plot
test_windows=usgs_data.iloc[:,1].rolling(15).mean()
test_windows.plot(figsize = (15,6))
plt.ylabel('Water Levels (m)')
plt.title('USGS Daily Data')
plt.show()
#%%
#stack three plots, (#rows,#columns,plot#)
import matplotlib.pyplot as plt
import pandas as pd

plt.style.use('fivethirtyeight')
fig = plt.figure(figsize = (6, 8))
plt1 = fig.add_subplot(3,1,1)
plt2 = fig.add_subplot(3,1,2)
plt3 = fig.add_subplot(3,1,3)

field_data = pd.read_excel('Field_measurements.xlsx', parse_dates = ['Date'])
plt1.plot(field_data['Date'], field_data['Water Levels (m)'], color ='green')
plt1.set_title('Field Measurements')

kgs_data = pd.read_csv('KGS_Index_Well.CSV', parse_dates = ['Date'])
plt2.plot(kgs_data['Date'], kgs_data['Water Levels (m)'], color ='blue')
plt2.set_title('Index Well')

usgs_data = pd.read_csv('USGS_Daily_Data.CSV', parse_dates=['Date'])
plt3.plot(usgs_data['Date'], usgs_data['Water Levels (m)'], color ='purple')
plt3.set_title('USGS Daily Data')
fig.subplots_adjust(hspace=1,wspace=1)
plt.show()

#%%
#All lines on the same graph
import pandas as pd

# figure handle to change properties more easily
combined_fig = plt.figure(figsize = (15, 6))

plt.plot(field_data['Date'], field_data['Water Levels (m)'], color ='green', label = "Field Measurements")
plt.plot(kgs_data['Date'], kgs_data['Water Levels (m)'], color ='blue', label = "KGS Index Well")
plt.plot(usgs_data['Date'], usgs_data['Water Levels (m)'], color ='purple', label = "USGS Daily Data")

#using rows from csv file or from dataframe (row 3260), bracket in this range
#plt.xlim(field_data.iloc[3260,0],field_data.iloc[3357,0])

# name y axis 
plt.ylabel('Water Levels (m)')
# title to my graph 
plt.title('Well Data')
plt.legend(loc='upper left', bbox_to_anchor=(0, 1.08)) 
combined_fig.savefig('Field Data.png', dpi = 300)


plt.show()

#%%
#convert Index Well hourly data to daily average
import pandas as pd
import os
cwd = os.chdir("/Users/abigailmccarthy/Desktop/the real desktop/thesis/KAW-DG-01_content/")

kgs_hourly = pd.read_excel('Index_well_hourly.xlsx', parse_dates = ['Date'])

data_columns=[kgs_hourly['Date'], kgs_hourly['Water Levels (m)']]
# Resample to daily frequency, aggregating with mean
kgs_hourly_mean = kgs_hourly[data_columns].resample('D').mean()
kgs_hourly_mean.head(24)
plt.show()









