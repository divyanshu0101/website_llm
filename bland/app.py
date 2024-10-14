# from flask import Flask, request, jsonify, render_template
# import requests
# import pandas as pd

# app = Flask(__name__)

# # Define your API key and headers for authentication
# api_key = 'sk-ikt6gx4uzw6qgbwv1p4awihmbq1ko1ph0vugp9z69hmgj8ajuxzeui4dx81atqd569'  # Replace with your actual API key
# headers = {
#     "authorization": api_key,
#     "Content-Type": "application/json"
# }

# @app.route('/')
# def home():
#     return render_template('index.html')  # Serve the frontend

# @app.route('/send_calls', methods=['POST'])
# def send_calls():
#     data = request.get_json()
#     name = data['name']
#     phone_number = data['phone_number']

#     # Load the call list from a CSV file
#     df = pd.read_csv('CallD.csv')

#     # Prepare the payload
#     batch_payload = {
#         "base_prompt": "You're calling to speak with {{name}} about taking the feedback on how was their experience in the GENAI lab Gurugram...",
#         "call_data": [
#             {
#                 "phone_number": phone_number,
#                 "name": name,
#             }
#         ],
#         "transfer_list": {
#             "default": "+918872002090",
#         },
#         "model": "enhanced",
#         "wait_for_greeting": False,
#         "first_sentence": "Hi there, My name is RIDHA I'm calling about your visit to the GENAI lab of PWC in Gurgaon, am I speaking to {{name}}.",
#         "voice": "maya",
#         "reduce_latency": True,
#         "temperature": 0.7,
#         "test_mode": False,
#         "campaign_id": "LABB",
#         "label": "Testing-1"
#     }

#     # Sending the batch of calls
#     send_batch_url = "https://api.bland.ai/v1/batches"
#     response = requests.post(send_batch_url, json=batch_payload, headers=headers)
#     batch_response = response.json()

#     if batch_response.get('message') == 'success':
#         return jsonify({"status": "success", "batch_id": batch_response.get('batch_id')})
#     else:
#         return jsonify({"status": "failure", "message": response.text}), 400

# if __name__ == '__main__':
#     app.run(debug=True)




from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

# Define your API key and headers for authentication
api_key = 'sk-ikt6gx4uzw6qgbwv1p4awihmbq1ko1ph0vugp9z69hmgj8ajuxzeui4dx81atqd569'  # Replace with your actual API key
headers = {
    "authorization": api_key,
    "Content-Type": "application/json"
}

@app.route('/')
def home():
    return render_template('index.html')  # Serve the frontend

@app.route('/send_calls', methods=['POST'])
def send_calls():
    data = request.get_json()
    name = data['name']
    phone_number = data['phone_number']

    # Prepare the payload for the Bland AI API call
    batch_payload = {
        "base_prompt": "You're calling to speak with {{name}} about giving them some insights as to what is Generative AI , how it works and what all are the use cases that can or are being used.",
        "call_data": [
            {
                "phone_number": phone_number,
                "name": name,
            }
        ],
        "transfer_list": {
            "default": "+919464612886",  # Replace with your transfer number
        },
        "model": "enhanced",
        "wait_for_greeting": False,
        "first_sentence": "Hi there, My name is RIDHA I'm calling about your visit to the GENAI lab of PWC in Gurgaon, am I speaking to {{name}}.",
        "voice": "maya",
        "reduce_latency": True,
        "temperature": 0.7,
        "test_mode": False,
        "campaign_id": "LABB",
        "label": "Testing-1"
    }

    # Sending the batch of calls
    send_batch_url = "https://api.bland.ai/v1/batches"
    response = requests.post(send_batch_url, json=batch_payload, headers=headers)
    batch_response = response.json()

    if batch_response.get('message') == 'success':
        return jsonify({"status": "success", "batch_id": batch_response.get('batch_id')})
    else:
        return jsonify({"status": "failure", "message": response.text}), 400

if __name__ == '__main__':
    app.run(debug=True)
      
