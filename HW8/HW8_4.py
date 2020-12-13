import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpl_patches
import numpy as np

# 讀入資料
dfa = pd.read_csv(r'submission_complete.csv')
dfb = pd.read_csv(r'start_end.csv')
df = pd.merge(dfa, dfb, on='challenge', how='left')

# 轉換時間欄位
df['submit_time'] = pd.to_datetime(df.submit_time, format='%Y-%m-%d %H:%M:%S')
df['start_time'] = pd.to_datetime(df.start_time, format='%Y/%m/%d %H:%M:%S')
df['end_time'] = pd.to_datetime(df.end_time, format='%Y/%m/%d %H:%M:%S')
df['test_time'] = df.end_time - df.start_time
df['spend'] = df.submit_time - df.start_time

# 只分析早於截止時間之資料
df = df[df.submit_time < df.end_time]
df['problem'] = df['problem'].str[0:7]
'''------------------------------------------'''
# I - 繳交次數
df1 = df[df.status != 'Accepted'].groupby('problem').size()

# II - 各problem答對人數
df2 = df[['status', 'user', 'challenge', 'problem']].drop_duplicates()
df2 = df2[df2.status == 'Accepted'].groupby(['problem']).size()

# III - 各題答對者平均花費時間(天數)
df3 = df[df.status == 'Accepted']
df3['spend_hours'] = df3.spend.dt.total_seconds() / (60*60*24)
df3 = df3.groupby(['problem', 'user']).first()
df3 = df3.groupby('problem').mean()

# IV - 各題首位答對者花費時間(分鐘)
df4 = df[df.status == 'Accepted']
df4['spend_hours'] = df4.spend.dt.total_seconds() / 60
df4 = df4.groupby(['problem']).first()
df4 = df4.groupby('problem').mean()

'''------------繪圖囉------------'''
'''
各題答對人數圖
ig, ax = plt.subplots()
ax.barh(df2.index, df2)
ax.set_title('Figure1. "Accepter(s)" Per Problem')
ax.invert_yaxis()
ax.text(
    df2['HW4 (4)'],
    'HW4 (4)',
    int(df2['HW4 (4)']),
    color='red',
    fontweight='bold',
    va='center')
ax.text(
    df2['HW6 (3)'],
    'HW6 (3)',
    int(df2['HW6 (3)']),
    color='red',
    fontweight='bold',
    va='center')
ax.text(
    df2['HW7 (3)'],
    'HW7 (3)',
    int(df2['HW7 (3)']),
    color='red',
    fontweight='bold',
    va='center')
plt.show()'''

'''
各題繳交次數圖
plt.rcParams["font.family"] = "Cambria"
ig, ax = plt.subplots()
ax.barh(df1.index, df1)
ax.invert_yaxis()
ax.set_title('Figure2. "Non-Accept" Number Per Problem')
ax.text(
    df1['HW4 (4)'],
    'HW4 (4)',
    int(df1['HW4 (4)']),
    color='red',
    fontweight='bold',
    va='center')
ax.text(
    df1['HW7 (3)'],
    'HW7 (3)',
    int(df1['HW7 (3)']),
    color='red',
    fontweight='bold',
    va='center')
plt.show()
'''
'''
各題答對者平均花費時間'''
ig, ax = plt.subplots()
ax.barh(df3.spend_hours.index, df3.spend_hours)
ax.invert_yaxis()
ax.set_title('Figure4. Average Spent-Time(days) of "All Accepters" Per Problem')
ax.text(df3.spend_hours['HW4 (4)'],'HW4 (4)',
        int(df3.spend_hours['HW4 (4)']),color='red', fontweight='bold', va='center')
ax.text(df3.spend_hours['HW7 (3)'],'HW7 (3)',
        int(df3.spend_hours['HW7 (3)']),color='red', fontweight='bold', va='center')
plt.show()

'''
首位答對者花費時間
ig, ax = plt.subplots()
ax.barh(df4.spend_hours.index, df4.spend_hours)
ax.invert_yaxis()
ax.set_title('Figure3. Spent-Time(mins) of "First Accepter" Per Problem')
ax.text(df4.spend_hours['HW4 (4)'],'HW4 (4)',
        int(df4.spend_hours['HW4 (4)']),color='red', fontweight='bold', va='center')
ax.text(df4.spend_hours['HW7 (3)'],'HW7 (3)',
        int(df4.spend_hours['HW7 (3)']),color='red', fontweight='bold', va='center')
plt.show()'''