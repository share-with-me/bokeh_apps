from bokeh.plotting import figure, output_server, show
output_server("line")
p = figure(plot_width=400, plot_height=400)
# add a line renderer
p.line([5, 2, 3, 4, 5], [5, 7, 2, 4, 5], line_width=2)
show(p)