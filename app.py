
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Sales Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Sales Performance Dashboard")
st.caption("Business sales and profit analysis")

# Sample dataset
df = pd.DataFrame({
    "Month": [
        "Jan", "Feb", "Mar", "Apr", "May", "Jun",
        "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
    ],
    "Sales": [
        12000, 15000, 18000, 14000, 22000, 25000,
        21000, 28000, 30000, 26000, 35000, 40000
    ],
    "Profit": [
        2000, 3000, 4000, 2500, 5000, 6000,
        4500, 7000, 7500, 6500, 9000, 11000
    ]
})

total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
avg_sales = df["Sales"].mean()

col1, col2, col3 = st.columns(3)

col1.metric("Total Sales", f"${total_sales:,.0f}")
col2.metric("Total Profit", f"${total_profit:,.0f}")
col3.metric("Average Monthly Sales", f"${avg_sales:,.0f}")

st.divider()

left, right = st.columns(2)

with left:
    st.subheader("Monthly Sales")
    fig_sales = px.bar(
        df,
        x="Month",
        y="Sales",
        title="Sales by Month",
        text_auto=True
    )
    st.plotly_chart(fig_sales, use_container_width=True)

with right:
    st.subheader("Monthly Profit")
    fig_profit = px.line(
        df,
        x="Month",
        y="Profit",
        title="Profit Trend",
        markers=True
    )
    st.plotly_chart(fig_profit, use_container_width=True)

st.subheader("Sales Data Table")
st.dataframe(df, use_container_width=True)

st.info("This dashboard uses sample data. You can replace it with your real sales data later.")
