import os
from pathlib import Path
from data.config import TEST_PROJECT_PATH

if os.environ.get("PROJECTALIS_ENV") == "DEV":
    ENV_PATH = "." # else str(Path.home())
    PROJECT_PATH = TEST_PROJECT_PATH


CONFIG_FILEPATH = os.path.join(ENV_PATH, 'data', 'projectalis-config.ini')
DB_FILEPATH = os.path.join(ENV_PATH, 'data', 'projectalis.db')

print(CONFIG_FILEPATH, DB_FILEPATH)
print(f"""
    PROJECTALIS_ENV: {os.environ.get("PROJECTALIS_ENV")} 
    env_path:{ENV_PATH} 
    test_project_path:{TEST_PROJECT_PATH} 
    config:{CONFIG_FILEPATH} 
    db_filepath: {DB_FILEPATH}"""
)