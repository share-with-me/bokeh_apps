import numpy as np
from bokeh.io import hplot, vplot, gridplot
from bokeh.plotting import figure, output_file, show
output_file("trigo.html" , title = "trigonometric")

num_points = 200

x = np.linspace(0, 6*np.pi, num_points)
y = np.sin(x)

tool = "pan, reset, save, box_select, wheel_zoom, box_zoom"

plot1 = figure(title = "Sine", tools = tool)

plot1.circle(x,y,legend = "sin(x)", color = "red")
plot1.circle(x,2*y, legend = "2*sin(x)" , color = "blue")

x0 = np.linspace(0,6*np.pi , num_points)
y0 = np.cos(x)

plot2 = figure(title = "Cosine", tools = tool)

plot2.circle(x0,y0,legend = "cos(x)", color = "red")
plot2.circle(x0,2*y0, legend = "2*cos(x)" , color = "blue")

x1 = np.linspace(0,6*np.pi , num_points)
y1 = np.tan(x)

plot3 = figure(title = "Tangent", tools = tool)

plot3.circle(x1,y1,legend = "tan(x)", color = "red")
plot3.circle(x1,2*y1, legend = "2*tan(x)" , color = "blue")


graph = gridplot([[plot1,plot2] , [plot3,None]])
show(graph)
