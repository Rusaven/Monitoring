import streamlit as st
import requests

# URL backend yang diberikan oleh ngrok
backend_url = 'http://127.0.0.1:5000/data'

# Mendapatkan data dari backend
response = requests.get(backend_url)
data = response.json()

# Menampilkan data di frontend
st.title('Data Monitoring')
st.write('Sensor 1:', data['sensor1'])
st.write('Sensor 2:', data['sensor2'])
st.write('Sensor 3:', data['sensor3'])
