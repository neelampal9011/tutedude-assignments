import streamlit as st

st.title("Simple Sales Dashboard")
st.write("Showing monthly sales data")

months = ["January", "February", "March", "April"]

sales = {
    "January": 1200,
    "February": 1500,
    "March": 900,
    "April": 2000
}

selected_month = st.selectbox("Select Month", months)

st.subheader("selected month sales")

st.write("Sales Value:", sales[selected_month])

st.subheader("monthly sales chart")
st.bar_chart(list(sales.values()))
