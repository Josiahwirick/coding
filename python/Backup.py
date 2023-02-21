import os
import shutil
import time

# Replace folder paths
folder_to_backup = '/home/user/Desktop'
backup_folder = '/home/user/Backup/'

# Set the inital backup time to 0
last_backup_time = 0

while True:
    # Get current modified time of the  folder
    current_time = os.path.getmtime(folder_to_backup)
    
    # If the folder has been modified since the last backup, create a new backup
    if current_time > last_backup_time:
        print("Folder modified, creating backup...")
        
        # Create a new backup folder with a timestamp
        timestamp = time.strftime('%Y-%m-%d_%H-%M-%S')
        backup_folder_with_timestamp = backup_folder + "_" + timestamp
        try:
            shutil.copytree(folder_to_backup, backup_folder_with_timestamp)
            print("Backup created")
        except shutil.Error as e:
            print(f'Error creating backup: {e}')
        except OSError as e:
            print(f'Error: {e.filename} - {e.strerror}')
        # Update the last backup time
        last_backup_time = current_time
        
        
    else:
        print('No changes detected, no backup created. Checking again soon...')
        
    # Wait for a few seconds before checking again
    time.sleep(10)
