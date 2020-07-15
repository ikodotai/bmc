from ._utils import Command


def config_host_add(**kwargs):
    '''Add an alias for the host storage.

    Usage ::

      >>> r = config_host_add(
          alias='aliasforost',
          url='http://localhost:9000',
          username='coolusername',
          password='soverysecret',
          )
      >>> r.content
      [{'status': 'success',
      'alias': 'aliasforhost',
      'URL': 'http://localhost:9000',
      'accessKey': 'coolusername',
      'secretKey': 'soverysecret',
      'api': 's3v4',
      'lookup': 'auto'}]
    '''
    cmd = Command('mc {flags} config host add {alias} {url} {username} {password}')
    return cmd(**kwargs)




def config_host_list(**kwargs):
    '''List hosts.

    Usage ::

      >>> r = config_host_list()
      >>> r.content
      [{'status': 'success',
        'alias': 'aliasforhost',
        'URL': 'http://localhost:9000',
        'accessKey': 'coolusername',
        'secretKey': 'soverysecret',
        'api': 's3v4',
        'lookup': 'auto'},
       {'status': 'success',
        'alias': 'coolname',
        'URL': 'http://localhost:9000',
        'accessKey': 'coolusername',
        'secretKey': 'soverysecret',
        'api': 's3v4',
        'lookup': 'auto'}]

      >>> r = config_host_list('coolname')
      >>> r.content
      [{'status': 'success',
        'alias': 'coolname',
        'URL': 'http://localhost:9000',
        'accessKey': 'coolusername',
        'secretKey': 'soverysecret',
        'api': 's3v4',
        'lookup': 'auto'}]
    '''
    kwargs.setdefault('alias', '')
    cmd = Command('mc {flags} config host list {alias}')
    return cmd(**kwargs)
