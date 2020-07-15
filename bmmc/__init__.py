'''BIGmama Python wrapper for the MinIO command line interface.'''

__version__ = '0.0.1'
__title__ = 'bmmc'

from ._user import (
    admin_user_list,
    admin_user_add,
    admin_user_remove,
    admin_user_enable,
    admin_user_disable,
    admin_user_info,
)

from ._config import (
    config_host_add,
    config_host_list,
)

from ._ls import (
    ls,
)

from ._server import (
    server,
)
