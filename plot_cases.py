import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt

# import confirmed cases time series from JHU CSSE database
ts_confirmed = pd.read_csv('csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv')

# select local data
ts_confirmed_us = ts_confirmed[ts_confirmed['Country/Region'] == 'US']
ts_confirmed_cn = ts_confirmed[ts_confirmed['Country/Region'] == 'China']
ts_confirmed_jp = ts_confirmed[ts_confirmed['Country/Region'] == 'Japan']
ts_confirmed_sk = ts_confirmed[ts_confirmed['Country/Region'] == 'Korea, South']
ts_confirmed_it = ts_confirmed[ts_confirmed['Country/Region'] == 'Italy']
ts_confirmed_ch = ts_confirmed[ts_confirmed['Country/Region'] == 'Switzerland']
ts_confirmed_ma = ts_confirmed[ts_confirmed['Province/State'] == 'Massachusetts']
ts_confirmed_pa = ts_confirmed[ts_confirmed['Province/State'] == 'Pennsylvania']
ts_confirmed_nc = ts_confirmed[ts_confirmed['Province/State'] == 'North Carolina']
ts_confirmed_ca = ts_confirmed[ts_confirmed['Province/State'] == 'California']
ts_confirmed_va = ts_confirmed[ts_confirmed['Province/State'] == 'Virginia']
ts_confirmed_dc = ts_confirmed[ts_confirmed['Province/State'] == 'District of Columbia']
ts_confirmed_oh = ts_confirmed[ts_confirmed['Province/State'] == 'Ohio']
ts_confirmed_wv = ts_confirmed[ts_confirmed['Province/State'] == 'West Virginia']
ts_confirmed_ms = ts_confirmed[ts_confirmed['Province/State'] == 'Mississippi']

# parse and plot
cases_us = ts_confirmed_us.sum().values[4:]
cases_cn = ts_confirmed_cn.sum().values[4:]
cases_jp = ts_confirmed_jp.values[0][4:]
cases_sk = ts_confirmed_sk.values[0][4:]
cases_it = ts_confirmed_it.values[0][4:]
cases_ch = ts_confirmed_ch.values[0][4:]
cases_ma = ts_confirmed_ma.values[0][4:]
cases_pa = ts_confirmed_pa.values[0][4:]
cases_nc = ts_confirmed_nc.values[0][4:]
cases_ca = ts_confirmed_ca.values[0][4:]
cases_va = ts_confirmed_va.values[0][4:]
cases_dc = ts_confirmed_dc.values[0][4:]
cases_oh = ts_confirmed_oh.values[0][4:]
cases_wv = ts_confirmed_wv.values[0][4:]
cases_ms = ts_confirmed_ms.values[0][4:]

# time series dates (columns) as timestamps
dates = []
for ii in ts_confirmed.columns[4:]:
    dates.append(dt.datetime.strptime(ii + ' 23:59', '%m/%d/%y %H:%M'))

# plot country comparisons
fig, ax = plt.subplots()
plt.semilogy(dates[np.where(cases_cn>0)[0][0]:], cases_cn[cases_cn>0], 'r.-', label='China')
plt.semilogy(dates[np.where(cases_it>0)[0][0]:], cases_it[cases_it>0], '.-', label='Italy')
plt.semilogy(dates[np.where(cases_sk>0)[0][0]:], cases_sk[cases_sk>0], '.-', label='South Korea')
plt.semilogy(dates[np.where(cases_us>0)[0][0]:], cases_us[cases_us>0], 'b.-', label='US')
plt.semilogy(dates[np.where(cases_jp>0)[0][0]:], cases_jp[cases_jp>0], '.-', label='Japan')

ax.set_ylim([0.9,1.5e9])
ax.xaxis.set_tick_params(rotation=45, labelsize=10)
fig.subplots_adjust(bottom=0.18)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
plt.ylabel('Confirmed COVID-19 Cases [source: JHU CSSE]')
plt.legend(loc=2)
plt.show()

# plot various US states
fig, ax = plt.subplots()
plt.semilogy(dates[np.where(cases_us>0)[0][0]:], cases_us[cases_us>0], 'k.-', label='US')
plt.semilogy(dates[np.where(cases_ca>0)[0][0]:], cases_ca[cases_ca>0], 'm.-', label='California')
plt.semilogy(dates[np.where(cases_ma>0)[0][0]:], cases_ma[cases_ma>0], 'r.-', label='Massachusetts')
plt.semilogy(dates[np.where(cases_pa>0)[0][0]:], cases_pa[cases_pa>0], 'b.-', label='Pennsylvania')
plt.semilogy(dates[np.where(cases_nc>0)[0][0]:], cases_nc[cases_nc>0], 'c.-', label='North Carolina')

ax.set_ylim([0.9,330e6])
ax.xaxis.set_tick_params(rotation=45, labelsize=10)
fig.subplots_adjust(bottom=0.18)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
plt.ylabel('Confirmed COVID-19 Cases [source: JHU CSSE]')
plt.legend(loc=2)
plt.show()

# plot state and country cases
fig, ax = plt.subplots()
plt.semilogy(dates[np.where(cases_us>0)[0][0]:], cases_us[cases_us>0], 'b.-', label='US')
plt.semilogy(dates[np.where(cases_ch>0)[0][0]:], cases_ch[cases_ch>0], 'r.-', label='Switzerland')
plt.semilogy(dates[np.where(cases_ma>0)[0][0]:], cases_ma[cases_ma>0], '.-', label='Massachusetts')
plt.semilogy(dates[np.where(cases_oh>0)[0][0]:], cases_oh[cases_oh>0], '.-', label='Ohio')
plt.semilogy(dates[np.where(cases_va>0)[0][0]:], cases_va[cases_va>0], '.-', label='Virginia')
plt.semilogy(dates[np.where(cases_ms>0)[0][0]:], cases_ms[cases_ms>0], '.-', label='Mississippi')
plt.semilogy(dates[np.where(cases_dc>0)[0][0]:], cases_dc[cases_dc>0], '.-', label='Washington, DC')
plt.semilogy(dates[np.where(cases_wv>0)[0][0]:], cases_wv[cases_wv>0], '.-', label='West Virginia')

ax.set_ylim([0.9,330e6])
ax.xaxis.set_tick_params(rotation=45, labelsize=10)
fig.subplots_adjust(bottom=0.18)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
plt.ylabel('Confirmed COVID-19 Cases [source: JHU CSSE]')
plt.legend(loc=2)
plt.show()
