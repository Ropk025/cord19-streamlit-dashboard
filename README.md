# CORD-19 Streamlit Dashboard

This dashboard visualizes metadata from COVID-19 research papers using Streamlit. It helps explore trends in publication dates, journals, and authorship.

## 🔧 Tech Stack
- Python
- Streamlit
- pandas
- matplotlib

## 🚀 How to Run
```bash
streamlit run app.py


#### 🧠 `app.py`
```python
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("CORD-19 Metadata Dashboard")

# Load sample data
df = pd.read_csv("data/metadata_sample.csv")

# Show basic stats
st.write("Total papers:", len(df))
st.write("Top journals:", df['journal'].value_counts().head())

# Plot publication trends
df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
df['year'] = df['publish_time'].dt.year
yearly_counts = df['year'].value_counts().sort_index()

fig, ax = plt.subplots()
ax.plot(yearly_counts.index, yearly_counts.values)
ax.set_title("Publication Trends Over Time")
ax.set_xlabel("Year")
ax.set_ylabel("Number of Papers")
st.pyplot(fig)

