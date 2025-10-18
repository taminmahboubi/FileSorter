import os # provides a list of operating system functions (scandir,makedirs, etc.)
import shutil # handles file system operations safely (.move(), .rmtree())

# ANSI color codes
GREEN = '\033[92m'
YELLOW = '\033[38;5;226m'
BLUE = '\033[94m'
RESET = '\033[0m'


# 1) First, get each of the unique file extensions within the current directory

# using a set because its a collection of unique, unordered items (no duplicates allowed)
unique_extensions = set()

for entry in os.scandir('.'):     # loop through the current directory
    if entry.is_file():       # if the element is a file
        extension = os.path.splitext(entry.name)[1].lstrip('.')  # get the extension of that file
        if extension:
            unique_extensions.add(extension)      # add that extension to the list of unique extensions (a folder will be created for these later)

# Printing the number of unique file extensions and their types (using the str.join() method)
print(f"File types found: {len(unique_extensions)}\n{'\n'.join(unique_extensions)}") 
print() # just extra space
# 2) Create a directory for each type of file extension within the current directory.

created_dirs = [] # a new list of the created directories

for entry in unique_extensions: # for each entry in unique_extensions
    os.makedirs(entry, exist_ok=True) # make a directory for each entry, exist_ok=True allows for it to continue (not throw error) if one that directory already exists!
    created_dirs.append(entry) # add it to the list of created_dirs
    print(f"{YELLOW}Directory{RESET}: {entry} → {GREEN}CREATED{RESET}") # a print message to notify the user the directory was created.


 # 3) loop through all the files to get each file into their corresponding folders
for entry in os.scandir('.'): # loop through the current directory again..
    if entry.is_file(): # if the current entry is a file..
        _, extension = os.path.splitext(entry.name) # set the name of the extension to 'extension', ignoring the filename with '_,'
        clean_extension = extension[1:] # bascially removing the '.' from the extension

        if clean_extension: # only move files with extensions
            target_path = os.path.join(clean_extension, entry.name) # created the target path e.g. 'pdf/document.pdf'
            shutil.move(entry.path, target_path) # moves the file from its current location(entry.path) to the new location(target_path)
            print(f"Successfully Moved: {entry.name} to {GREEN}{clean_extension}{RESET}/")







