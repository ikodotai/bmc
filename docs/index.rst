.. rst-class:: hide-header


bmc
###


bmc is a Python 3 wrapper library for MinIO's command line interface `mc <https://github.com/minio/mc>`_ and `minio`. 
`MinIO <https://min.io>`_, an Amazon Simple Storage Service (S3) compatible object storage. It has a useful `Python client library <https://github.com/minio/minio-py>`_ which unfortunately lacks administrative capabilities that the `mc` and `minio` command line interfaces provide, such as adding users and hosts, which we need to do for the `iko <https://iko.ai>`_ machine learning platform. This library solves that `problem <https://github.com/minio/minio-py/issues/829>`_.

It has no external dependencies but assumes the presences of `mc` and `minio` command line interfaces.

.. toctree::
   :maxdepth: -1

   introduction
   api



Getting Started
---------------

::

  >>> import bmc

  >>> r = bmc.config_host_add(
  ...     alias='aliasforhost',
  ...     url='http://localhost:9000',
  ...     username='jhadjar',
  ...     password='soverysecret',
  ... )

  >>> r.content
  [{'status': 'success',
  'alias': 'aliasforhost',
  'URL': 'http://localhost:9000',
  'accessKey': 'jhadjar',
  'secretKey': 'soverysecret',
  'api': 's3v4',
  'lookup': 'auto'}]


.. raw:: html

    <script id="asciicast-8CTCfGKzCHHt7IaL7wNCvoyJe" src="https://asciinema.org/a/8CTCfGKzCHHt7IaL7wNCvoyJe.js" async></script>








