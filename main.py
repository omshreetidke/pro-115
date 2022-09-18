
import os

source = 'mainfile.txt'

dest = 'newfile.txt'

os.rename(source, dest)
print("Source path renamed to destination path successfully.")