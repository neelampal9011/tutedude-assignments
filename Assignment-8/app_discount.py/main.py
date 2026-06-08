import streamlit as st

st.title("Price Calculator")

price = st.number_input("Enter original price:")
discount_percentage = st.slider("discount percentage", min_value=0, max_value=50, value=10)

if st.button("Calculate"):
    discount_amount = price * (discount_percentage / 100)
    final_price = price - discount_amount
    
    st.success(f"final price: {final_price}")
    
    comparison_data = [
        ["before", f"{price}"],
        ["after", f"{final_price}"]
    ]
    st.table(comparison_data)
