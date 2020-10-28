from ._utils import Command

__all__ = [
    'admin_group_add',
    'admin_group_remove',
    'admin_group_info',
    'admin_group_list',
    'admin_group_enable',
    'admin_group_disable',
]


def admin_group_add(**kwargs):
    '''Add users to a new or existing group.

    Usage:

      >>> r = admin_group_add(target='aliasforhost', group='admins', members=['rockstar', 'test'])
      >>> r.content
      {'status': 'success', 'groupName': 'admins', 'members': ['rockstar', 'test']}
    '''
    if not isinstance(kwargs['members'], str):
        kwargs['members'] = ' '.join(kwargs['members'])

    cmd = Command('mc {flags} admin group add {target} {group} {members}')

    return cmd(**kwargs)


def admin_group_remove(**kwargs):
    '''Remove group or members from a group.

    Usage::

      >>> r = admin_group_remove(target='aliasforhost', group='admins',
                                members=['rockstar', 'test'])
      >>> r.content
      {'status': 'success', 'groupName': 'admins', 'members': ['rockstar', 'test']}

      >>> r = admin_group_remove(target='local', group='admins')
      >>> r.content
      {'status': 'success', 'groupName': 'admins'}
    '''
    if 'members' not in kwargs:
        kwargs['members'] = ''
    elif not isinstance(kwargs['members'], str):
        kwargs['members'] = ' '.join(kwargs['members'])

    cmd = Command('mc {flags} admin group remove {target} {group} {members}')

    return cmd(**kwargs)


def admin_group_info(**kwargs):
    '''Display group info.

    Usage::

      >>> r = admin_group_info(target='aliasforhost', group='admins')
      >>> r.content
      {'status': 'success', 'groupName': 'admins', 'members': ['rockstar', 'test'],
      'groupStatus': 'enabled', 'groupPolicy': 'somePolicy'}
    '''
    cmd = Command('mc {flags} admin group info {target} {group}')
    return cmd(**kwargs)


def admin_group_list(**kwargs):
    '''Display list of groups.

    Usage::

      >>> r = admin_group_list(target='aliasforhost')
      >>> r.content
      {'status': 'success', 'groups': ['foo', 'bar', 'admins']}
    '''
    cmd = Command('mc {flags} admin group list {target}')
    return cmd(**kwargs)


def admin_group_enable(**kwargs):
    '''Enable a group.

    Usage::

      >>> r = admin_group_enable(target='aliasforhost', group='admins')
      >>> r.content
      {'status': 'success', 'groupName': 'admins', 'groupStatus': 'enabled'}
    '''
    cmd = Command('mc {flags} admin group enable {target} {group}')
    return cmd(**kwargs)


def admin_group_disable(**kwargs):
    '''Disable a group.

    Usage::

      >>> r = admin_group_disable(target='aliasforhost', group='admins')
      >>> r.content
      {'status': 'success', 'groupName': 'admins', 'groupStatus': 'disabled'}
    '''
    cmd = Command('mc {flags} admin group disable {target} {group}')
    return cmd(**kwargs)
