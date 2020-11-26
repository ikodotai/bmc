from ._utils import Command

__all__ = [
    'admin_policy_add',
    'admin_policy_remove',
    'admin_policy_list',
    'admin_policy_info',
    'admin_policy_set',
]

POLICY_COMMAND = 'mc {flags} admin policy '


def admin_policy_add(**kwargs):
    '''Add new canned policy on MinIO.

    Usage::

      >>> r = admin_policy_add(target='aliasforhost', name='admins', file='/tmp/policy.json')
      >>> r.content
      {'status': 'success', 'policy': 'admins', 'isGroup': False}
    '''
    cmd = Command(POLICY_COMMAND + 'add {target} {name} {file}')

    return cmd(**kwargs)


def admin_policy_remove(**kwargs):
    '''Remove canned policy from MinIO.

    Usage::

      >>> r = admin_policy_remove(target='aliasforhost', name='admins')
      >>> r.content
      {'status': 'success', 'policy': 'admins', 'isGroup': False}
    '''
    cmd = Command(POLICY_COMMAND + 'remove {target} {name}')

    return cmd(**kwargs)


def admin_policy_list(**kwargs):
    '''List all policies on MinIO.

    Usage::

      >>> r = admin_policy_list(target='aliasforhost')
      >>> r.content
      [{'status': 'success', 'policy': 'diagnostics', 'isGroup': False},
      {'status': 'success', 'policy': 'readonly', 'isGroup': False},
      {'status': 'success', 'policy': 'writeonly', 'isGroup': False},
      {'status': 'success', 'policy': 'admins', 'isGroup': False}]
    '''
    cmd = Command(POLICY_COMMAND + 'list {target}')

    return cmd(**kwargs)


def admin_policy_info(**kwargs):
    '''Show info on a policy.

    Usage::

      >>> r = admin_policy_info(target='aliasforhost', name='admins')
      >>> r.content
      {'status': 'success',
      'policy': 'admins',
      'policyJSON': {'Version': '2012-10-17',
        'Statement': [{'Effect': 'Allow',
          'Action': ['s3:*'],
          'Resource': ['arn:aws:s3:::*']}]},
      'isGroup': False}
    '''
    cmd = Command(POLICY_COMMAND + 'info {target} {name}')

    return cmd(**kwargs)


def admin_policy_set(**kwargs):
    '''Set IAM policy on a user or group

    Usage::

      >>> r = admin_policy_set(target='aliasforhost', name='admins', user='rockstar')
      >>> r.content
      {'status': 'success',
      'policy': 'admins',
      'userOrGroup': 'rockstar',
      'isGroup': False}
    '''

    if {'user', 'group'}.issubset(kwargs.keys()):
        raise KeyError('Only one of user or group arguments can be set.')

    if 'group' in kwargs:
        cmd = Command(POLICY_COMMAND + 'set {target} {name} group={group}')
    else:
        cmd = Command(POLICY_COMMAND + 'set {target} {name} user={user}')

    return cmd(**kwargs)
