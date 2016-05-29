import os
import shutil

from settings import DOWNLOAD_DIR, dst_dir1,dst_dir2

download_list = os.listdir(DOWNLOAD_DIR)

pairs = []

for file in download_list:

    # Se e' una directory fai questo questo e questo

    location = os.path.join(DOWNLOAD_DIR, file)
    if os.path.isdir(location):
        def get_size():
            total_size = 0
            for dirpath, dirnames, filenames in os.walk(location):
                for f in filenames:
                    fp = os.path.join(dirpath, f)
                    total_size += os.path.getsize(fp)
            return total_size


        if get_size() > 700000000L:
            for file in os.listdir(os.path.join(location)):
                if file.endswith((".mkv", ".avi", "mp4")):  # Sara' un film o un pornazzo
                    shutil.move(os.path.join(location), dst_dir1)
        else:
            shutil.move(os.path.join(location), dst_dir2)

    # Altrimenti se e' un cazzo di file fai questo questo e questo

    elif file.endswith((".mkv", ".avi")):
        shutil.move(os.path.join(location), dst_dir1)
    else:
        shutil.move(os.path.join(location), dst_dir2)
