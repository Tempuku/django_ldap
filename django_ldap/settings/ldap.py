import ldap
import os
from django_auth_ldap.config import LDAPSearch


AUTH_LDAP_SERVER_URI = os.getenv("AUTH_LDAP_SERVER_URI")
AUTH_LDAP_BIND_DN = os.getenv("AUTH_LDAP_BIND_DN")
AUTH_LDAP_BIND_PASSWORD = os.getenv("AUTH_LDAP_BIND_PASSWORD")
AUTH_LDAP_USER_SEARCH = LDAPSearch(os.getenv("AUTH_LDAP_USER_DIRECTORY"), ldap.SCOPE_SUBTREE,
                                   os.getenv("AUTH_LDAP_USER_UID"))
AUTH_LDAP_USER_ATTR_MAP = {
    "first_name": "givenName",
    "last_name": "sn",
    "email": "mail"
}
