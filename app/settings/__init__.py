import contextlib

with contextlib.suppress(ImportError):
    from dotenv import load_dotenv, find_dotenv
    load_dotenv(find_dotenv())  # load environment variables from .env when using pycharm


from .settings import *
from .ldap import *
from .drf import *
from .logging import *
from .database import *
