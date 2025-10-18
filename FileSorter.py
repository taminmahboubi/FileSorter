# provides a list of operating system functions (scandir,makedirs, etc.)
import os

# 1) First, get each of the unique file extensions within the current directory

# using a set because its a collection of unique, unordered items (no duplicates allowed)
unique_extensions = set()

for entry in os.scandir('.'):     # loop through the current directory
    if entry.is_file():       # if the element is a file
        extension = os.path.splitext(entry.name)[1].lstrip('.')  # get the extension of that file
        unique_extensions.add(extension)      # add that extension to the list of unique extensions (a folder will be created for these later)

