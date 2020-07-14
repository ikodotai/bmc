'''Manage users. Command to add, remove, enable, disable, list users on MinIO server.'''

import subprocess
from ._utils import make_json

__all__ = [

    'user_list',
    'user_add',
    'user_remove',
    'user_enable',
    'user_disable',
    'user_info',

]


def user_list(target, flags='--json', **kwargs):
    '''List all users on MinIO.

    Usage::

      >>> user_list('aliasforhost')
      [{'status': 'success', 'accessKey': 'hellokitten', 'userStatus': 'enabled'},
       {'status': 'success', 'accessKey': 'jumanji', 'userStatus': 'enabled'},
       {'status': 'success', 'accessKey': 'rockstar', 'userStatus': 'enabled'},
       {'status': 'success', 'accessKey': 'test_access_key', 'policyName': 'readwrite', 'userStatus': 'enabled'}]
    '''
    cmd = f'mc {flags} admin user list {target}'.split()
    return make_json(subprocess.check_output(cmd))


def user_add(target, username, password, flags='--json', **kwargs):
    '''Add a new user on MinIO.

    Usage::

      >>> user_add('aliasforhost', 'rockstar', 'verysecretpassword')
      [{'status': 'success',
        'accessKey': 'rockstar',
        'secretKey': 'verysecretpassword',
        'userStatus': 'enabled'}]
    '''
    cmd = f'mc {flags} admin user add {target} {username} {password}'.split()
    return make_json(subprocess.check_output(cmd))


def user_remove(target, username, flags='--json', **kwargs):
    '''Remove user on MinIO.

    Usage::

      >>> user_remove('aliasforhost', 'hellokitten')
      [{
       'status': 'success',
       'accessKey': 'hellokitten'
      }]
    '''
    cmd = f'mc {flags} admin user remove {target} {username}'.split()
    return make_json(subprocess.check_output(cmd))


def user_enable(target, username, flags='--json', **kwargs):
    '''Enable a user on MinIO.

    Usage::

      >>> user_enable('aliasforhost', 'rockstar')
      [{'status': 'success', 'accessKey': 'rockstar'}]
    '''
    cmd = f'mc {flags} admin user enable {target} {username}'.split()
    return make_json(subprocess.check_output(cmd))


def user_disable(target, username, flags='--json', **kwargs):
    '''Disable a user on MinIO.

    Usage::

      >>> user_disable('aliasforhost', 'rockstar')
      [{'status': 'success', 'accessKey': 'rockstar'}]
    '''
    cmd = f'mc {flags} admin user disable {target} {username}'.split()
    return make_json(subprocess.check_output(cmd))


def user_info(target, username, flags='--json', **kwargs):
    '''Display info of a user.

    Usage::

      >>> user_info('aliasforhost', 'rockstar')
      [{'status': 'success', 'accessKey': 'rockstar', 'userStatus': 'disabled'}]
    '''
    cmd = f'mc {flags} admin user info {target} {username}'.split()
    return make_json(subprocess.check_output(cmd))
