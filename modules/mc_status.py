from mcipc.query import Client
from flask import jsonify


def mc_status():
    try:
        with Client('127.0.0.1', 25585) as client:
            full_status = client.stats(full=True)
            return jsonify({
                'host_name': full_status.host_name,
                'game_type': full_status.game_type,
                'game_id': full_status.game_id,
                'version': full_status.version,
                'plugins': full_status.plugins,
                'map': full_status.map,
                'host_port': full_status.host_port,
                'player': {
                    'num': full_status.num_players,
                    'max': full_status.max_players,
                    'list': full_status.players
                }
            })
    except ConnectionRefusedError:
        return {
            'host_name': '',
            'game_type': '',
            'game_id': '',
            'version': '',
            'plugins': [],
            'map': '',
            'host_port': 0,
            'player': {
                'num': 0,
                'max': 0,
                'list': []
            }
        }

