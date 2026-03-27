# edu/ccrm/io/BackupService.py

import os
import shutil
from datetime import datetime

class BackupService:

    # ✅ Copy files to timestamped backup folder
    def backup(self, source_folder, backup_root):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        source = source_folder
        dest = os.path.join(backup_root, f"backup_{timestamp}")

        os.makedirs(dest, exist_ok=True)

        # Copy files and folders
        for root, dirs, files in os.walk(source):
            rel_path = os.path.relpath(root, source)
            target_dir = os.path.join(dest, rel_path)

            os.makedirs(target_dir, exist_ok=True)

            for file in files:
                src_file = os.path.join(root, file)
                dst_file = os.path.join(target_dir, file)

                shutil.copy2(src_file, dst_file)

        print(f"✅ Backup created at {dest}")

    # ✅ Recursive utility: show directory size
    def compute_directory_size(self, directory):
        total_size = 0

        for root, dirs, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    total_size += os.path.getsize(file_path)
                except OSError:
                    pass

        return total_size