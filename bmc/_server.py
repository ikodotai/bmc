'''MinIO server. Start object storage server'''

from ._utils import Command

__all__ = [

    'server',
]


def server(**kwargs):
    '''Start object storage server.

    Usage::

      >>> server(address=':9008', dir='/home/jugurtha/data')
    '''
    cmd = Command('minio {flags} server {dir}')
    return cmd(**kwargs)
