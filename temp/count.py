import os

count = 0
for root_dir, cur_dir, files in os.walk(r'C:\Users\zacha\OneDrive\Documents\programms\the_files\temp'):
    count += len(files)
print('file count:', count-1)