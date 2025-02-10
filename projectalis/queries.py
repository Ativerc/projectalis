
# create table queries
create_project_tags_table_query = """
CREATE TABLE IF NOT EXISTS project_tags(
id INTEGER PRIMARY KEY AUTOINCREMENT,
project_tag TEXT UNIQUE,
description TEXT
);
"""

# create_git_remotes_table_query = """
# CREATE TABLE IF NOT EXISTS git_remotes(
# id INTEGER PRIMARY KEY AUTOINCREMENT,
# url TEXT
# );
# """

create_notes_table_query = """
CREATE TABLE IF NOT EXISTS notes(
id INTEGER PRIMARY KEY AUTOINCREMENT,
app TEXT UNIQUE,
url TEXT
);"""

create_workspace_dirs_table_query = """
CREATE TABLE IF NOT EXISTS workspace_dirs(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT UNIQUE,
path TEXT UNIQUE,
project_tag_id INTEGER,
FOREIGN KEY(project_tag_id) REFERENCES project_tags(id)
);
"""

create_projects_table_query = """
CREATE TABLE IF NOT EXISTS projects(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT UNIQUE,
path TEXT UNIQUE,
git_remote_url TEXT,
last_modified_date DATE,
workspace_dir_id INTEGER,
notes_id INTEGER,
FOREIGN KEY(workspace_dir_id) REFERENCES workspace_dirs(id),
FOREIGN KEY(notes_id) REFERENCES notes(id)
);
"""

# insert into projects table
insert_into_projects_table_query = """
INSERT INTO projects(name, path, git_remote_url) VALUES(?,?,?);
"""