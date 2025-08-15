import streamlit as st
import pandas as pd
import pycountry_convert as pc
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import joblib
import plotly.express as px
import requests

# ===============================
# CONFIG
# ===============================
st.set_page_config(page_title="SDG Analysis Dashboard", layout="wide")
SERPER_API_KEY = "5e085686e623ecb66d0def02dd304c16a5c41312"

# ===============================
# LOAD DATA
# ===============================
@st.cache_data
def load_data():
    return pd.read_csv("UN_SDG.csv")

df = load_data()

# ===============================
# REGION MAPPING
# ===============================
def get_region(country_name):
    try:
        country_code = pc.country_name_to_country_alpha2(country_name)
        continent_code = pc.country_alpha2_to_continent_code(country_code)
        return {
            'AF': 'Africa',
            'EU': 'Europe',
            'AS': 'Asia',
            'NA': 'North America',
            'SA': 'South America',
            'OC': 'Oceania'
        }.get(continent_code, None)
    except:
        return None

if "REGION_GROUP" not in df.columns:
    df["REGION_GROUP"] = df["REF_AREA_LABEL"].apply(get_region)

# ===============================
# INTERACTIVE MODEL
# ===============================
st.title("⚡ Interactive SDG Clustering Model")

col1, col2 = st.columns(2)
with col1:
    region_choice = st.selectbox("🌍 Select Region", sorted(df["REGION_GROUP"].dropna().unique()))
with col2:
    sdg_choice = st.selectbox("📊 Select SDG Indicator",
                              sorted(df[df["REGION_GROUP"] == region_choice]["INDICATOR_LABEL"].unique()))

# Filter and process
filtered_df = df[(df["REGION_GROUP"] == region_choice) & (df["INDICATOR_LABEL"] == sdg_choice)]

if filtered_df.empty:
    st.warning(f"No data for {region_choice} and {sdg_choice}")
else:
    numeric_cols = filtered_df.select_dtypes(include=['number']).columns.tolist()
    filtered_df = filtered_df.dropna(subset=numeric_cols)

    scaler = StandardScaler()
    data_scaled = scaler.fit_transform(filtered_df[numeric_cols])

    pca = PCA(n_components=2)
    pca_data = pca.fit_transform(data_scaled)

    numeric_df = pd.DataFrame({
        "PCA1": pca_data[:, 0],
        "PCA2": pca_data[:, 1],
        "Country": filtered_df["REF_AREA_LABEL"].values,
        "SDG_Value": filtered_df["OBS_VALUE"].values
    })

    kmeans = KMeans(n_clusters=3, random_state=42)
    numeric_df["Cluster"] = kmeans.fit_predict(numeric_df[["PCA1", "PCA2"]])

    joblib.dump(kmeans, "sdg_kmeans_model.pkl")
    joblib.dump(scaler, "scaler.pkl")

    # Plot clusters
    st.subheader("📊 PCA-based Cluster Visualization")
    fig = px.scatter(
        numeric_df, x="PCA1", y="PCA2",
        color=numeric_df["Cluster"].astype(str),
        hover_data=["Country", "SDG_Value"],
        title=f"SDG Clusters for {region_choice} - {sdg_choice}",
        color_discrete_sequence=px.colors.qualitative.Set1
    )
    st.plotly_chart(fig, use_container_width=True)

    # Rankings
    st.subheader("🏆 Country Rankings by SDG Value")
    st.dataframe(
        numeric_df[["Country", "SDG_Value", "Cluster"]]
        .sort_values(by="SDG_Value", ascending=False),
        use_container_width=True
    )

    # ===============================
    # AUTOMATIC SUGGESTIONS SECTION
    # ===============================
    st.markdown("---")
    st.subheader("💡 Suggested Actions to Improve Performance")

    def search_serper(query):
        url = "https://google.serper.dev/search"
        headers = {
            "X-API-KEY": SERPER_API_KEY,
            "Content-Type": "application/json"
        }
        payload = {"q": query}
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code == 200:
            results = response.json().get("organic", [])
            suggestions = [f"- [{r['title']}]({r['link']}): {r['snippet']}" for r in results[:5]]
            return "\n".join(suggestions) if suggestions else "No relevant suggestions found."
        else:
            return f"Error: {response.status_code}"

    suggestions_query = f"How can {region_choice} improve {sdg_choice} SDG performance"
    st.markdown(search_serper(suggestions_query))

    # ===============================
    # OPTIONAL CHATBOT SECTION
    # ===============================
    st.markdown("---")
    st.subheader("💬 Ask the Chatbot for More Help")

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    user_input = st.text_input("Type your question about SDG improvements:")

    if st.button("Send"):
        if user_input.strip():
            bot_reply = search_serper(user_input)
            st.session_state.chat_history.append(("You", user_input))
            st.session_state.chat_history.append(("Bot", bot_reply))

    for role, text in st.session_state.chat_history:
        if role == "You":
            st.markdown(f"**🧑 You:** {text}")
        else:
            st.markdown(f"**🤖 Bot:** {text}")
