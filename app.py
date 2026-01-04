import streamlit as st
import pandas as pd

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------
st.set_page_config(
    page_title="Airline Traffic Analysis",
    layout="wide"
)

# --------------------------------------------------
# Custom CSS
# --------------------------------------------------
st.markdown("""
<style>
/* Main background */
.main {
    background-color: #f9fbfd;
}

/* Title */
h1 {
    color: #0b5ed7;
    text-align: center;
    font-weight: 700;
}

/* Section headers */
h2, h3 {
    color: #1f2937;
    margin-top: 30px;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #0b5ed7;
}
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] p,
section[data-testid="stSidebar"] span {
    color: white;
}

/* Content padding */
.block-container {
    padding: 2rem 3rem;
}

/* Image cards */
img {
    border-radius: 12px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.15);
    margin-bottom: 25px;
}

/* Footer */
.footer {
    text-align: center;
    color: gray;
    font-size: 14px;
    margin-top: 40px;
}
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# Title
# --------------------------------------------------
st.title("✈️ Airline Traffic Analysis Dashboard")
st.markdown(
    "This dashboard presents **Exploratory Data Analysis (EDA)** "
    "of airline traffic using passenger, freight, and mail data."
)

# --------------------------------------------------
# Load Dataset
# --------------------------------------------------
@st.cache_data
def load_data():
    return pd.read_csv("data/city_pairs.csv")

df = load_data()

# --------------------------------------------------
# Sidebar
# --------------------------------------------------
st.sidebar.header("📊 Dashboard Overview")
st.sidebar.metric("Total Rows", df.shape[0])
st.sidebar.metric("Total Columns", df.shape[1])

# --------------------------------------------------
# Dataset Preview
# --------------------------------------------------
st.subheader("📄 Dataset Preview")
st.dataframe(df.head(), use_container_width=True)

# --------------------------------------------------
# Visualizations
# --------------------------------------------------
st.markdown("---")
st.header("📈 Visual Insights")

st.subheader("Yearly Passenger Trend")
st.image("images/yearly_passenger_trend.png", use_container_width=True)

st.subheader("Passengers Over Time")
st.image("images/passengers_over_time.png", use_container_width=True)

st.subheader("Freight Over Time")
st.image("images/freight_over_time.png", use_container_width=True)

st.subheader("Mail Over Time")
st.image("images/mail_over_time.png", use_container_width=True)

st.subheader("Average Passengers by Month")
st.image("images/average_passengers_by_month.png", use_container_width=True)

st.subheader("Passengers vs Freight")
st.image("images/passengers_vs_freight.png", use_container_width=True)

st.subheader("Top Countries by Traffic")
st.image("images/top_countries.png", use_container_width=True)

st.subheader("Top Airports / Ports")
st.image("images/top_ports.png", use_container_width=True)

st.subheader("Correlation Heatmap")
st.image("images/correlation_heatmap.png", use_container_width=True)

# --------------------------------------------------
# Footer
# --------------------------------------------------
st.markdown("---")
st.markdown(
    '<div class="footer">'
    '✈️ Airline Traffic Analysis | Data Science Project<br>'
    '🛠 Python · Pandas · Matplotlib · Seaborn · Streamlit'
    '</div>',
    unsafe_allow_html=True
)
