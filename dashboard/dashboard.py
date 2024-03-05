# Import Library
import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image

# Load Data
@st.cache_data
def load_data():
    data = pd.read_csv("https://raw.githubusercontent.com/107rasyid/Belajar-Analisis-Data-dengan-Python/main/dataset/day.csv")
    return data

# Title Dashboard
st.title("Bike Share Dashboard :bike:")
st.markdown("---")

# Load data
data = load_data()

# Sidebar
st.sidebar.title("Profil saya:")
st.sidebar.markdown("**• Nama: Rasyid Alfiansyah**")
st.sidebar.markdown("**• Email: [rasyidalfiansyh@gmail.com]**")
st.sidebar.markdown("**• github: [107rasyid](https://www.github.com/107rasyid)**")
st.sidebar.markdown("**• LinkedIn: [Rasyid Alfiansyah](https://www.linkedin.com/in/rasyid-alfiansyah-b61770217/)**")
st.sidebar.markdown("---")

# Visualization
st.header("Visualisasi Data")
# 1. Rata-rata jumlah sepeda yang disewakan (cnt) per jam pada hari kerja (workingday = 0) selama musim panas (season = 2) setiap tahunnya
# Calculate average count per hour per year
average_cnt_per_hour = data.groupby('yr')['cnt'].mean()
average_cnt_per_hour.index = ['2011', '2012']

# Visualize the data
fig = px.bar(average_cnt_per_hour, x=average_cnt_per_hour.index, y=average_cnt_per_hour.values,
             title='Rata-rata Jumlah Sepeda Disewakan per Jam pada Hari Kerja selama Musim Panas',
             labels={'x': 'Tahun', 'y': 'Rata-rata Jumlah Sepeda Disewakan per Jam'})

# Remove unwanted ticks from x-axis
fig.update_layout(xaxis=dict(tickvals=[2011, 2012], ticktext=['2011', '2012']))

st.plotly_chart(fig)

# 2. Hubungan antara musim (season) dan jumlah sewa (cnt) pada tahun 2012
# Filter data for year 2012
data_2012 = data[data['yr'] == 1]

# Calculate average count per hour
season_cnt_2012 = data_2012.groupby('season')['cnt'].mean().reset_index()
season_cnt_2012['season_label'] = season_cnt_2012['season'].map({1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'})

# Visualize the data
fig_season_cnt_2012 = px.bar(season_cnt_2012, x='season_label', y='cnt', 
                             title='Rata-rata Jumlah Sepeda Disewakan per Musim pada Tahun 2012',
                             labels={'season_label': 'Musim', 'cnt': 'Jumlah sewa'})   
st.plotly_chart(fig_season_cnt_2012)

# 3. Pengaruh cuaca (weathersit) dengan jumlah sewa (cnt) selama musim gugur (season 3) pada tahun 2012
# Filter data for autumn season (season = 3) and year 2012 (yr = 1)
autumn_weather_2012 = data[(data['season'] == 3) & (data['yr'] == 1)]
autumn_weather_2012['weather_label'] = autumn_weather_2012['weathersit'].map({1: 'Cerah/Sedikit Awan', 2: 'Kabut/Berawan', 3: 'Hujan Ringan/Salju Ringan', 4: 'Hujan Lebat/Salju'})

# Visualize the data
fig_autumn_weather_2012 = px.box(autumn_weather_2012, x='weather_label', y='cnt', 
                                 title='Pengaruh Cuaca terhadap Jumlah Sewa Sepeda selama Musim Gugur 2012',
                                 labels={'weather_label': 'Cuaca', 'cnt': 'Jumlah sewa'})
    
st.plotly_chart(fig_autumn_weather_2012)

# 4. Korelasi antara kecepatan angin (windspeed) dan jumlah rental sepeda (cnt) selama musim dingin (season 4) pada tahun 2012
winter_2012 = data[(data['season'] == 4) & (data['yr'] == 1)]
fig_windspeed_cnt_winter_2012 = px.scatter(winter_2012, x='windspeed', y='cnt', 
                                           title='Korelasi antara Kecepatan Angin dan Jumlah Rental Sepeda selama Musim Dingin 2012',
                                           labels={'season_label': 'Musim', 'cnt': 'Jumlah sewa'})
st.plotly_chart(fig_windspeed_cnt_winter_2012)

# 5. Hubungan antara hari libur (holiday) dan jumlah sewa (cnt) pada tahun 2012
holiday_cnt_2012 = data[data['yr'] == 1].groupby('holiday')['cnt'].mean().reset_index()
holiday_cnt_2012['holiday_label'] = holiday_cnt_2012['holiday'].map({0: 'Bukan hari libur', 1: 'Hari Libur'})
fig_holiday_cnt_2012 = px.bar(holiday_cnt_2012, x='holiday_label', y='cnt', 
                              title='Rata-rata Jumlah Sepeda Disewakan selama Hari Libur pada Tahun 2012',
                              labels={'holiday_label': 'Libur', 'cnt': 'Jumlah sewa'})
st.plotly_chart(fig_holiday_cnt_2012)

# About
st.sidebar.title("About")
st.sidebar.info("Dashboard ini menampilkan visualisasi untuk sekumpulan data Bike Share. ")
st.sidebar.caption("Dibuat pada 5 Maret 2024")