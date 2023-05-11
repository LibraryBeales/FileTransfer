import os
import shutil

src_dir = "./source"
dest_dir = "./target"

# The final name of the files after copy
file_name = "textcopy"
# The file name you want to copy, loop uses .contain so can be incomplete.
search_name = "another"

#Could make both 

# Initialize an index to add to the new filenames.
index = 0

# os.walk will go through the src_dir and all subdirectories
for root, dirs, files in os.walk(src_dir):
    for file in files:
        # Check if the file matches the search_name
        if file.__contains__(search_name):
            # Construct the full path to the file
            file_path = os.path.join(root, file)
            # Construct the new filename with an index.  File extension is set manually, but could be user input.
            new_file_name = f"{file_name}_{index}.txt"
            new_file_path = os.path.join(dest_dir, new_file_name)
            # Move the file to the destination directory
            shutil.copy(file_path, new_file_path)
            # Plus 1 the index.  #If you are doing this in batches, you'll have to manually adjust the index starting point.  Another potential input.
            index += 1