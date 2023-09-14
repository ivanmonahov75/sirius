import os
from dotenv import load_dotenv


def get_env_var(var_name):
    load_dotenv()
    return os.getenv(var_name)
