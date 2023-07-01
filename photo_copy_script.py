import os
import shutil
from datetime import datetime

def copy_images(src, dst):
    for root, dirs, files in os.walk(src):
        for file in files:
            if file.endswith(".jpg") or file.endswith(".jpeg"):
                file_path = os.path.join(root, file)
                creation_time = os.path.getctime(file_path)
                year = datetime.fromtimestamp(creation_time).year
                dst_folder = os.path.join(dst, str(year))
                if not os.path.exists(dst_folder):
                    os.makedirs(dst_folder)
                shutil.copy2(file_path, dst_folder)

src_folder = "E:\\backup\\pic\\Dropbox"
dst_folder = "D:\\pics"
copy_images(src_folder, dst_folder)