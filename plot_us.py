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
pop_us = us_deaths['Population'].values.sum()
deaths_ma = us_deaths[us_deaths['Province_State']=='Massachusetts'].sum().values[12:]
pop_ma = us_deaths[us_deaths['Province_State']=='Massachusetts']['Population'].values.sum()
deaths_pa = us_deaths[us_deaths['Province_State']=='Pennsylvania'].sum().values[12:]
pop_pa = us_deaths[us_deaths['Province_State']=='Pennsylvania']['Population'].values.sum()
deaths_nc = us_deaths[us_deaths['Province_State']=='North Carolina'].sum().values[12:]
pop_nc = us_deaths[us_deaths['Province_State']=='North Carolina']['Population'].values.sum()
deaths_fl = us_deaths[us_deaths['Province_State']=='Florida'].sum().values[12:]
pop_fl = us_deaths[us_deaths['Province_State']=='Florida']['Population'].values.sum()
deaths_tx = us_deaths[us_deaths['Province_State']=='Texas'].sum().values[12:]
pop_tx = us_deaths[us_deaths['Province_State']=='Texas']['Population'].values.sum()
deaths_ca = us_deaths[us_deaths['Province_State']=='California'].sum().values[12:]
pop_ca = us_deaths[us_deaths['Province_State']=='California']['Population'].values.sum()

# time series dates (columns) as timestamps
dates = []
for ii in us_confirmed.columns[11:]:
    dates.append(dt.datetime.strptime(ii + ' 23:59', '%m/%d/%y %H:%M'))

## confirmed cases over time (log scale)
#fig, ax = plt.subplots()
#
#plt.semilogy(dates[np.where(cases_us>0)[0][0]:], cases_us[cases_us>0], 'b.', ms=1)
#ax.annotate('Confirmed Cases: {:,}'.format(cases_us[-1]), (dates[-1]+dt.timedelta(days=1),
#    0.85*cases_us[-1]), color='blue', fontsize=9)
#
#plt.semilogy(dates[np.where(deaths_us>0)[0][0]:], deaths_us[deaths_us>0], 'r.', ms=1)
#ax.annotate('Deaths: {:,}'.format(deaths_us[-1]), (dates[-1]+dt.timedelta(days=1),
#    0.85*deaths_us[-1]), color='red', fontsize=9)
#
#ax.set_ylim([0.9,300e6])
#ax.xaxis.set_tick_params(rotation=45, labelsize=10)
#fig.subplots_adjust(bottom=0.18, right=0.73)
#ax.spines['right'].set_visible(False)
#ax.spines['top'].set_visible(False)
#plt.title('COVID-19 in the United States [source: JHU CSSE]', fontsize=10)
## plt.legend()
#plt.show()

# daily deaths + trailing average (US)
daily_deaths = deaths_us[1:] - deaths_us[:-1]
fig, ax = plt.subplots()
plt.bar(dates[1:], daily_deaths, width=1)
plt.plot(dates[7:], (daily_deaths[:-6]+daily_deaths[1:-5]+daily_deaths[2:-4]+daily_deaths[3:-3]+daily_deaths[4:-2]+daily_deaths[5:-1]+daily_deaths[6:])/7, 'r-', lw=2.5)
ax.xaxis.set_tick_params(rotation=45, labelsize=10)
fig.subplots_adjust(bottom=0.18)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
plt.ylabel('new reported deaths by day [source: JHU CSSE]')
plt.ylim(bottom=0)
plt.show()

# daily deaths + trailing average (MA)
daily_deaths = (deaths_ma[1:] - deaths_ma[:-1])/pop_ma
fig, ax = plt.subplots()
plt.bar(dates[1:], daily_deaths, width=1)
plt.plot(dates[7:], (daily_deaths[:-6]+daily_deaths[1:-5]+daily_deaths[2:-4]+daily_deaths[3:-3]+daily_deaths[4:-2]+daily_deaths[5:-1]+daily_deaths[6:])/7, 'r-', lw=2.5)
ax.xaxis.set_tick_params(rotation=45, labelsize=10)
fig.subplots_adjust(bottom=0.18)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
plt.ylabel('fraction of MA killed per day [source: JHU CSSE]')
plt.ylim(0,5e-5)
plt.show()

