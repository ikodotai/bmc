'''BIGmama Platform Python SDK.'''

__version__ = '0.0.1'
__title__ = 'mcadmin'

from .user import (
    user_list,
    user_add,
    user_remove,
    user_enable,
    user_disable,
    user_info,
)

del user