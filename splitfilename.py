#from somehwere on StackOverflow
import os
import shutil
 
# Source directories - relative or absolute paths.
source_folder = "./source/"
destination = "./target/"
 
# A list of all files in the source directory
for folders, subfolders, file in os.walk(source_folder):
    src_file = os.path.join(source_folder, file)
    # splitext() splits the basename and extension from the filename
    #, eg exclude.txt becomes (exclude, .txt)
    filename, extension = os.path.splitext(file)
    # Create a new filename with the string "_copy" added to it
    new_file = f"{filename}_copy{extension}"
    # Join the destination folder with the new filename
    dest_file = os.path.join(destination, new_file)
    # If the destination file already exists, skip it
    if os.path.exists(dest_file):
        continue
    # Copy the source file to the destination folder with the new filename
    shutil.copy(src_file, dest_file)