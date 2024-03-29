import environ
from split_settings.tools import include
from dotenv import find_dotenv

env = environ.Env()
env.read_env(env_file=find_dotenv(".env"))

DEBUG = env.bool("DEBUG", default=True)

settings: tuple[str, ...] = (
    "components/common.py",
    "components/auth.py",
    "components/database.py",
    "components/apps.py",
    "components/middleware.py",
    "components/templates.py",
    "components/timezone.py",
    "components/locale.py",
)

include(*settings)
