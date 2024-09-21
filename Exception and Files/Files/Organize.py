import os
import shutil
from pathlib import Path

# Define the file type categories
file_types = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'],
    'Documents': ['.pdf', '.doc', '.docx', '.txt', '.ppt', '.pptx', '.xls', '.xlsx'],   # noqa
    'Videos': ['.mp4', '.mov', '.avi', '.mkv', '.flv'],
    'Music': ['.mp3', '.wav', '.aac', '.flac'],
    'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz'],
    'Scripts': ['.py', '.js', '.html', '.css', '.sh', '.bat'],
    'Others': []  # For any other file types
}


def organize_desktop(desktop_path):
    # Ensure the path is valid
    desktop = Path(desktop_path)
    if not desktop.exists():
        print(f"The path {desktop_path} does not exist.")
        return

    # Iterate over each file in the desktop directory
    for item in desktop.iterdir():
        if item.is_file():
            # Get the file extension
            ext = item.suffix.lower()

            # Find the appropriate folder based on file extension
            folder_name = None
            for category, extensions in file_types.items():
                if ext in extensions:
                    folder_name = category
                    break
            if not folder_name:
                folder_name = 'Others'  # If no category matches

            # Create the folder if it doesn't exist
            folder_path = desktop / folder_name
            folder_path.mkdir(exist_ok=True)

            # Move the file into the appropriate folder
            shutil.move(str(item), str(folder_path / item.name))

    print("Desktop organized successfully.")


if __name__ == '__main__':
    # Set your desktop path here
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    desktop_path = 'C:/Users/10695562/OneDrive - LTIMindtree/Desktop/'
    print("the desktop path: ", desktop_path)
    organize_desktop(desktop_path)
