#Pandas Tutorial
data = {
  'calories': [420, 380, 390],
  'duration': [50, 40, 45]
}
df = pd.DataFrame(data)
print(df.loc[0])
