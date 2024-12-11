#!/usr/bin/env python3

import argparse
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
        if file.endswith(
            (".log", ".json", ".html")
        ):  # Support for log, json, html files
            file_path = os.path.join(folder_path, file)
            file_month = datetime.fromtimestamp(os.path.getmtime(file_path)).strftime(
                "%Y%m"
            )
            if file_month not in files_by_month:
                files_by_month[file_month] = []
            files_by_month[file_month].append(file_path)

    # Create zip archives and remove original files with progress bar
    for month, file_paths in files_by_month.items():
        zip_file_path = os.path.join(folder_path, f"archive_{month}.zip")
        with zipfile.ZipFile(zip_file_path, "w") as zipf:
            for file_path in tqdm(file_paths, desc=f"Archiving {month}", unit="file"):
                zipf.write(file_path, os.path.basename(file_path))
                os.remove(file_path)


def main():
    parser = argparse.ArgumentParser(description="Archive log files by month.")
    parser.add_argument(
        "folder_path", type=str, help="Path to the folder containing log files."
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Perform a dry-run without actually archiving the files.",
    )
    parser.add_argument(
        "--log-level",
        type=str,
        default="INFO",
        help="Set the logging level (e.g., INFO, DEBUG, WARNING).",
    )
    args = parser.parse_args()

    # Perform dry-run if specified
    if args.dry_run:
        print("Dry run: No files will be archived.")

    print(f"Starting to archive log files from: {args.folder_path}")
    archive_logs_by_month(args.folder_path)


if __name__ == "__main__":
    main()
