from bokeh.charts import Histogram, output_file,show 
from bokeh.plotting import figure, hplot, vplot, gridplot
from bokeh.sampledata.autompg import autompg as data

output_file("histogram.html")
hist = Histogram(data, "mpg", bins = 70, title = "Histogram",  color = "blue")
show(hist)