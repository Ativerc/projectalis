import sqlite3
from constants import DB_FILEPATH
from queries import (create_project_tags_table_query,
                    create_notes_table_query,
                    create_workspace_dirs_table_query,
                    create_projects_table_query)

from queries import insert_into_projects_table_query


conn = sqlite3.connect(DB_FILEPATH)

def create_tables():
    cur = conn.cursor()
    script = (f"""
                    {create_project_tags_table_query}
                    {create_notes_table_query}
                    {create_workspace_dirs_table_query}
                    {create_projects_table_query}
                    """)
    cur.executescript(script)

def insert_into_projects_table(data):
    cur = conn.cursor()
    try:
        cur.executemany(insert_into_projects_table_query, data)
        conn.commit()
    except sqlite3.Error as e:
        print(e)

    

if __name__ == "__main__":
    create_tables()
    pass
