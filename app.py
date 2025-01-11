from flask import Flask, request, jsonify
from binance.client import Client

app = Flask(__name__)

# Load the secret key from the generated file
with open(r"/home/leon/Desktop/generated_password.txt", 'r') as file:
    SECRET_KEY = file.read().strip()

@app.route('/endpoint', methods=['POST'])
def endpoint():
    # Check for the secret key in the request header
    provided_key = request.headers.get('Authorization')

    if provided_key == SECRET_KEY:
        data = request.json
        
        # Extract the Binance API key and secret key from the request data
        binance_api_key = data.get('binance_api_key')
        binance_secret_key = data.get('binance_secret_key')
        
        # Create a Binance client with the provided API key and secret key
        client = Client(binance_api_key, binance_secret_key)
        
        # Use the Binance client to perform trading operations
        # For example, to get the current price of BTCUSDT:
        price = client.get_symbol_ticker(symbol='BTCUSDT')
        print(f"Current price of BTCUSDT: {price['price']}")
        
        return jsonify({'message': 'Received', 'data': data}), 200
    else:
        return jsonify({'error': 'Unauthorized'}), 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)