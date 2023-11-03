from os import environ

from dotenv import load_dotenv
from flask import Flask, jsonify, request

from modules.mc_status import mc_status
from modules.sys_status import sys_status

load_dotenv()
SECRET_KEY = environ.get('SECRET_KEY')
ALLOWED_ORIGINS = ['https://mealuet.com', 'https://www.mealuet.com']

app = Flask(__name__)


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


@app.after_request
def add_cors_headers(response):
    origin = request.headers.get('Origin')
    if origin and origin in ALLOWED_ORIGINS:
        response.headers['Access-Control-Allow-Origin'] = origin
    response.headers['Access-Control-Allow-Headers'] = 'X-API-KEY'
    return response


if __name__ == '__main__':
    assert SECRET_KEY is not None, 'SECRET_KEY must be provided. '
    app.run(host='localhost', port=25595)
