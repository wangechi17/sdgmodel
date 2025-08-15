import streamlit as st

# Page configuration
st.set_page_config(page_title="SDG Analysis Dashboard", layout="wide")

# Title
st.title("🌍 PROJECT DASHBOARD")

# Image and Intro side by side
col1, col2 = st.columns([1, 3])

with col1:
    st.image("ME.jpeg", caption="Abigail Wangeci Ndegwa", use_container_width=True)  # Replace with your image file

with col2:
    st.markdown("""
    ### 👩‍🎓 **Presented By:**  
    **Abigail Wangeci Ndegwa**

    ### 📚 **Project Title:**  
    _Regional & Indicator-Based Analysis of UN Sustainable Development Goals Using Machine Learning_

    ### 👨‍🏫 **Lecturer:**  
    **Peter Gachuki**

    ### 📝 **Overview:**  
    Welcome to the **SDG Analysis Dashboard**.  
    This platform explores **UN Sustainable Development Goals (SDGs)** data using **unsupervised machine learning (K-Means)**,  
    allowing for insightful clustering and analysis of global and regional performance.
    """)
