import pandas as pd
import pandas_profiling as pdp

data = pd.read_csv('./data/data.csv',names=range(1,748))
df = data[6:]
df.loc['2017-07-16':'2020-07-19',[4,15]]
profile = pdp.ProfileReport(df)
profile.to_file("myoutputfile.html")

