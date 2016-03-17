from bokeh.charts import Scatter, output_file, show
from bokeh.plotting import hplot, vplot, gridplot, figure
from bokeh.sampledata.autompg import autompg as data

scatter = Scatter(data, x = "mpg" , y = "hp" , color = "cyl",title = "Scatter Plot" , xlabel = "Miles per gallon",ylabel = "Hp",
	legend = "top_right")

output_file("scatter.html")

show(scatter)