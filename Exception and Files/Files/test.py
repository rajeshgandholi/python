import os

desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
print("the desktop path: ", desktop_path)
desktop_path = 'C:/Users/10695562/OneDrive - LTIMindtree/Desktop/'
entries = os.scandir(desktop_path)

# example1
for entry in entries:
    if os.path.isfile(entry):
        print('File:', entry.name)
    elif os.path.isdir(entry):
        print('Directory:', entry.name)
