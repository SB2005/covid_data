import pandas as pd 
import plotly.express as px

df = pd.read_csv("covid_data.csv")
print(df[0:15])

fig = px.scatter(df, x="date", y="cases",color = "country")
fig.show()