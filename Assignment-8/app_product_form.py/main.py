import streamlit as st

st.title("Product Information")
st.sidebar.header("Product Input Form")
product_name = st.sidebar.text_input("Product name")

categories = ["electronics", "clothing", "books", "home & kitchen", "toys"]
category = st.sidebar.selectbox("Category", categories)
price = st.sidebar.number_input("Price")

if st.sidebar.button("Add product"):
    if product_name.strip() == "":
        st.error("enter product name")
    else:
        st.success("product added successfully")
        st.write(f"Name : {product_name}")
        st.write(f"Category : {category}")
        st.write(f"Price : {price}")





