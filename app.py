from flask import Flask, jsonify
import time

app = Flask(__name__)

# Temporary in-memory storage
processed_data_store = {}

# Mock data for retrieval
mock_data = {
    "items": [
        {"id": 1, "name": "item1", "value": 10},
        {"id": 2, "name": "item2", "value": 20},
        {"id": 3, "name": "item3", "value": 30}
    ]
}

# Simulate data retrieval
@app.route('/fetch-data', methods=['GET'])
def fetch_data():
    time.sleep(2)  # Simulate network delay
    data = mock_data
    process_data(data)
    return jsonify({"message": "Data fetched and processed successfully"}), 200

# Process the data (e.g., convert text to uppercase)
def process_data(data):
    processed_data = {}
    for item in data["items"]:
        processed_data[item["id"]] = {
            "name": item["name"].upper(),
            "value": item["value"] * 2  # Example transformation: double the value
        }
    global processed_data_store
    processed_data_store = processed_data

# Retrieve the processed data
@app.route('/get-processed-data', methods=['GET'])
def get_processed_data():
    return jsonify(processed_data_store), 200

if __name__ == '__main__':
    app.run(debug=True)
