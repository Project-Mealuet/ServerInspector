from os import environ

from dotenv import load_dotenv
from flask import Flask, jsonify, request
from flask_cors import CORS

from modules.mc_status import mc_status
from modules.sys_status import sys_status

load_dotenv()
SECRET_KEY = environ.get('SECRET_KEY')

app = Flask(__name__)
CORS(app)


@app.before_request
def check_key():
    received_key = request.headers.get('X-API-KEY')
    if not received_key or received_key != SECRET_KEY:
        return jsonify({'error': 'Invalid API key'}), 403


@app.route('/api/status/system', methods=['GET'])
def get_sys_status():
    return sys_status()


@app.route('/api/status/minecraft', methods=['GET'])
def get_mc_status():
    return mc_status()


if __name__ == '__main__':
    assert SECRET_KEY is not None, 'SECRET_KEY must be provided. '
    app.run(host='localhost', port=25595)
