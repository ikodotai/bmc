from ._utils import Command


def ls(**kwargs):
    '''List buckets and objects.

    Usage::

      >>> r = ls()
      >>> r.content
      [{
       "status": "success",
       "type": "folder",
       "lastModified": "2020-06-01T12:25:04.163216097+01:00",
       "size": 4096,
       "key": "tests/",
       "etag": ""
      }
      {
       "status": "success",
       "type": "file",
       "lastModified": "2020-06-01T04:00:29.27764459+01:00",
       "size": 807,
       "key": "tox.ini",
       "etag": ""
      }]

      >>> r = ls(target='coolname', recursive=True)
      >>> r.content

    '''
    kwargs.setdefault('target', '')
    cmd = Command('mc ls {flags} {target}')
    return cmd(**kwargs)
