.. _api:

API
===

.. module:: bmmc

This documents the different functions and main objects for bmmc.



mc admin
--------

.. autofunction:: admin_user_list
.. autofunction:: admin_user_add
.. autofunction:: admin_user_remove
.. autofunction:: admin_user_enable
.. autofunction:: admin_user_disable
.. autofunction:: admin_user_info

mc config
---------

.. autofunction:: config_host_add
.. autofunction:: config_host_list

mc ls
-----

.. autofunction:: ls

minio server
------------

.. autofunction:: server


Command Object
--------------

.. autoclass:: bmmc._utils.Command
   :members:
   :inherited-members:


Response Object
---------------

.. autoclass:: bmmc._utils.Response
   :members:
   :inherited-members:

   .. attribute:: command
   .. attribute:: content
   .. attribute:: json
   .. attribute:: name
   .. attribute:: output
   .. attribute:: status