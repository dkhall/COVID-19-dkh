import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt

# import US cases time series from JHU CSSE database
us_cases = pd.read_csv('csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv')

# time series dates (columns) as timestamps
dates = []
for ii in us_cases.columns[11:]:
    dates.append(dt.datetime.strptime(ii + ' 23:59', '%m/%d/%y %H:%M'))

# get county data
county_cases = us_cases[us_cases['Admin2']=='Middlesex'].sum().values[11:]
new_county_cases = county_cases[1:] - county_cases[:-1]
trailing_week_avg = \
    (new_county_cases[0:-6] + \
    new_county_cases[1:-5] + \
    new_county_cases[2:-4] + \
    new_county_cases[3:-3] + \
    new_county_cases[4:-2] + \
    new_county_cases[5:-1] + \
    new_county_cases[6:]) / 7

# plotting
plt.bar(dates[1:], new_county_cases, width=1)
plt.plot(dates[7:], trailing_week_avg, 'r-')
plt.ylim(bottom=0)
plt.show()