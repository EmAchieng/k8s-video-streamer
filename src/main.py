from flask import Flask, request, jsonify
from router import route_video

app = Flask(__name__)

@app.route('/')
def home():
    return "Smart Video Routing for CDN Optimization"

@app.route('/route', methods=['POST'])
def route():
    data = request.json
    if 'ip' not in data:
        return jsonify({'error': 'IP address is required'}), 400
    
    ip = data['ip']
    server = route_video(ip)
    return jsonify({'server': server})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
    