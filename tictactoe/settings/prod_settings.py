import dj_database_url
from tictactoe.settings.base import *

db_from_env = dj_database_url.config()

DEBUG = False

DATABASES['default'].update(db_from_env)