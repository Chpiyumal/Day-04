import shutil
import os

#Create a source file
source_file = "source_doc.txt"
with open(source_file, 'w') as f:
    f.write("This is the original content.")
print(f"Created the '{source_file}' file for copying")

#----Copy the file
destination_file = "copied_doc.txt"
try:
    shutil.copy(source_file, destination_file)
    print(f"File '{source_file}' succssfully copied to '{destination_file}")
    print(f"Content of '{destination_file}: {open(destination_file)}")
except FileNotFoundError:
    print(f"File '{source_file} not found")
except Exception as e:
    print(f"Error Occured: '{e}")

#----Cleanup
if os.path.exists(source_file):
    os.remove(source_file)
if os.path.exists(destination_file):
    os.remove(destination_file)
print("Cleaned up the dummy files")
