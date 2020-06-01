import subprocess
import json


__all__ = [

    'user_list',
    'user_add',
    'user_remove',
    'user_enable',
    'user_disable',
    'user_info',

]

def make_json(subprocess_output):
    return json.loads('[' + subprocess_output.decode('utf-8').strip('\n').replace('\n', ',') + ']')


def user_list(target, flags='--json', **kwargs):
    cmd = f'mc {flags} admin user list {target}'.split()
    return make_json(subprocess.check_output(cmd))


def user_add(target, username, password, flags='--json', **kwargs):
    cmd = f'mc {flags} admin user add {target} {username} {password}'.split()
    return make_json(subprocess.check_output(cmd))


def user_remove(target, username, flags='--json', **kwargs):
    cmd = f'mc {flags} admin user remove {target} {username} {password}'.split()
    return make_json(subprocess.check_output(cmd))


def user_enable(target, username, flags='--json', **kwargs):
    cmd = f'mc {flags} admin user enable {target} {username} {password}'.split()
    return make_json(subprocess.check_output(cmd))


def user_disable(target, username, flags='--json', **kwargs):
    cmd = f'mc {flags} admin user disable {target} {username}'.split()
    return make_json(subprocess.check_output(cmd))


def user_info(target, username, flags='--json', **kwargs):
    cmd = f'mc {flags} admin user info {target} {username}'.split()
    return make_json(subprocess.check_output(cmd))
