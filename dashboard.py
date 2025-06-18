import streamlit as st
from scraper import scrape_jobs_from_remoteok
import pandas as pd

st.set_page_config(page_title="Job Aggregator", layout="wide")
st.title("🌍 Remote Job Listings Aggregator")
st.markdown("Live job data from [RemoteOK](https://remoteok.com)")

# ✅ Load data
df = scrape_jobs_from_remoteok()

# ✅ Show raw data
st.subheader("📋 Job Listings")
st.write(df)

# 🔍 Filter
job_filter = st.text_input("Filter jobs by keyword (e.g., Python, Frontend, Remote):")

if job_filter:
    df = df[df.apply(lambda row: job_filter.lower() in str(row).lower(), axis=1)]

# Show filtered jobs
if not df.empty:
    st.dataframe(df, use_container_width=True)
    st.download_button("📥 Download CSV", data=df.to_csv(index=False), file_name="jobs.csv")
else:
    st.warning("No jobs found. Try a different keyword.")
