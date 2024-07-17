# app.py
import streamlit as st
import requests

def fetch_dummy_data():
    url = 'http://localhost:5000/get_dummy_data'  # Ganti dengan URL backend Anda
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def main():
    st.title('Dummy Data Display')

    # Fetch dummy data from backend
    dummy_data = fetch_dummy_data()

    if dummy_data:
        st.write('Temperature:', dummy_data['temperature'])
        st.write('Humidity:', dummy_data['humidity'])
        st.write('Pressure:', dummy_data['pressure'])
        st.write('Status:', dummy_data['status'])
    else:
        st.write('Failed to fetch data from backend.')

if __name__ == '__main__':
    main()
