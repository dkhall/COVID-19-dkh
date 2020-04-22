import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt

# import confirmed cases time series from JHU CSSE database
us_confirmed = pd.read_csv('csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv')
us_deaths = pd.read_csv('csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_US.csv')

# parse and plot
cases_us = us_confirmed.sum().values[10:]
deaths_us = us_deaths.sum().values[11:]

# time series dates (columns) as timestamps
dates = []
for ii in us_confirmed.columns[11:]:
    dates.append(dt.datetime.strptime(ii + ' 23:59', '%m/%d/%y %H:%M'))

# plot country comparisons
fig, ax = plt.subplots()

plt.semilogy(dates[np.where(cases_us>0)[0][0]:], cases_us[cases_us>0], 'b.', ms=2)
ax.annotate('Confirmed Cases: {:,}'.format(cases_us[-1]), (dates[-1]+dt.timedelta(days=1),
    0.85*cases_us[-1]), color='blue', fontsize=9)

plt.semilogy(dates[np.where(deaths_us>0)[0][0]:], deaths_us[deaths_us>0], 'r.', ms=2)
ax.annotate('Deaths: {:,}'.format(deaths_us[-1]), (dates[-1]+dt.timedelta(days=1),
    0.85*deaths_us[-1]), color='red', fontsize=9)

ax.set_ylim([0.9,300e6])
ax.xaxis.set_tick_params(rotation=45, labelsize=10)
fig.subplots_adjust(bottom=0.18, right=0.75)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
plt.title('COVID-19 in the United States [source: JHU CSSE]', fontsize=10)
# plt.legend()
plt.show()


# select local data
# us_confirmed_us = us_confirmed[us_confirmed['Country/Region'] == 'US']

# TODO curve fitting

# TODO heat map

