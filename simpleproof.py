import os
import shutil

source_folder = "./source"
destination_folder = "./target"

name = "anothercopy.txt"

dest_dir = (destination_folder)

for folders, subfolders, files in os.walk(source_folder):

    for index, file in enumerate(files, 1):
        three_digit_index = str(index).zfill(3)
        source_file = os.path.join(folders, file)
        filename, extension = os.path.splitext(file)
        new_file = f"{filename}_{three_digit_index}{extension}"
        destination1 = os.path.join(dest_dir, new_file)
        if os.path.exists(destination1):
            continue
        if file.endswith(name):
            shutil.copy2(source_file, destination1)

