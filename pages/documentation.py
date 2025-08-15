import streamlit as st

# Page configuration
st.set_page_config(page_title="Project History", layout="wide")

# Page title
st.title("📜 Project History: Regional & Indicator-Based Analysis of UN SDGs Using Machine Learning")

# --- Problem Statement ---
st.header("Problem Statement")
st.write("""
Many nations have committed to achieving the United Nations Sustainable Development Goals (SDGs) by 2030. 
However, tracking and comparing progress across different countries and regions is challenging due to the vast amount 
of multi-dimensional data. Stakeholders often struggle to identify which countries are leading or lagging in specific 
goals, and decision-makers need clearer insights to focus their policies and resources effectively. Without a structured 
analysis, it’s difficult to spot performance clusters, trends, and regional disparities.
""")
st.image("sdg1.png", caption="Global SDG complexity and data gaps", use_container_width=True)

# --- Proposed Solution ---
st.header("Proposed Solution")
st.write("""
This project applies **unsupervised machine learning (K-Means clustering)** to categorize countries into performance groups 
based on their SDG indicator values. By grouping nations with similar patterns, it becomes easier to visualize trends, 
highlight leaders and laggards, and provide actionable insights for policy intervention.

The project also integrates interactive filtering by region and SDG indicator, allowing users to dynamically explore specific 
performance areas. Visualizations such as leaderboards, trend charts, and PCA-based cluster plots make the results 
accessible to a wide audience.
""")

# --- Data Sources ---
st.header("Data Sources")
st.write("""
- **UN SDG Global Database**: Official global dataset on Sustainable Development Goals indicators.
- Pre-processed and aggregated per country and per year for analysis.
- Cleaned and formatted for compatibility with machine learning models.
""")
st.image("datasetsource.png", caption="Sample of SDG dataset", use_container_width=True)
st.image("excel snippet.png", caption="Excel snippet", use_container_width=True)

# --- Exploratory Data Analysis (EDA) ---
st.header("Exploratory Data Analysis (EDA)")
st.write("""
1. **Data Inspection**: Loaded the dataset, checked structure, and identified available features.
""")
st.image("load dataset.png", caption="data inspection", use_container_width=True)
st.write("""
2. **Data Cleaning**: Checked for missing values, handled null entries, and removed anomalies.
""")
st.image("check missing values.png", caption="data cleaning", use_container_width=True)
st.write("""
3. **Outlier Analysis**: Detected and addressed data points that could skew model results.
""")
st.image("outlier1.png", caption="outliers", use_container_width=True)
st.image("outlier2.png", caption="outliers", use_container_width=True)
st.image("outlier3.png", caption="outliers", use_container_width=True)
st.image("outlier 4.png", caption="outliers", use_container_width=True)
st.write("""
4. **Indicator Review**: Listed all available SDG indicators and calculated baseline averages.
""")
st.image("indicators.png", caption="indicator", use_container_width=True)
st.write("""
5. **Global Trends**: Plotted SDG value trends globally over time.
""")
st.image("global trends.png", caption="Global SDG trend visualization", use_container_width=True)
st.write("""
6. **Country Focus**: Generated specific trend plots (e.g., Canada).
""")
st.image("canada case study.png", caption="Canada case study", use_container_width=True)
st.write("""
7. **Regional Leaderboards**: Computed average scores per country to compare performance.
""")

st.image("africa.png", caption="Africa trends", use_container_width=True)
st.image("north america.png", caption="North America trends", use_container_width=True)
st.image("south america.png", caption="South America trends", use_container_width=True)
st.image("ocenia.png", caption="Oceania trends", use_container_width=True)
st.image("europe.png", caption="Europe trends", use_container_width=True)
st.image("asia.png", caption="Asia trends", use_container_width=True)

# --- Model Training ---
st.header("Model Training")
st.write("""
- **StandardScaler**: Applied to normalize numeric features.
- **Principal Component Analysis (PCA)**: Reduced dimensionality for visualization while keeping patterns intact.
- **K-Means Clustering**: Grouped countries into 3 performance clusters.
- **Model Saving**: Stored model and scaler using `joblib` for reuse in the Streamlit app.
- **Interactive Exploration**: Enabled dynamic filtering by region and SDG indicator, with re-clustering on demand.
""")
st.image("cluster.png", caption="PCA-based clustering visualization", use_container_width=True)
