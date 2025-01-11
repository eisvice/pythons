import pandas as pd
import matplotlib.pyplot as plt
from sqlite3 import connect
import seaborn as sns

conn = connect('lazac.sqlite3')
playground_detail = pd.read_sql('SELECT * FROM customers_playgrounddetail WHERE playground_id = 3', conn)

print(playground_detail)

print(playground_detail['total_amount'].sum())

customers = pd.read_sql('SELECT * FROM customers_customer WHERE playground_id = 3 AND status = \'finished\' AND cost > 10', conn, parse_dates=True)
customers['start_time'] = pd.to_datetime(customers['start_time']).dt.tz_localize('UTC').dt.tz_convert('Europe/Moscow')
customers['time'] = pd.to_datetime(customers['start_time']).dt.hour
# customers['time'] = pd.Series(customers['time']).dt.hour

customers['date'] = pd.to_datetime(customers['start_time']).dt.date

print(customers.head())
print(customers.describe())
print(customers.loc[customers['cost']>9000])

# plt.plot(customers['id'], customers['cost'])
# plt.show()


cost_by_hour = customers.groupby(['date', 'time'])[['cost']].sum()
# cost_by_hour = cost_by_hour.reset_index()
# cost_by_hour.loc['----'] = None
# cost_by_hour.loc['total sum'] = cost_by_hour.sum()
print(f"{cost_by_hour}\nAll {cost_by_hour['cost'].sum()}")

print(customers.pivot_table(values='cost', index='date', columns='time', aggfunc='sum', margins=True))
print(customers.groupby(['time'])[['cost']].sum().T.rename(index={'cost': 'All'}))

total_sum = customers.groupby(['time'])[['cost']].sum().rename(columns={'cost': 'All'})
sum_sum = total_sum.sum()
total_sum = total_sum.T
total_sum['All'] = sum_sum
print(total_sum)

distribution_by_weekdays = customers
distribution_by_weekdays['weekday'] = pd.to_datetime(distribution_by_weekdays['start_time']).dt.day_name()
distribution_by_weekdays['weekday_n'] = pd.to_datetime(distribution_by_weekdays['start_time']).dt.weekday
print(distribution_by_weekdays)
# distribution_by_weekdays_grouped = distribution_by_weekdays.groupby(['weekday', 'time'])[['cost']].sum()
distribution_by_weekdays_grouped = distribution_by_weekdays.pivot_table(values='cost', columns='time', index=['weekday','weekday_n'], aggfunc='sum', margins=True)
print(distribution_by_weekdays_grouped.sort_index(level='weekday_n').droplevel('weekday_n'))
for_plot = distribution_by_weekdays.pivot_table(values='cost', columns='time', index=['weekday','weekday_n'], aggfunc='sum').sort_index(level='weekday_n').droplevel('weekday_n')

# plt.plot(for_plot.index, for_plot.columns)

# for time_cost in for_plot.index:
#     # plt.plot(for_plot[time_cost], for_plot[time_cost])
#     print(time_cost)
#     print(for_plot[time_cost])

#     plt.plot(time_cost, for_plot[time_cost])
print(len(for_plot.columns))
for i in range(len(for_plot.index)):
    plt.plot(for_plot.columns, for_plot.iloc[i,], label=for_plot.index[i])
plt.legend()
plt.show()
# print(distribution_by_weekdays_grouped[:-1].sort_index(key=lambda x: ))


cost_by_payment = customers.groupby('payment')[['cost']].sum()
cost_by_payment.loc['----'] = None
cost_by_payment.loc['total sum'] = cost_by_payment.sum()
print(cost_by_payment)

customers['bank'] = customers['bank'].fillna('no bank (cash)')
cost_by_bank = customers.groupby('bank')[['cost']].sum()
cost_by_bank.loc['----'] = None
cost_by_bank.loc['total sum'] = cost_by_bank.sum()
print(cost_by_bank)

# fig, ax = plt.subplots(figsize=(10,6))
# sns.boxplot(x = 'time', y = 'cost', data = cost_by_hour)
# plt.show()