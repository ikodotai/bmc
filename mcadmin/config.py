import subprocess
from ._utils import make_json


def host_add(alias, url, username, password, flags='--json', **kwargs):
    '''Add an alias for the host storage.

    Usage ::

      >>> host_add('coolname', 'http://localhost:9000', 'minio_access_key', 'minio_secret_key')
      [{'status': 'success',
      'alias': 'aliasforhost',
      'URL': 'http://localhost:9000',
      'accessKey': 'minio_access_key',
      'secretKey': 'minio_secret_key',
      'api': 's3v4',
      'lookup': 'auto'}]
    '''
    cmd = f'mc {flags} config host add {alias} {url} {username} {password}'.split()
    return make_json(subprocess.check_output(cmd))




def host_list(alias='', flags='--json', **kwargs):
    '''List hosts.

    Usage ::

      >>> host_list()
      [{'status': 'success',
        'alias': 'aliasforhost',
        'URL': 'http://localhost:9000',
        'accessKey': 'minio_access_key',
        'secretKey': 'minio_secret_key',
        'api': 's3v4',
        'lookup': 'auto'},
       {'status': 'success',
        'alias': 'coolname',
        'URL': 'http://localhost:9000',
        'accessKey': 'minio_access_key',
        'secretKey': 'minio_secret_key',
        'api': 's3v4',
        'lookup': 'auto'}]

      >>> host_list('coolname')
      [{'status': 'success',
        'alias': 'coolname',
        'URL': 'http://localhost:9000',
        'accessKey': 'minio_access_key',
        'secretKey': 'minio_secret_key',
        'api': 's3v4',
        'lookup': 'auto'}]
    '''
    cmd = f'mc {flags} config host list {alias}'.split()
    return make_json(subprocess.check_output(cmd))
