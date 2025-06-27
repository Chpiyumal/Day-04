import shutil
import os

#Create a dummy file and a target directory
file_to_move = 'report.pdf'
target_dir   =  'archives'

with open(file_to_move, 'w') as f:
    f.write("Confidential Report data")
os.makedirs(target_dir, exist_ok=True)
print(f"Created '{file_to_move}' and '{target_dir}'")

#Moving the file
try:
    shutil.move(file_to_move, target_dir)
    print(f"File '{file_to_move} moved to '{target_dir} successfully")
    print(f"New path: {os.path.join(target_dir, file_to_move)}")

except FileNotFoundError:
    print(f"File '{file_to_move}' Not Found")
except FileExistsError:
    print(f"File '{file_to_move}' Already exists in '{target_dir} Directory")
except Exception as e:
    print(f"An Error Occured: '{e}")

#--Cleanup
if os.path.exists(target_dir):
    shutil.rmtree(target_dir) #Use Rmtree as target_dir now contain
print("Cleanup dummy directory")
