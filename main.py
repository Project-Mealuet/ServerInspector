from os import environ

from flask import Flask, jsonify, request

from modules.mc_status import mc_status
from modules.sys_status import sys_status

SECRET_KEY = environ['SECRET_KEY']

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


if __name__ == '__main__':
    app.run(host='localhost', port=25595)
