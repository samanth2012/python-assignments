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

#cleaning empty cells
print(df.dropna) #returns new datafarame by removing empty cells
df.fillna(130) # replacing empty cells with the value "130"
dropna(inplace=True) #removes empty cells returns original DataFrame instead of returning a new one.


#cleaning wrong format
to_datetime() #method for converting a column into date formats?

#cleaning duplicates
df.drop_duplicates() --> removes duplicates
#correlation
df.corr()-->prints correlation matrix

#Plotting
df.plot() -->plotting
df.plot(kind='scatter', x = 'Duration', y = 'Calories') --> scatter
df['Duration'].plot(kind='hist') --> --> histogram
