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

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Sales", f"${total_sales:,.2f}")
col2.metric("Total Profit", f"${total_profit:,.2f}")
col3.metric("Quantity Sold", total_quantity)
col4.metric("Total Orders", total_orders)

# Sales Over Time
st.subheader("Sales Over Time")
sales_over_time = filtered_df.groupby('Order Date')['Sales'].sum().reset_index()
fig1 = px.line(sales_over_time, x='Order Date', y='Sales', title='Sales Over Time')
st.plotly_chart(fig1, use_container_width=True)

# Category-wise Sales
st.subheader("Sales by Category")
category_sales = filtered_df.groupby('Category')['Sales'].sum().reset_index()
fig2 = px.bar(category_sales, x='Category', y='Sales', color='Category', title='Sales by Category')
st.plotly_chart(fig2, use_container_width=True)

# Region-wise Profit
st.subh

