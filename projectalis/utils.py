import configparser
import os


from projectalis.constants import CONFIG_FILEPATH

def save_config(work_dir):
    """Saves the config file to the CONFIG_FILEPATH

    Args:
        dir (str): location of a work_dir
    """
    Config = configparser.RawConfigParser()
    with open(CONFIG_FILEPATH, 'w') as config_file:
        Config.add_section('Base')
        Config.set('Base', work_dir, work_dir)
        Config.write(config_file)

