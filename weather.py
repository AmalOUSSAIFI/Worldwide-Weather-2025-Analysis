import pandas as pd
import numpy as np
data= pd.read_excel("worldwide_weather_2025.xlsx")
data.head()
data.info()
data.describe()
data["date"]= pd.to_datetime(data["date"])
data["day_of_week"]= pd.to_datetime(data["day_of_week"])
data["day_of_year"] =pd.to_datetime(data["day_of_year"])
data= data[data["apparent_temperature_max"].between(-50,60)]
data= data[data["apparent_temperature_min"].between(-50,60)]
data= data[data["temperature_2m_mean"].between(-50,60)]
data= data[data["temp_7d_avg"].between(-50,60)]
data= data[data["temp_lag_1"].between(-50,60)]
data= data[data["temp_lag_7"].between(-50,60)]
data= data[data["temp_range"].between(-50,60)]
data= data[data["temperature_2m_max"].between(-50,60)]
data= data[data["temperature_2m_mean"].between(-50,60)]
data= data[data["temperature_2m_min"].between(-50,60)]
data["rain_sum"]= data["rain_sum"].fillna(0)
#Temperature trends
import matplotlib.pyplot as plt

data.groupby("date")["temperature_2m_mean"].mean().plot()
plt.title("Global Average Tempreture_2025")
plt.show()
#Rainfall by continent/country
data.groupby("country")["rain_sum"].sum().sort_values(ascending=False).head(10)
#seasonal Analysis
data ["month"]= data["date"].dt.month
monthly_temp=data.groupby("month")["temperature_2m_mean"].mean()
monthly_temp.plot(kind="bar")
plt.title("Monthly Avg Temperature")
plt.show()
heatwaves=data[data["temperature_2m_mean"]>40]
flood_risk=data[data["rain_sum"]>100]
plt.scatter(data["longitude"],data["latitude"],cmap="hot",s=2)
plt.colorbar(label="temperature_2m_mean")
plt.show()
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

x= data[["precipitation_sum","high_wind_flag"]]
y=data["temperature_2m_mean"]

x_train, x_test, y_train,y_test=train_test_split(x,y,test_size=0.2)

model=LinearRegression()
model.fit(x_train,y_train)
data["rain_today"] = (data["rain_sum"]>0).astype(int)
import streamlit as st 
st.title("Global Weather Analysis 2025")
st.line_chart(data.groupby("date")["temperature_2m_mean"].mean())