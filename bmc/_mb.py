from ._utils import Command


def mb(**kwargs):
    '''Make a bucket.

    Usage::

      >>> r = mb(target='s3/vacation-pictures')
      >>> r.content
      [{'status': 'success',
        'bucket': 's3/vacation-pictures',
        'region': ''}]
      >>> r = mb(target='s3/vacation-pictures-bis', region='us-east-1')
      >>> r.json
      '[{"status":"success","bucket":"s3/vacation-pictures-bis","region":""}]'

    :param target: where to create the bucket, example: 's3/awesome-bucket'
    :param region: bucket region. Defaults to 'us-east-1'
    :param with_lock: if set to ``True``, enable object lock
    '''
    cmd = Command('mc {flags} mb {target}')
    return cmd(**kwargs)
