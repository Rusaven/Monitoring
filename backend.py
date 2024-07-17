from flask import Flask, jsonify
from flask_cors import CORS
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "https://barelangmrt-monitoring.streamlit.app"}})  # Adjust origin as needed

scheduler = BackgroundScheduler()
data = list(range(1, 11))  # Dummy initial data

@app.route('/data', methods=['GET'])
def get_data():
    return jsonify({'data': data})

def update_data():
    global data
    # Update data (dummy logic)
    data = [(x + 1) % 10 + 1 for x in data]

scheduler.add_job(update_data, 'interval', seconds=5)  # Adjust interval as needed
scheduler.start()

if __name__ == '__main__':
    app.run(debug=True)
