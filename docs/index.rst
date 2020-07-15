.. rst-class:: hide-header


bmmc
####


bmmc is a Python wrapper for MinIO's command line interface `mc` and `minio`. 
MinIO has a useful client library which unfortunately lacks administrative capabilities, such as adding users and hosts, which we need to do for the `iko <https://iko.ai>`_ machine learning platform.

.. toctree::
   :maxdepth: -1

   introduction
   api



Getting Started
---------------

::

  >>> import bmmc

  >>> r = bmmc.config_host_add(
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

    <script id="asciicast-umJbbEZO0zb5SZliX1T2LMlxV" src="https://asciinema.org/a/umJbbEZO0zb5SZliX1T2LMlxV.js" async></script>








