#!/usr/bin/env python3

import os
import zipfile
from datetime import datetime

from tqdm import tqdm


def archive_logs_by_month(folder_path):
    # Get list of all files in the folder
    files = os.listdir(folder_path)

    # Group files by month
    files_by_month = {}
    for file in files:
        if file.endswith(".log"):
            file_path = os.path.join(folder_path, file)
            file_month = datetime.fromtimestamp(os.path.getmtime(file_path)).strftime(
                "%Y-%m"
            )
            if file_month not in files_by_month:
                files_by_month[file_month] = []
            files_by_month[file_month].append(file_path)

    # Create zip archives and remove original files with progress bar
    for month, file_paths in files_by_month.items():
        zip_file_path = os.path.join(folder_path, f"{month}.zip")
        with zipfile.ZipFile(zip_file_path, "w") as zipf:
            for file_path in tqdm(file_paths, desc=f"Archiving {month}", unit="file"):
                zipf.write(file_path, os.path.basename(file_path))
                os.remove(file_path)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Archive log files by month.")
    parser.add_argument(
        "folder_path", type=str, help="Path to the folder containing log files."
    )
    args = parser.parse_args()

    archive_logs_by_month(args.folder_path)
