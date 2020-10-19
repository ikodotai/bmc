from ._utils import Command


def rb(**kwargs):
    '''Remove a bucket.

    Usage::

      >>> r = rb(target='s3/vacation-pictures')
      >>> r.content
      [{'status': 'success', 'bucket': 's3/vacation-pictures'}]
      >>> r = rb(target='s3/vacation-pictures-bis', region='us-east-1')
      >>> r.json
      '[{"status":"success","bucket":"s3/vacation-pictures-bis"}]'

    :param target: target bucket to remove, example: 's3/awesome-bucket'
    :param force: if set to ``True``, allows a recursive removal operation.
                  Defaults to ``False``.
    :param dangerous: if set to ``True``, allows site-wide removal of objects.
                  Defaults to ``False``.

    '''
    cmd = Command('mc {flags} rb {target}')
    return cmd(**kwargs)
