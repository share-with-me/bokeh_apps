from bokeh.plotting import figure, output_file, show
output_file("bokeh_start.html")
graph = figure()
graph.line([1,2,3,4,5],[3,6,2,4,2], line_width = 3, color = 'red')
graph.xaxis.axis_label = 'Demand'
graph.yaxis.axis_label = 'Supply'
show(graph)