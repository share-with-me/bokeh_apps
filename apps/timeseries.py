#Reference has been taken majorly from the user guide examples fot this python file

from collections import OrderedDict
import pandas as pd

from bokeh.charts import TimeSeries, show, output_file

AAPL = pd.read_csv(
    "http://ichart.yahoo.com/table.csv?s=AAPL&a=0&b=1&c=2000&d=0&e=1&f=2010",
    parse_dates=['Date'])
MSFT = pd.read_csv(
    "http://ichart.yahoo.com/table.csv?s=MSFT&a=0&b=1&c=2000&d=0&e=1&f=2010",
    parse_dates=['Date'])

xyvalues = OrderedDict(
    AAPL=AAPL['Adj Close'],
    Date=AAPL['Date'],
    MSFT=MSFT['Adj Close'],
)

tool = "resize, pan, wheel_zoom, box_select, box_zoom, save,reset"

output_file("timeseries.html" , title = "TimeSeries View")

p = TimeSeries(xyvalues, index = 'Date' , legend = True, title = "TimeSeries", tools = tool, ylabel = "Stock Price")

show(p)