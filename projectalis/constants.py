import os
from pathlib import Path
from data.config import TEST_PROJECT_PATH


ENV_PATH = "." # str(Path.home())

CONFIG_FILEPATH = os.path.join(ENV_PATH, 'data', 'projectalis-config.ini')
DB_FILEPATH = os.path.join(ENV_PATH, 'data', 'projectalis.db')

print(CONFIG_FILEPATH, DB_FILEPATH)