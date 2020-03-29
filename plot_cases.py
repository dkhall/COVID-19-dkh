import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt

# import confirmed cases time series from JHU CSSE database
ts_confirmed = pd.read_csv('csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')

# select local data
ts_confirmed_us = ts_confirmed[ts_confirmed['Country/Region'] == 'US']
ts_confirmed_cn = ts_confirmed[ts_confirmed['Country/Region'] == 'China']
ts_confirmed_jp = ts_confirmed[ts_confirmed['Country/Region'] == 'Japan']
ts_confirmed_sk = ts_confirmed[ts_confirmed['Country/Region'] == 'Korea, South']
ts_confirmed_it = ts_confirmed[ts_confirmed['Country/Region'] == 'Italy']
ts_confirmed_de = ts_confirmed[ts_confirmed['Country/Region'] == 'Germany']
ts_confirmed_es = ts_confirmed[ts_confirmed['Country/Region'] == 'Spain']
ts_confirmed_ch = ts_confirmed[ts_confirmed['Country/Region'] == 'Switzerland']

# parse and plot
cases_us = ts_confirmed_us.values[0][4:]
cases_cn = ts_confirmed_cn.sum().values[4:]
cases_jp = ts_confirmed_jp.values[0][4:]
cases_sk = ts_confirmed_sk.values[0][4:]
cases_it = ts_confirmed_it.values[0][4:]
cases_ch = ts_confirmed_ch.values[0][4:]
cases_de = ts_confirmed_de.values[0][4:]
cases_es = ts_confirmed_es.values[0][4:]

# time series dates (columns) as timestamps
dates = []
for ii in ts_confirmed.columns[4:]:
    dates.append(dt.datetime.strptime(ii + ' 23:59', '%m/%d/%y %H:%M'))

# plot country comparisons
fig, ax = plt.subplots()
plt.semilogy(dates[np.where(cases_cn>0)[0][0]:], cases_cn[cases_cn>0], 'r-')
plt.semilogy(dates[-1], cases_cn[-1], 'r.')
ax.annotate('China: {:,}'.format(cases_cn[-1]), (dates[-1]+dt.timedelta(days=1), 0.6*cases_cn[-1]), color='red', fontsize=9)

plt.semilogy(dates[np.where(cases_it>0)[0][0]:], cases_it[cases_it>0], 'g-')
plt.semilogy(dates[-1], cases_it[-1], 'g.')
ax.annotate('Italy: {:,}'.format(cases_it[-1]), (dates[-1]+dt.timedelta(days=1), 0.85*cases_it[-1]), color='green', fontsize=9)

plt.semilogy(dates[np.where(cases_us>0)[0][0]:], cases_us[cases_us>0], 'b-')
plt.semilogy(dates[-1], cases_us[-1], 'b.')
ax.annotate('US: {:,}'.format(cases_us[-1]), (dates[-1]+dt.timedelta(days=1), 1.00*cases_us[-1]), color='blue', fontsize=9)

#plt.semilogy(dates[np.where(cases_sk>0)[0][0]:], cases_sk[cases_sk>0], '.-', label='South Korea')
#plt.semilogy(dates[np.where(cases_jp>0)[0][0]:], cases_jp[cases_jp>0], '.-', label='Japan')
#plt.semilogy(dates[np.where(cases_de>0)[0][0]:], cases_de[cases_de>0], '.-', label='Germany')
#plt.semilogy(dates[np.where(cases_es>0)[0][0]:], cases_es[cases_es>0], '.-', label='Spain')

ax.set_ylim([0.9,3e5])
ax.xaxis.set_tick_params(rotation=45, labelsize=10)
fig.subplots_adjust(bottom=0.18, right=0.85)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
plt.ylabel('Confirmed COVID-19 Cases [source: JHU CSSE]')
plt.show()
