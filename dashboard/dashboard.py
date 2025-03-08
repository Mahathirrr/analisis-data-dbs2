import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

# Set page config
st.set_page_config(
    page_title="Bike Sharing Dashboard",
    page_icon="🚲",
    layout="wide"
)

# Load data
@st.cache_data
def load_data():
    hour_df = pd.read_csv('data/hour.csv')
    hour_df['dteday'] = pd.to_datetime(hour_df['dteday'])

    # Denormalize numerical columns
    hour_df['temp'] = hour_df['temp'] * 41
    hour_df['atemp'] = hour_df['atemp'] * 50
    hour_df['hum'] = hour_df['hum'] * 100
    hour_df['windspeed'] = hour_df['windspeed'] * 67

    # Map season values
    season_map = {1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'}
    hour_df['season'] = hour_df['season'].map(season_map)

    # Map weather values
    weather_map = {
        1: 'Clear',
        2: 'Mist',
        3: 'Light Snow/Rain',
        4: 'Heavy Rain/Snow'
    }
    hour_df['weathersit'] = hour_df['weathersit'].map(weather_map)

    return hour_df

# Load the data
df = load_data()

# Title
st.title('🚲 Bike Sharing Analysis Dashboard')
st.write('This dashboard shows the analysis of bike sharing data from 2011 to 2012')

# Sidebar filters
st.sidebar.header('Filters')

# Date range filter
date_range = st.sidebar.date_input(
    "Select Date Range",
    [df['dteday'].min(), df['dteday'].max()],
    min_value=df['dteday'].min(),
    max_value=df['dteday'].max()
)

# Season filter
season_filter = st.sidebar.multiselect(
    'Select Seasons',
    options=df['season'].unique(),
    default=df['season'].unique()
)

# Weather filter
weather_filter = st.sidebar.multiselect(
    'Select Weather Conditions',
    options=df['weathersit'].unique(),
    default=df['weathersit'].unique()
)

# Filter the data
filtered_df = df[
    (df['dteday'].dt.date >= date_range[0]) &
    (df['dteday'].dt.date <= date_range[1]) &
    (df['season'].isin(season_filter)) &
    (df['weathersit'].isin(weather_filter))
]

# Create two columns for KPIs
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Rentals", f"{filtered_df['cnt'].sum():,}")

with col2:
    st.metric("Average Daily Rentals", f"{filtered_df.groupby('dteday')['cnt'].mean().mean():.0f}")

with col3:
    st.metric("Registered Users", f"{filtered_df['registered'].sum():,}")

with col4:
    st.metric("Casual Users", f"{filtered_df['casual'].sum():,}")

# Create tabs for different visualizations
tab1, tab2 = st.tabs(["Temporal Analysis", "Weather Impact"])

with tab1:
    # Hourly pattern
    st.subheader("Hourly Rental Pattern")
    hourly_rentals = filtered_df.groupby('hr')['cnt'].mean().reset_index()
    fig_hourly = px.line(
        hourly_rentals,
        x='hr',
        y='cnt',
        title='Average Rentals by Hour of Day'
    )
    st.plotly_chart(fig_hourly, use_container_width=True)

    # Create two columns for seasonal and monthly patterns
    col1, col2 = st.columns(2)

    with col1:
        # Seasonal pattern
        st.subheader("Seasonal Pattern")
        seasonal_data = filtered_df.groupby('season')[['casual', 'registered']].mean().reset_index()
        fig_seasonal = px.bar(
            seasonal_data,
            x='season',
            y=['casual', 'registered'],
            title='Average Rentals by Season and User Type',
            barmode='group'
        )
        st.plotly_chart(fig_seasonal, use_container_width=True)

    with col2:
        # Monthly pattern
        st.subheader("Monthly Pattern")
        monthly_data = filtered_df.groupby('mnth')['cnt'].mean().reset_index()
        fig_monthly = px.line(
            monthly_data,
            x='mnth',
            y='cnt',
            title='Average Rentals by Month',
            markers=True
        )
        st.plotly_chart(fig_monthly, use_container_width=True)

with tab2:
    # Weather impact analysis
    col1, col2 = st.columns(2)

    with col1:
        # Weather situation impact
        st.subheader("Impact of Weather Situation")
        weather_impact = filtered_df.groupby('weathersit')['cnt'].mean().reset_index()
        fig_weather = px.bar(
            weather_impact,
            x='weathersit',
            y='cnt',
            title='Average Rentals by Weather Condition'
        )
        st.plotly_chart(fig_weather, use_container_width=True)

    with col2:
        # Temperature impact
        st.subheader("Impact of Temperature")
        fig_temp = px.scatter(
            filtered_df,
            x='temp',
            y='cnt',
            title='Rental Count vs Temperature',
            trendline="lowess"
        )
        st.plotly_chart(fig_temp, use_container_width=True)

    # Create two columns for humidity and windspeed impact
    col1, col2 = st.columns(2)

    with col1:
        # Humidity impact
        st.subheader("Impact of Humidity")
        fig_humidity = px.scatter(
            filtered_df,
            x='hum',
            y='cnt',
            title='Rental Count vs Humidity',
            trendline="lowess"
        )
        st.plotly_chart(fig_humidity, use_container_width=True)

    with col2:
        # Windspeed impact
        st.subheader("Impact of Wind Speed")
        fig_wind = px.scatter(
            filtered_df,
            x='windspeed',
            y='cnt',
            title='Rental Count vs Wind Speed',
            trendline="lowess"
        )
        st.plotly_chart(fig_wind, use_container_width=True)

# Footer
st.markdown("---")
st.markdown("Created with ❤️ by Muhammad Mahathir")