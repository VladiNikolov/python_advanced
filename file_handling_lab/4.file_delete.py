import os

try:
    os.remove("delete_this_file.txt")
except FileNotFoundError:
    print('File already deleted!')

