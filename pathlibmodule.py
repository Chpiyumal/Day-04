import pathlib
import os

#------Creating path Objects
print("\n--- 1.Creating path Objects----")
#Current Working Directory
print(pathlib.Path)
current_dir = pathlib.Path.cwd()
print(f"Current working Directory (path object):'{current_dir}'" )

# A relative path
relative_file  = pathlib.Path('my_document.txt')
print(f"Relative file path: '{relative_file}")

# An absolute path according to OS
absolute_path = pathlib.Path('/tmp/test_dir') #Linux, MacOS
#Absolute path = pathlib.Path (C:\Users\Student_15\Desktop\Python Chp\Codes\Day-04>)
print(f"Absolute path example : '{absolute_path}")

#Join paths using '/' operator (very intuitive)
joined_path = current_dir / 'data' / 'reports' / 'report.csv'
print(f"Joined path using / operator: '{joined_path}")


#---------Accessing Path Components---------
print(f"\n----2.Accessign path Components-----")
#Using joined path for above demo
print(f"Full path: '{joined_path}")
print(f"File/Folder name: '{joined_path.name}") #report.csv
print(f"Parent Directory : {joined_path.parent}") # '/path/to/current/dir/data
print(f"File stem (name without suffix): '{joined_path.stem}'") # 'report'
print(f"File suffix (extension): {joined_path.suffix} ") #'csv'
print(f"All suffixes: {joined_path.suffixes}") # ['.csv']
print(f"Anchor (root of the path): {joined_path.anchor}") #'/' or Unic \..C
print(f"Path parts: {joined_path.parts}") #'/', 'path' , 'to'

#---3.Checking Paths (Existence and Type)---
print("\n--- 3.Checking Paths ---")
test_file = pathlib.Path('test_file.txt')
test_dir = pathlib.Path('test_file_dir')