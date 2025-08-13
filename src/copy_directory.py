import os
import shutil

def copy_directory(src, dst):


    if not os.path.exists(dst):
        os.mkdir(dst)

    content = os.listdir(src)
    for item in content:
        item_path = os.path.join(src, item)
        if os.path.isfile(item_path):
            shutil.copy(item_path, dst)
        if os.path.isdir(item_path):
            new_dir = os.path.join(dst, item)
            copy_directory(item_path, new_dir)
        