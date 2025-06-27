import shutil
import os

#Setup:Creating a dummy source directory
source_dir = "my_source_project"

os.makedirs(os.path.join(source_dir, "css"), exist_ok=True)
os.makedirs(os.path.join(source_dir, "js"), exist_ok=True)
with open(os.path.join(source_dir, "index.html"), 'w') as f:
    f.write("<html></html>")
with open(os.path.join(source_dir, "style.css"), 'w') as f:
    f.write("body{}")
print(f"Created Dummy source Directory: '{source_dir}")

#Copy the Directory Tree
destination_dir = "my_backup_project"

try:
    #If destination directory already exists and not empty, copytree will raise
    #To overwrite, typically removes the destination first and move
    shutil.copytree(source_dir, destination_dir)
    print(f"'{source_dir}' copied to '{destination_dir}' successfully")
    print(f"Contents of destination directory")
    for root, dirs, files in os.walk(destination_dir):
        level = root.replace(destination_dir, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print(f"{indent}{os.path.basename(root)}/")
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print(f"{subindent}{f}")
except FileExistsError:
    print(f"Error: Destination directory '{destination_dir}' already exists")
except Exception as e:
    print(f"Error Occured: '{e}'")
     