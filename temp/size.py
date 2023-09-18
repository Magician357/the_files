import math

def convert_size(size_bytes):
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return "%s %s" % (s, size_name[i])

# import module
import os

# assign size
size = 0

# assign folder path
folders=["C:\\Users\\zacha\\OneDrive\\Documents\\programms\\the_files\\temp\\other","C:\\Users\\zacha\\OneDrive\\Documents\\programms\\the_files\\temp\\text","C:\\Users\\zacha\\OneDrive\\Documents\\programms\\the_files\\temp\\video"]

# get size
for Folderpath in folders:
    for path, dirs, files in os.walk(Folderpath):
        for f in files:
            fp = os.path.join(path, f)
            size += os.path.getsize(fp)

# display size
print("Folder size: " + str(size)+" bytes")
print(convert_size(size))