import pandas as pd
import datetime
df = pd.read_excel(r'timetable.xlsx')
day = "Thursday"
for i in range(20):
    if df.loc[i][3] == day:
        x = df.loc[i][1]
        total = x.hour*60*60+x.minute*60
        print(total)
