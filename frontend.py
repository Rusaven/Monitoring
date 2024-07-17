# frontend.py

import streamlit as st
import requests

# Fungsi untuk mengambil data dari backend
def fetch_data():
    url = 'http://localhost:5000/data'  # Ganti dengan URL backend yang sesuai
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        st.error(f'Error: {response.status_code}')

# Halaman utama Streamlit
def main():
    st.title('Monitoring Website')

    st.write('Data dari backend:')
    data = fetch_data()
    st.write(data)

if __name__ == '__main__':
    main()
