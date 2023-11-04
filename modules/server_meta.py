from os.path import join, exists

from flask import send_from_directory, jsonify

GAME_ROOT = '/home/ubuntu/mealuet-serverpacks'


def server_meta(sub_path):
    full_path = join(GAME_ROOT, sub_path)
    if not exists(join(full_path, 'server_meta.json')):
        return jsonify({
            'name': '',
            'logo': '',
            'game_version': '',
            'mod_loader': ''
        })
    return send_from_directory(full_path, 'server_meta.json')
