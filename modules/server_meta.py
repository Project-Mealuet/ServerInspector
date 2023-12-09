from os.path import join, exists, dirname

from flask import send_from_directory, jsonify
from psutil import process_iter, NoSuchProcess, AccessDenied, ZombieProcess


def _find_absolute_jar_path_of_java_process(port):
    for proc in process_iter(['pid', 'name', 'cmdline', 'cwd']):
        try:
            if 'java' in proc.info['name'].lower():
                for conn in proc.connections(kind='inet'):
                    if conn.laddr.port == port:
                        for arg in proc.info['cmdline']:
                            if arg.endswith('.jar'):
                                absolute_jar_path = join(proc.info['cwd'], arg)
                                return proc.pid, absolute_jar_path
        except (NoSuchProcess, AccessDenied, ZombieProcess):
            pass
    return None, None


def server_meta():
    process_id, absolute_jar_path = _find_absolute_jar_path_of_java_process(25565)
    game_path = dirname(absolute_jar_path)
    print(game_path)
    print(join(game_path, 'server_meta.json'))
    if not exists(join(game_path, 'server_meta.json')):
        return jsonify({
            'name': '',
            'logo': '',
            'game_version': '',
            'mod_loader': ''
        })
    return send_from_directory(game_path, 'server_meta.json')
