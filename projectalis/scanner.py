import os
from pathlib import Path
from data.config import TEST_PROJECT_PATH
import subprocess

from db import insert_into_projects_table




def get_git_remote(target_directory):
    process = subprocess.Popen(["git", "remote", "-v"], cwd=target_directory, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    stdout, stderr = process.communicate()
    if process.returncode == 0:
        try:
            return (stdout.split("\t")[1].split(" ")[0])
        except IndexError: # Git Initialised but no git remote-url set
            return None


def is_git_present(path):
    return Path(path/".git").is_dir()

def scan_work_dir(dir_path):
    p = Path(dir_path)
    sub_dirs = [x for x in p.iterdir() if x.is_dir()]
    project_dirs_data = []
    count = 0
    for posixpath in sub_dirs:
        git_present = is_git_present(posixpath)
        if git_present: # if git_init in posixpath
            remote_url = get_git_remote(posixpath)
            git_remote_url = remote_url
        else: # if no git_init in posixpath
            git_remote_url = "no_git"
        dir_data = (
                str(posixpath).split("/")[-1],
                str(posixpath),
                git_remote_url
        )
        count += 1
        project_dirs_data.append(dir_data)
    print(project_dirs_data)
    return project_dirs_data



def add_projects():
    projects_data = scan_work_dir(TEST_PROJECT_PATH)
    insert_into_projects_table(projects_data)

add_projects()