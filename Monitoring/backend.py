# backend.py
from flask import Flask, jsonify
from flask_cors import CORS
import time

app = Flask(__name__)
CORS(app)

@app.route('/data', methods=['GET'])
def get_data():
    while True:
        # Generate dummy data 1-10 repeated
        data = list(range(1, 11))
        return jsonify({'data': data})
        time.sleep()  # Delay to simulate real-time update

if __name__ == '__main__':
    app.run(debug=True)
