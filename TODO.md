# TODO

[x] - Create and connect to DB
[x] - Tables for dirs, projects, project_types, project_meta_data
    - ~~project_types table: ID, project_type, description~~
    - ~~dirs table: ID, name, path, FK(project_type) REFERENCES project_types(id)~~ 
    - ~~projects table :~~ 
      - ~~ID,~~ 
      - ~~name,~~ 
      - ~~dir_path FK(dirs_table_id), ~~
      - ~~dir_slug PATH,~~ 
      - git_remote FK(git_remote_table id) , 
      - FOREIGN KEY(notes) REFERENCES notes(id)
    
    - project_status table: ID, status_name, description
    - ~~git_remotes table~~
      - ID,
      - git_remote_url,  
      - LATER WITH Github CLI Integration project_visibility_on_remote 
    - ~~notes table:~~
      - id
      - app
      - url
[ ] - Get main work_dir from user
[x] - Scan work_dir for directories with .git and git remote
[ ] - 
[ ] - MVP
[ ] - Invoke from anywhere on the terminal
[ ] - Connect with git remote API
[ ] - API so my todo app can use it
