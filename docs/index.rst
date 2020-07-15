.. rst-class:: hide-header


bmmc
####


bmmc is a Python wrapper for MinIO's command line interface. MinIO has a 
useful client library, but it lacks the capability to do some operations, such 
as configure hosts, or list users.

Getting Started
---------------

::

  >>> import bmmc

  >>> r = config_host_add(
  ...     alias='coolname',
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



.. toctree::
   :maxdepth: 2

   introduction
   api





