import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
from bokeh.plotting import figure, show, gridplot, hplot, vplot
import bokeh.charts
from bokeh.io import output_file
import bokeh.charts.utils
import bokeh.models
import bokeh.palettes
import bokeh.plotting


output_file("zoomed_fourier.html")
data = pd.read_csv('data.csv' , comment = '#' , names = ['t(ms)', 'V(microV)'])
data.head()

#Starting at 0 instant time

data['t(ms)']-=data['t(ms)'].min()

#Conversion to seconds
data['t(ms)']/=1000
#Renaming the column name now
data = data.rename(columns = {'t(ms)':'t(s)'})

print('Number of samples = ', len(data))
print('Max time taken = ', data['t(s)'].max(), 's')


#Zooming the spikes , here we take the range of spikes as from 0.675 to 0.690

spikes = (0.675 < data['t(s)']) & (data['t(s)'] < 0.69)
plot = bokeh.charts.Line(data.loc[spikes,:],x = 't(s)', y =  'V(microV)', color = "blue")


show(plot)
