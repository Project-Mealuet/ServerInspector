from os.path import join, exists

from flask import send_from_directory, jsonify

GAME_ROOT = '/home/ubuntu'


def server_meta(sub_path):
    full_path = join(GAME_ROOT, sub_path)
    if not exists(full_path):
        return jsonify({
            'name': '',
            'logo': '',
            'game_version': '',
            'mod_loader': ''
        })
    return send_from_directory(full_path, 'server_meta.json')
