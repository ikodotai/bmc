from ._utils import Command


def mb(**kwargs):
    '''Make a bucket.

    Usage::

      >>> r = mb(target='s3/newbucket')
      >>> r.content
      [{'status': 'success',
        'bucket': 's3/vacation-pictures',
        'region': ''}]
      >>> r.json
      >>> r = mb(target='s3/vacation-pictures', region='us-east-1')
      '[{"status":"success","bucket":"s3/vacation-pictures","region":""}]'

    :param target: where to create the bucket, example: 's3/awesome-bucket'
    :param region: bucket region. Defaults to 'us-east-1'
    :param with_lock: if set to ``True``, enable object lock
    '''
    cmd = Command('mc mb {flags} {target}')
    return cmd(**kwargs)
