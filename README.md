# personal-rom-file-move
Two Python scripts that are made for moving the contents of ROMS and BIOS files to a backup location using Robocopy, and for restoring those files to the non-backup location.

# robocopy_files_backup.py
Script to backup the files. Modules used:
- subprocess -> call

- os -> listdir, makedirs

# robocopy_files_restore.py
Script to restore the files. Modules used:
- subprocess -> call

- os -> listdir