from ._utils import Command

__all__ = [
    'admin_bucket_quota_get',
    'admin_bucket_quota_change'
]

QUOTA_COMMAND = 'mc {flags} admin bucket quota '


def admin_bucket_quota_get(**kwargs):
    '''Get quota of the bucket on MinIO.

    Usage::

      >>> r = admin_bucket_quota_get(target='aliasforhost', bucket_name='mybucket')
      >>> r.content
      {'status': 'success', 'bucket': 'bucket1', 'quota': 21474836480, 'type': 'hard'}
    '''
    cmd = Command(QUOTA_COMMAND + '{target}/{bucket_name}')

    return cmd(**kwargs)


def admin_bucket_quota_set(**kwargs):
    '''Set quota of the bucket on MinIO.

    Usage::

      >>> r = admin_bucket_quota_set(target='aliasforhost', bucket_name='mybucket', quota=1024)
      >>> r.content
      {'status': 'success', 'bucket': 'bucket1', 'quota': 1024, 'type': 'hard'}
    '''
    cmd = Command(QUOTA_COMMAND + '{target}/{bucket_name} --hard {quota}')

    return cmd(**kwargs)

