"""Here we see how to move all the file from the desktop into a folder"""  # noqa
"""Below are the steps that we are going to follow to achieve the task"""

"""
1. Make the folder CleanedUp/
2. List the files in the Desktop/ folder
3. For each file in the Desktop/ folder
    4. Move the file to the CleanedUp/ folder
"""

import os  # noqa

folder = 'C:/Users/10695562/OneDrive - LTIMindtree/Desktop/'

entries = os.scandir(folder)

# example1
for entry in entries:
    if os.path.isfile(entry):
        print('File:', entry.name)
    elif os.path.isdir(entry):
        print('Directory:', entry.name)

#  example 2
folder_original = 'C:/Users/10695562/OneDrive - LTIMindtree/Desktop/'
folder_destination = 'C:/Users/10695562/OneDrive - LTIMindtree/Desktop/CleanedUp/'  # noqa
if not os.path.isdir(folder_destination):
    os.mkdir(folder_destination)

for entry in os.scandir(folder_original):
    location_original = os.path.join(folder_original, entry.name)
    location_destination = os.path.join(folder_destination, entry.name)

    if os.path.isfile(location_original):
        os.rename(location_original, location_destination)
        print("File: ", location_original, " --moved to-->", location_destination)  # noqa
    else:
        print("No files to cleanup!!")
