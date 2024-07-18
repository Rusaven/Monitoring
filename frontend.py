import streamlit as st
import requests
import time

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

st.title("Barelang MRT")
st.header("Real-time data display for monitoring system")
st.text("Fetching data from Flask backend ...")

backend_url = "http://127.0.0.1:5000/data"

placeholder = st.empty()

def fetch_data():
    response = requests.get(backend_url)
    if response.status_code == 200:
        data = response.json()
        placeholder.write(f"Data: {data}")
    else:
        placeholder.write("Failed to fetch data from backend.")

fetch_data()
st.experimental_rerun(interval=5000)
