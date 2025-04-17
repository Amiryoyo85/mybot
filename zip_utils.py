
import zipfile
import os

def create_zip(directory, zip_name):
    """Create a zip file from a directory."""
    if not os.path.exists(directory):
        raise ValueError(f"Directory '{directory}' does not exist")
        
    with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for foldername, subfolders, filenames in os.walk(directory):
            for filename in filenames:
                file_path = os.path.join(foldername, filename)
                # Skip the zip file itself if it's in the same directory
                if os.path.abspath(file_path) == os.path.abspath(zip_name):
                    continue
                zipf.write(file_path, os.path.relpath(file_path, directory))
