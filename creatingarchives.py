import shutil
import os

#Create a Dummy folder content to archive
data_folder = "my_data_for_archive"
os.makedirs(os.path.join(data_folder, "docs"), exist_ok=True)
with open(os.path.join(data_folder, "Important.txt"), 'w')as f:
    f.write("Important Data Here")
with open(os.path.join(data_folder, "notes.md"), 'w')as f:
    f.write("Meeting Notes")
print(f"Created a dummy foler for archive: '{data_folder}'")


#---Creating a zip for archive
archive_name = "My_data_archive"

try:
    #--Create my_data_for_archive.zip in current directory
    #Containing the content of my_data for archive
    archive_path = shutil.make_archive(archive_name, 'zip', root_dir=data_folder)
    print(f"archive created '{archive_path}'")
    print(f"Does archive exist? {os.path.exists(archive_path)}")
except Exception as e:
    print(f"An Error Occured: '{e}'")
        
#Cleanup 
if os.path.exists(data_folder):
    os.remove(data_folder)
if os.path.exists(archive_path):
    os.remove(archive_path)