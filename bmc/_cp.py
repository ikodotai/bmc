from ._utils import Command


def cp(**kwargs):
    '''Copy objects.

    Usage::

      cp(source='Music/*.ogg', target='s3/jukebox/')
      cp(recursive=True, source='play/mybucket/burningman2011/', target='ts3/mybucket/')
      cp(recursive=True, backup/2014/ backup/2015/ play/archive/)
      cp(older_than='7d10h', source='play/mybucket/burningman2011/', target='s3/mybucket/')
      cp(newer_than='7d10h', source='play/mybucket/burningman2011/', target='~/latest/')
      cp(source='本語', target='s3/andoria/')
      cp(recursive=True, source='workdir/documents/May 2014/', target='s3/miniocloud')
      cp(recursive=True, encrypt_key="s3/documents/=32byteslongsecretkeymustbegiven1,myminio/documents/=32byteslongsecretkeymustbegiven2", source='s3/documents/', target='myminio/documents/')
      cp(recursive=True, encrypt_key="s3/documents/=MzJieXRlc2xvbmdzZWNyZWFiY2RlZmcJZ2l2ZW5uMjE=,myminio/documents/=MzJieXRlc2xvbmdzZWNyZWFiY2RlZmcJZ2l2ZW5uMjE=", source='s3/documents/', target='myminio/documents/')
      cp(attr="key1=value1;key2=value2", source='Music/*.mp4', target='play/mybucket/')
      cp(attr="Cache-Control=max-age=90000,min-fresh=9000;key1=value1;key2=value2", recursive=True, source='play/mybucket/burningman2011/', target='s3/mybucket/')
      cp(storage_class='REDUCED_REDUNDANCY', source='myobject.txt', target='play/mybucket')
      cp(recursive=True, continue=True, source='dir/', target='play/mybucket')
      cp(preserve=True, source='myobject.txt', target='play/mybucket')
      cp(retention_mode='governance', retention_duration='1d', source='locked.txt', target='play/locked-bucket/')
      cp(legal_hold='on', source='locked.txt', target='play/locked-bucket/')
      cp(disable_multipart=True, source='myobject.txt', target='play/mybucket')

    :param source: source object to copy, example filesystem: 'Music/*.mp4'
    :param target: target to copy to, example 's3/music'
    :param recursive: if set to ``True``, copy recursively. Defaults to ``False``.
    :param older_than: copy objects older than L days, M hours, and N minutes.

    :param newer_than: copy objects newer than L days, M hours, and N minutes.
    :param set_storage_class: set storage class for new object(s) on target.
    :param encrypt_value: if set to ``True``, encrypt/decrypt objects using
                          server-side encryption with server managed keys.
                          Defaults to ``False``.
    :param attr: add custom metadata for the object.


    :param continue: if set to ``True``, create or resume copy session
    :param preserve: if set to ``True``, preserve filesystem attributes for
                     mode, ownership, timestamps. Defaults to ``False``.
    :param disable_multipart: if set to ``True``, disable multipart upload
                              feature. Defaults to ``False``.
    :param md5: if set to ``True``, force all upload(s) to calculate md5sum
                checksum. Defaults to ``False``.


    :param retention_mode: retention mode to apply on the object (governance, compliance)
    :param retention_duration: retention duration for the object in d days or y years.
    :param recursive: if set to ``True``, copy recursively. Defaults to ``False``.
    :param older_than: copy objects older than L days, M hours, and N minutes.

    :param legal_hold: apply legal hold to the copied object (on, off)
    :param encrypt_key: encrypt/decrypt objects using server-side encryption
           with customer provided keys


    '''
    cmd = Command('mc {flags} cp {source} {target}')
    return cmd(**kwargs)
