import pandas as pd
from bokeh.io import io, vplot, hplot, gridplot,show

from bokeh.io import output_file as op
from bokeh.sampledata.glucose import data
from bokeh.models import BoxAnnotation
from bokeh.plotting import figure

op("Region.html" , title = "Vaue based regioning")

tool = "pan, wheel_zoom, box_zoom, box_select, reset, save"

data = data.ix['2010-10-06' : '2010-10-13']

plot = figure(x_axis_type = "datetime" , tools = tool)

plot.line(data.index.to_series() , data['glucose'], line_color = "black" , line_width = 2, legend = "glucose")

low_box = BoxAnnotation(plot=plot, top=80, fill_alpha=0.1, fill_color='blue')
mid_box = BoxAnnotation(plot=plot, bottom=80, top=180, fill_alpha=0.1, fill_color='green')
high_box = BoxAnnotation(plot=plot, bottom=180, fill_alpha=0.1, fill_color='red')

plot.renderers.extend([low_box, mid_box, high_box])
plot.title = "Glucose Region Range"

plot.xaxis.axis_label = 'Time'
plot.yaxis.axis_label = 'Value'

show(plot)