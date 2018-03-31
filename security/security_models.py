# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging

from flask_appbuilder.const import LOGMSG_WAR_SEC_LOGIN_FAILED
from flask_appbuilder.security.sqla.manager import SecurityManager

from security.security_views import MyAuthRemoteUserView

logger = logging.getLogger(__name__)


class MySecurityManager(SecurityManager):
    logger.info("using customize my security manager")
    authremoteuserview = MyAuthRemoteUserView

    def auth_user_remote_user(self, username):
        """
            this is a overwrite method
            
            REMOTE_USER user Authentication

            :type self: User model
        """
        user = self.find_user(username=username)

        # User does not exist, create one if auto user registration.
        if user is None and self.auth_user_registration:
            user = self.add_user(
    # All we have is REMOTE_USER, so we set
    # the other fields to blank.
                username=username,
                first_name=username.split('@')[0],
                last_name='-',
                email=username,
                role=self.find_role(self.auth_user_registration_role))

        # If user does not exist on the DB and not auto user registration,
        # or user is inactive, go away.
        elif user is None or (not user.is_active()):
            logger.info(LOGMSG_WAR_SEC_LOGIN_FAILED.format(username))
            return None
            
        self.update_user_auth_stat(user)
        return user
