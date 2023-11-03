from flask import jsonify
from psutil import cpu_percent, virtual_memory, disk_usage


def sys_status():
    cpu_status = cpu_percent(interval=1)
    memory_status = virtual_memory()
    disk_status = disk_usage('/')

    return jsonify({
        'cpu_percent': cpu_status,
        'memory': {
            'total': memory_status.total,
            'used': memory_status.used,
            'percent': memory_status.percent
        },
        'disk': {
            'total': disk_status.total,
            'used': disk_status.used,
            'percent': disk_status.percent
        }
    })
