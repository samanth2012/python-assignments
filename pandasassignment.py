#Pandas Tutorial
data = {
  'calories': [420, 380, 390],
  'duration': [50, 40, 45]
}
df = pd.DataFrame(data)
print(df.loc[0])

#analyzing dataframes
import pandas as pd
df=pd.head(10) #print first 10 rows
print(df)
df1=pd.tail(10) #print last 10 rows
print(df)
