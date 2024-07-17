# frontend.py
import streamlit as st
import requests
import time

def get_data():
    response = requests.get('https://barelangmrt-monitoring.streamlit.app/')  # Adjust URL as needed
    if response.status_code == 200:
        return response.json()['data']
    else:
        return None

def main():
    st.title('Real-time Data Display')
    
    while True:
        data = get_data()
        if data:
            st.write('Received Data:', data)
        time.sleep(1)  # Polling interval

if __name__ == '__main__':
    main()
