import os
from plugins import base

system = base.get_platform()
base.init_hosts(system)
base.handle_plugins()
base.copy_host(system)
base.flush_dns(system)