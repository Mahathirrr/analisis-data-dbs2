# Bike Sharing Analysis Project

## Setup environment

```bash
pip install -r requirements.txt
```

## Run steamlit dashboard

```bash
cd dashboard
streamlit run dashboard.py
```

## Project Organization

```
.
├── dashboard/
│   ├── dashboard.py
├── data/
│   ├── day.csv
│   └── hour.csv
├── proyek_analisis_data.ipynb
├── README.md
└── requirements.txt
```

## Project Structure

1. `dashboard.py`: The main dashboard application built with Streamlit
2. `proyek_analisis_data.ipynb`: Jupyter notebook containing the data analysis process
3. `requirements.txt`: List of Python packages required to run the project

## Features

1. Interactive dashboard with:
   - Date range filter
   - Season filter
   - Weather condition filter
   - Multiple visualizations for temporal and weather analysis
2. Comprehensive data analysis including:
   - Temporal patterns analysis
   - Weather impact analysis
   - RFM analysis
   - Detailed visualizations

## Data Analysis Process

The analysis follows these main steps:

1. Data Wrangling
   - Data gathering from CSV files
   - Data assessment for quality issues
   - Data cleaning and preparation
2. Exploratory Data Analysis (EDA)
   - Temporal pattern analysis
   - Weather impact analysis
3. Visualization & Explanatory Analysis
   - Creating insightful visualizations
   - Answering key business questions
4. Advanced Analysis
   - RFM Analysis for usage patterns

## Dashboard Features

The Streamlit dashboard provides:

1. Key Performance Indicators (KPIs)
   - Total rentals
   - Average daily rentals
   - Number of registered users
   - Number of casual users
2. Interactive Filters
   - Date range selection
   - Season filter
   - Weather condition filter
3. Visual Analysis
   - Temporal patterns (hourly, daily, monthly, seasonal)
   - Weather impact analysis
   - Temperature and humidity effects
   - Wind speed impact
