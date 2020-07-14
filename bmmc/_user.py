'''Manage users. Command to add, remove, enable, disable, list users on MinIO server.'''

from ._utils import Command

__all__ = [

    'admin_user_list',
    'admin_user_add',
    'admin_user_remove',
    'admin_user_enable',
    'admin_user_disable',
    'admin_user_info',

]



def admin_user_list(**kwargs):
    '''List all users on MinIO.

    Usage::

      >>> admin_admin_user_list(target='aliasforhost')
      [{'status': 'success', 'accessKey': 'hellokitten', 'userStatus': 'enabled'},
       {'status': 'success', 'accessKey': 'jumanji', 'userStatus': 'enabled'},
       {'status': 'success', 'accessKey': 'rockstar', 'userStatus': 'enabled'},
       {'status': 'success', 'accessKey': 'test_access_key', 'policyName': 'readwrite', 'userStatus': 'enabled'}]
    '''
    cmd = Command(cmd_template='mc {flags} admin user list {target}')
    return cmd(**kwargs)


def admin_user_add(target, username, password, **kwargs):
    '''Add a new user on MinIO.

    Usage::

      >>> admin_user_add(target='aliasforhost', username='rockstar', password='verysecretpassword')
      [{'status': 'success',
        'accessKey': 'rockstar',
        'secretKey': 'verysecretpassword',
        'userStatus': 'enabled'}]
    '''
    cmd = Command('mc {flags} admin user add {target} {username} {password}')
    return cmd(**kwargs)


def admin_user_remove(target, username, **kwargs):
    '''Remove user on MinIO.

    Usage::

      >>> admin_user_remove('aliasforhost', 'hellokitten')
      [{
       'status': 'success',
       'accessKey': 'hellokitten'
      }]
    '''
    cmd = Command('mc {flags} admin user remove {target} {username}')
    return cmd(**kwargs)


def admin_user_enable(target, username, **kwargs):
    '''Enable a user on MinIO.

    Usage::

      >>> admin_user_enable('aliasforhost', 'rockstar')
      [{'status': 'success', 'accessKey': 'rockstar'}]
    '''
    cmd = Command('mc {flags} admin user enable {target} {username}')
    return cmd(**kwargs)


def admin_user_disable(target, username, **kwargs):
    '''Disable a user on MinIO.

    Usage::

      >>> admin_user_disable('aliasforhost', 'rockstar')
      [{'status': 'success', 'accessKey': 'rockstar'}]
    '''
    cmd = Command('mc {flags} admin user disable {target} {username}')
    return cmd(**kwargs)


def admin_user_info(target, username, **kwargs):
    '''Display info of a user.

    Usage::

      >>> admin_user_info('aliasforhost', 'rockstar')
      [{'status': 'success', 'accessKey': 'rockstar', 'userStatus': 'disabled'}]
    '''
    cmd = Command('mc {flags} admin user info {target} {username}')
    return cmd(**kwargs)
