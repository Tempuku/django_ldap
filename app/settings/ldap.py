import ldap
import os

from django.utils.module_loading import import_string
from django_auth_ldap.config import LDAPSearch

AUTH_LDAP_SERVER_URI = os.getenv("AUTH_LDAP_SERVER_URI")
AUTH_LDAP_BIND_DN = os.getenv("AUTH_LDAP_BIND_DN")
AUTH_LDAP_BIND_PASSWORD = os.getenv("AUTH_LDAP_BIND_PASSWORD")
AUTH_LDAP_USER_SEARCH = LDAPSearch(os.getenv("AUTH_LDAP_USER_DIRECTORY"), ldap.SCOPE_SUBTREE,
                                   os.getenv("AUTH_LDAP_USER_UID"))
AUTH_LDAP_USER_ATTR_MAP = {
    "username": "cn",
    "first_name": "givenName",
    "last_name": "sn"
}
AUTH_LDAP_GROUP_SEARCH = LDAPSearch(os.getenv("AUTH_LDAP_USER_DIRECTORY"), ldap.SCOPE_SUBTREE)
AUTH_LDAP_GROUP_TYPE = import_string("django_auth_ldap.config." + os.getenv("AUTH_LDAP_GROUP_TYPE", "PosixGroupType"))
AUTH_LDAP_USER_FLAGS_BY_GROUP = {
    "is_superuser": "CN=django-admins," + os.getenv("AUTH_LDAP_USER_DIRECTORY"),
}
AUTH_LDAP_FIND_GROUP_PERMS = True
AUTH_LDAP_CACHE_GROUPS = True
AUTH_LDAP_GROUP_CACHE_TIMEOUT = 1  # 1 hour cache
