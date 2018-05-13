from alpha_vantage.timeseries import TimeSeries
import alphavantageapikey as key
from pprint import pprint
import time
ts = TimeSeries(key=key, output_format='pandas')
data, meta_data = ts.get_intraday(symbol='BLNK',interval='1min', outputsize='full')

starttime=time.time()
while True:
    pprint(data.tail(1))
    time.sleep(10.0 - ((time.time() - starttime) % 10.0))