'''BIGmama Python wrapper for the MinIO command line interface.'''

__version__ = '0.0.4'
__title__ = 'bmc'


from ._ls import (
    ls,
)

from ._mb import (
    mb,
)

from ._rb import (
    rb,
)

from ._cp import (
    cp,
)


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


from ._server import (
    server,
)

from ._policy import (
    admin_policy_add,
    admin_policy_remove,
    admin_policy_list,
    admin_policy_info,
    admin_policy_set,
)

from ._group import (
    admin_group_add,
    admin_group_remove,
    admin_group_info,
    admin_group_list,
    admin_group_enable,
    admin_group_disable,
)

from ._utils import (
    BMCError,
    check_error,
)
