import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
df = pd.read_csv('worldometer_data.csv')

country_deaths = df.groupby("Country/Region")["TotalDeaths"].sum().reset_index()

fig = px.choropleth(country_deaths, 
                    locations="Country/Region", 
                    locationmode="country names",
                    color="TotalDeaths",
                    title="COVID-19 Deaths by Country",
                    color_continuous_scale="Reds")
fig.show()

country_deaths.to_csv("country_deaths.csv", index=False)
fig.write_html("covid_deaths_map.html")