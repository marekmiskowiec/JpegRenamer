import os

folder_path = "images"
file_extension = "jpeg"

# Check if the folder exists
if not os.path.exists(folder_path):
    print(f"The specified folder '{folder_path}' does not exist.")
    exit()

# Get the list of files in the specified folder
file_list = [file for file in os.listdir(folder_path) if file.endswith(f".{file_extension}")]

# Check if there are files to rename
if not file_list:
    print(f"No files with the extension '.{file_extension}' found in the folder.")
    exit()

# Sort the list of files based on numeric values in the file names
sorted_file_list = sorted(file_list, key=lambda x: int(x.split(".")[0]))

# Rename the files, starting from 1
for index, old_filename in enumerate(sorted_file_list, start=1):
    # Skip system files like '.DS_Store'
    if old_filename == '.DS_Store':
        print("Skip file '.DS_Store'")
        continue

    new_filename = f"{index}.{file_extension}"
    old_filepath = os.path.join(folder_path, old_filename)
    new_filepath = os.path.join(folder_path, new_filename)

    try:
        # Rename the file and print the changes
        os.rename(old_filepath, new_filepath)
        print(f"{old_filename} ----> {new_filename}")
    except Exception as e:
        print(f"Error renaming file '{old_filename}': {str(e)}")