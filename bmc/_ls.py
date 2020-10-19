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

    :param target: target to list objects for. example: 's3/awesome-bucket'.
                   Defaults to an empty string '' to list the current working
                   directory.
    :param recursive: if set to ``True``, will recursively list objects.
                      Defaults to ``False``

    '''
    kwargs.setdefault('target', '')
    cmd = Command('mc {flags} ls {target}')
    return cmd(**kwargs)
