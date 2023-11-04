from os.path import join

from flask import send_from_directory

GAME_ROOT = '/home/ubuntu'


def server_meta(sub_path):
    full_path = join(GAME_ROOT, sub_path)
    return send_from_directory(full_path, 'server_meta.json')
