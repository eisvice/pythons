import pandas as pd
import matplotlib.pyplot as plt

hour = pd.read_csv('hour.csv')
print(hour.head())
# print(hour)
# print(hour['count'].mean())
# print(hour['count'].median())
# print(hour['count'].std())
# print(hour['count'].max())
# print(hour['count'].min())
# print(hour.describe())
print(hour.loc[0, 'count'])
print(hour.loc[2:4, 'registered'])
print(hour.loc[hour['hr']<5, 'registered'].mean())
print(hour.loc[(hour['hr']<5) & (hour['temp']<0.50), 'count'].mean())
print(hour.loc[(hour['hr']<5) & (hour['temp']>0.50), 'count'].mean())
print(hour.groupby(['season'])['count'].mean())
print(hour.groupby(['season','holiday'])['count'].mean())

# fig, ax = plt.subplots(figsize=(10,6))
# ax.scatter(x = hour['instant'], y = hour['count'])
# plt.xlabel("Hour")
# plt.ylabel("Count")
# plt.title("Ridership Count by Hour")
# plt.show()

hour_first48 = hour.loc[0:48,:]
# fig, ax = plt.subplots(figsize=(10,10))
# ax.scatter(x = hour_first48['instant'], y = hour_first48['count'])
# plt.xlabel("Hour")
# plt.ylabel("Count")
# plt.title("Count by Hour - First Two Days")
# plt.show()


fig, ax = plt.subplots(figsize=(10,10))
ax.plot(hour_first48['instant'], hour_first48['casual'], c = 'red', label = 'casual', linestyle = '-')
ax.plot(hour_first48['instant'], hour_first48['registered'], c = 'blue', label = 'registered', linestyle = '--')

ax.legend()
plt.show()