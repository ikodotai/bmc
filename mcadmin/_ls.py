import subprocess
from ._utils import make_json


def ls_buckets_objects(target='', flags='--json', recursive=False, **kwargs):
    '''List buckets and objects.

    Usage::

      >>> ls()
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

      >>> ls('coolname', recursive=True)
    '''
    recursive = '--recursive' if recursive else ''
    cmd = f'mc {flags} ls {recursive} {target}'.split()
    return make_json(subprocess.check_output(cmd))
