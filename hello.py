import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
st.set_page_config(page_title="Sales Dashboard", page_icon=":bar_chart:")
st.title("sales performance dashboard")
data = {
    "Region": ["North", "South", "East", "West","North", "South", "East", "West"],
    "Sales": [200,150,None,300,250,None,220,280],
    "Profit": [50,40,30,None,60,35,None,70],
    "Category":["Electronics","Furniture","Clothing","Electronics","Furniture","Clothing","Electronics","Furniture"],
    
}
df = pd.DataFrame(data)
st.subheader("Raw Data")
st.write(df)
df.fillna(df.mean(numeric_only=True), inplace=True)
st.subheader("Cleaned Data")
st.write(df)
st.sidebar.header("Filters data")
region_filter = st.sidebar.multiselect("Select Region", options=df["Region"].unique(), default=df["Region"].unique())
filtered_df = df[df["Region"].isin(region_filter)]

#KPI's
total_sales=filtered_df["Sales"].sum()
total_profit=filtered_df["Profit"].sum()
col1,col2=st.columns(2)
col1.metric("Total Sales", f"{total_sales:.2f}")
col2.metric("Total Profit", f"{total_profit:.2f}")
#sales by category
st.subheader("Sales by Category")
cat_data = filter.groupby("Category")["Sales"].sum().reset_index()
fig,ax=plt.subplpots(figsize=(8,5))
ax.bar(cat_data.index,cat_data.values)
ax.set_title("Sales by Category")
ax.set_xlabel("Category")
ax.set_ylabel("Sales")
st.pyplot(fig)
#profit distribution
st.subheader("Profit Distribution")
fig2, ax2 = plt.subplots(figsize=(8,5))
ax2.pie(filtered_df["Profit"], labels=filtered_df["Region"], autopct='%1.1f%%', startangle=140)
ax2.set_title('Profit Distribution by Region')
st.pyplot(fig2)
#sales vs profit comparision
st.subheader("Sales vs profit comparision")
fig3, ax3 = plt.subplots(figsize=(8,5))
ax3.scatter(filtered_df["Sales"], filtered_df["Profit"], color='blue')
ax3.set_xlabel("Sales")
ax3.set_ylabel("Profit")
ax3.set_title("Sales vs Profit")
st.pyplot(fig3)



