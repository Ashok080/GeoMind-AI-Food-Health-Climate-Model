import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title and description
st.set_page_config(page_title="GeoMind-AI: Food, Health, Climate Model")
st.title("🌍 GeoMind-AI: Food, Health & Climate Risk Prediction")
st.markdown("""
This project combines data from **MODIS**, **ECOSTRESS**, and **MIMIC-IV** 
to analyze:
- 🌾 Food insecurity risk  
- 🏥 ICU health conditions  
- 🌦️ Climate vulnerabilities  

Upload your data to begin prediction.
""")

# Upload section
st.header("📤 Upload CSV Data")
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success("✅ File uploaded successfully!")
    st.dataframe(df.head())

    # Basic analysis
    st.header("📊 Basic Statistics")
    st.write(df.describe())

    # Plotting example
    st.header("📈 Column-wise Plot")
    column = st.selectbox("Select column to plot", df.columns)
    plt.figure(figsize=(10, 4))
    plt.plot(df[column])
    plt.title(f"{column} Trend")
    st.pyplot(plt)

else:
    st.warning("Please upload a CSV file to continue.")

# Footer
st.markdown("---")
st.markdown("🔬 Built with NASA Data | ICU Records | ML Models")
