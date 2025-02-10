#!/usr/bin/python

import argparse
from pathlib import Path



from constants import CONFIG_FILEPATH, DB_FILEPATH

CONFIG_DATA_PATH = "./data"


def checks():
    # CONFIG DATA PATH check --> no? config data path 
    # doesn't exist
    # CONFIG FILE PATH check --> no? prompt user to 
    # run setup
    # 
    if Path(CONFIG_DATA_PATH).exists() is False:
        raise Exception("The ConfigFile path doesn't exist! Please check!")
    if Path(DB_FILEPATH).exists() is False:
        raise Exception("The DBFile path doesn't exist! Please check!")


def main():
    parser = argparse.ArgumentParser(description="Keep track of your projects using the command line",
                                    formatter_class=argparse.ArgumentDefaultsHelpFormatter) # include default value of arguments in help message
    parser.add_argument('--configure', action='store_true', 
                        help="Configure projectalis. If run, you will " +
                        "be prompted for configuration values such as:\n" +
                        "Your default workspace, a default project_tag")
    args = parser.parse_args()
    print("""Welcome to projectalis
        
        This CLI tool will help you to keep track of all your coding/dev projects on your PC
        """)
    


if __name__ == "__main__":
    main()