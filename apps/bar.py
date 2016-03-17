#Reference for data has been made with the dataset used in the user guide

from bokeh.plotting import figure, hplot, vplot, gridplot, output_file, show
from bokeh.charts import Bar
from bokeh.sampledata.autompg import autompg as data

bar = Bar(data, 'cyl' , values = 'mpg' , agg = "median",group = "origin", legend = "top_right",title = "Bar Graph" , bar_width = 0.5)
output_file("bar.html")

show(bar)