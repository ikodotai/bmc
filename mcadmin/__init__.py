'''BIGmama Platform Python SDK.'''

__version__ = '0.0.1'
__title__ = 'mcadmin'

from ._user import (
    user_list,
    user_add,
    user_remove,
    user_enable,
    user_disable,
    user_info,
)

from ._config import (
    host_add,
    host_list,
)

from ._ls import (
    ls_buckets_objects,
)
