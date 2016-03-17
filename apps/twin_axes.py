from bokeh.plotting import hplot, vplot, gridplot, figure, output_file, show
from bokeh.models import LinearAxis , Range1d
import numpy as np
x = np.arange(-2*np.pi , 2*np.pi , 0.2)
y = np.sin(x)

y2 = np.linspace(0,100, len(y))

output_file("twin_axes.html")

plot  = figure(x_range = (-7,7) , y_range = (-1.5, 1.5) , title = "Twin_Axes")
plot.circle(x,y, color = "green")

plot.extra_y_ranges = {"extra": Range1d(start=0, end=100)}
plot.circle(x, y2, color="red", y_range_name="extra")
plot.add_layout(LinearAxis(y_range_name="extra"), 'right')

show(plot)