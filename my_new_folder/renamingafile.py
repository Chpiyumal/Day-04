import os

old_name = "old_file.txt"
new_name = "new_file.txt"

#Create a dummy file for demo
with open(old_name, 'w') as f:
    f.write("Content of the old file")

try:
    os.rename(old_name, new_name)
    print(f"Renamed '{old_name}' to '{new_name}'")

except FileNotFoundError:
    print(f"Old file '{old_name}' not found")
except FileExistsError:
    print(f"File '{new_name}' already exists.")
except Exception as e:
    print(f"An error occured: '{e}'")
    