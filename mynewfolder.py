import os

new_folder_name = "my_new_folder"

try:

    os.mkdir(new_folder_name)
    print(f"Directory '{new_folder_name}' aleady exists.")
except FileExistsError:
    print(f"An error occured: {e}")

