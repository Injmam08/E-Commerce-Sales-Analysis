import streamlit as st
import pandas as pd
import plotly.express as px

# Load Data
@st.cache_data
def load_data():
    df = pd.read_csv('Sample - Superstore.csv', encoding='latin1')
    df['Order Date'] = pd.to_datetime(df['Order Date'])
    df['Ship Date'] = pd.to_datetime(df['Ship Date'])
    return df

df = load_data()

# Sidebar Filters
st.sidebar.header("Filter Data")
selected_segment = st.sidebar.multiselect("Segment", options=df['Segment'].unique(), default=df['Segment'].unique())
selected_category = st.sidebar.multiselect("Category", options=df['Category'].unique(), default=df['Category'].unique())

# Filter DataFrame
filtered_df = df[(df['Segment'].isin(selected_segment)) & (df['Category'].isin(selected_category))]

# Title
st.title("E-Commerce Sales Analysis Dashboard")

# KPIs
total_sales = filtered_df['Sales'].sum()
total_profit = filtered_df['Profit'].sum()
total_quantity = filtered_df['Quantity'].sum()
total_orders = filtered_df['Order ID'].nunique()

st.metric("Total Sales", f"${total_sales:,.2f}")
st.metric("Total Profit", f"${total_profit:,.2f}")
st.metric("Total Quantity Sold", total_quantity)
st.metric("Total Orders", total_orders)

# Sales Over Time
st.subheader("Sales Over Time")
sales_over_time = filtered_df.groupby('Order Date')['Sales'].sum().reset_index()
fig1 = px.line(sales_over_time, x='Order Date', y