# daily deaths + trailing average (PA)
daily_deaths = (deaths_pa[1:] - deaths_pa[:-1])/pop_pa
fig, ax = plt.subplots()
plt.bar(dates[1:], daily_deaths, width=1)
plt.plot(dates[7:], (daily_deaths[:-6]+daily_deaths[1:-5]+daily_deaths[2:-4]+daily_deaths[3:-3]+daily_deaths[4:-2]+daily_deaths[5:-1]+daily_deaths[6:])/7, 'r-', lw=2.5)
ax.xaxis.set_tick_params(rotation=45, labelsize=10)
fig.subplots_adjust(bottom=0.18)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
plt.ylabel('fraction of PA killed per day [source: JHU CSSE]')
plt.ylim(0,5e-5)
plt.show()

# daily deaths + trailing average (NC)
daily_deaths = (deaths_nc[1:] - deaths_nc[:-1])/pop_nc
fig, ax = plt.subplots()
plt.bar(dates[1:], daily_deaths, width=1)
plt.plot(dates[7:], (daily_deaths[:-6]+daily_deaths[1:-5]+daily_deaths[2:-4]+daily_deaths[3:-3]+daily_deaths[4:-2]+daily_deaths[5:-1]+daily_deaths[6:])/7, 'r-', lw=2.5)
ax.xaxis.set_tick_params(rotation=45, labelsize=10)
fig.subplots_adjust(bottom=0.18)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
plt.ylabel('fraction of NC killed per day [source: JHU CSSE]')
plt.ylim(0,5e-5)
plt.show()

# daily deaths + trailing average (FL)
daily_deaths = (deaths_fl[1:] - deaths_fl[:-1])/pop_fl
fig, ax = plt.subplots()
plt.bar(dates[1:], daily_deaths, width=1)
plt.plot(dates[7:], (daily_deaths[:-6]+daily_deaths[1:-5]+daily_deaths[2:-4]+daily_deaths[3:-3]+daily_deaths[4:-2]+daily_deaths[5:-1]+daily_deaths[6:])/7, 'r-', lw=2.5)
ax.xaxis.set_tick_params(rotation=45, labelsize=10)
fig.subplots_adjust(bottom=0.18)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
plt.ylabel('fraction of FL killed per day [source: JHU CSSE]')
plt.ylim(0,5e-5)
plt.show()

# daily deaths + trailing average (TX)
daily_deaths = (deaths_tx[1:] - deaths_tx[:-1])/pop_tx
fig, ax = plt.subplots()
plt.bar(dates[1:], daily_deaths, width=1)
plt.plot(dates[7:], (daily_deaths[:-6]+daily_deaths[1:-5]+daily_deaths[2:-4]+daily_deaths[3:-3]+daily_deaths[4:-2]+daily_deaths[5:-1]+daily_deaths[6:])/7, 'r-', lw=2.5)
ax.xaxis.set_tick_params(rotation=45, labelsize=10)
fig.subplots_adjust(bottom=0.18)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
plt.ylabel('fraction of TX killed per day [source: JHU CSSE]')
plt.ylim(0,5e-5)
plt.show()

# daily deaths + trailing average (CA)
daily_deaths = (deaths_ca[1:] - deaths_ca[:-1])/pop_ca
fig, ax = plt.subplots()
plt.bar(dates[1:], daily_deaths, width=1)
plt.plot(dates[7:], (daily_deaths[:-6]+daily_deaths[1:-5]+daily_deaths[2:-4]+daily_deaths[3:-3]+daily_deaths[4:-2]+daily_deaths[5:-1]+daily_deaths[6:])/7, 'r-', lw=2.5)
ax.xaxis.set_tick_params(rotation=45, labelsize=10)
fig.subplots_adjust(bottom=0.18)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
plt.ylabel('new reported CA deaths by day [source: JHU CSSE]')
plt.ylim(0,5e-5)
plt.show()

# TODO curve fitting

# TODO heat map

