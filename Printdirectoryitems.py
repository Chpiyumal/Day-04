import os

#List content of the directory
print("Contents of the current directory")
for item in os.listdir('.'):
    print(item)
