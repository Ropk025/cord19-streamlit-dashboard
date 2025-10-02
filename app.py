import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="CORD-19 Dashboard", layout="wide")
st.title("📊 CORD-19 Metadata Dashboard")

# Load sample data
DATA_PATH = "data/metadata_sample.csv"
df = pd.read_csv(DATA_PATH)

# Clean and prepare
df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
df['year'] = df['publish_time'].dt.year

# Sidebar filters
st.sidebar.header("🔍 Filters")
selected_year = st.sidebar.selectbox("Select Year", sorted(df['year'].dropna().unique()))
filtered_df = df[df['year'] == selected_year]

# Show stats
st.subheader(f"📅 Papers Published in {selected_year}")
st.write(f"Total papers: {len(filtered_df)}")

# Journal distribution
st.subheader("📰 Top Journals")
top_journals = filtered_df['journal'].value_counts().head(10)
st.bar_chart(top_journals)

# Publication trend
st.subheader("📈 Publication Trend Over Time")
yearly_counts = df['year'].value_counts().sort_index()
fig, ax = plt.subplots()
ax.plot(yearly_counts.index, yearly_counts.values, marker='o')
ax.set_xlabel("Year")
ax.set_ylabel("Number of Papers")
ax.set_title("CORD-19 Publication Trend")
st.pyplot(fig)
