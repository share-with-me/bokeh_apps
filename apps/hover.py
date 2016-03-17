from bokeh.plotting import figure, output_file, show
from bokeh.models import HoverTool, BoxSelectTool

output_file("hover.html")

TOOLS = [BoxSelectTool(), HoverTool()]

plot = figure(tools = TOOLS, title = "Hover functionality")

plot.square([1,2,3,4], [2,4,6,8] , size = 15, color = "red", alpha = "0.6")
plot.xaxis.axis_label = "X"
plot.yaxis.axis_label = "Y"
show(plot)