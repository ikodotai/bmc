.. _api:

API
===

.. module:: bmc

This documents the different functions and main objects for bmc.


mc ls
-----

.. autofunction:: ls


mc mb
-----

.. autofunction:: mb



mc rb
-----

.. autofunction:: rb


mc cp
-----

.. autofunction:: cp


mc group
--------

.. autofunction:: admin_group_add
.. autofunction:: admin_group_remove
.. autofunction:: admin_group_info
.. autofunction:: admin_group_list
.. autofunction:: admin_group_enable
.. autofunction:: admin_group_disable


mc policy
---------

.. autofunction:: admin_policy_add
.. autofunction:: admin_policy_remove
.. autofunction:: admin_policy_list
.. autofunction:: admin_policy_info
.. autofunction:: admin_policy_set


mc admin
--------

.. autofunction:: admin_user_list
.. autofunction:: admin_user_add
.. autofunction:: admin_user_remove
.. autofunction:: admin_user_enable
.. autofunction:: admin_user_disable
.. autofunction:: admin_user_info

mc bucket quota
--------
.. autofunction:: admin_bucket_quota_get
.. autofunction:: admin_bucket_quota_set


mc config
---------

.. autofunction:: config_host_add
.. autofunction:: config_host_list


minio server
------------

.. autofunction:: server


Command Object
--------------

.. autoclass:: bmc._utils.Command
   :members:
   :inherited-members:


Response Object
---------------

.. autoclass:: bmc._utils.Response
   :members:
   :inherited-members:

   .. attribute:: command
   .. attribute:: content
   .. attribute:: json
   .. attribute:: name
   .. attribute:: output
   .. attribute:: status