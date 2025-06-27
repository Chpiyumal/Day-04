import os

folder_to_remove = "empty_folder_to_delete"
os.mkdir(folder_to_remove)
try:
    os.rmdir(folder_to_remove)
    print(f"Directory '{folder_to_remove}' removed. ")
except OSError as e:
    print(f"Error removing directory '{folder_to_remove}: {e}")

