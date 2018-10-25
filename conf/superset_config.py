from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

try:
	# you'd better put all the import stuff here, since superset will ignore it 
	from flask_appbuilder.security.manager import AUTH_REMOTE_USER
	from security.security_models import MySecurityManager
except Exception as ex:
	raise Exception(ex)

# using customize MY security manager
CUSTOM_SECURITY_MANAGER = MySecurityManager

# AUTHENTICATION CONFIG
AUTH_TYPE = AUTH_REMOTE_USER

# setup Public role name, no authentication needed
AUTH_ROLE_PUBLIC = 'Gamma'

# Will allow user self registration
AUTH_USER_REGISTRATION = True
