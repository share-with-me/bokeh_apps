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

output_file("fourier.html")
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

#We will stick to data from 5000 to 25000

plot = bokeh.charts.Line(data.loc[5000:25000,:],x = 't(s)', y =  'V(microV)', color = "blue")
show(plot)
