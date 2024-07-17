import streamlit as st
import requests
import time

def get_data():
    try:
        response = requests.get('http://localhost:5000/data')  # Adjust URL to your backend endpoint
        if response.status_code == 200:
            return response.json()['data']
        else:
            st.error(f'Error: {response.status_code}')
            return None
    except requests.exceptions.RequestException as e:
        st.error(f'Error: {e}')
        return None

def main():
    st.title('Real-time Data Display')
    
    while True:
        data = get_data()
        if data:
            st.write('Received Data:', data)
        time.sleep(5)  # Adjust polling interval as needed

if __name__ == '__main__':
    main()
