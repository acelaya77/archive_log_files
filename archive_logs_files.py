#!/usr/bin/env python3

import argparse
import os
import zipfile
from datetime import datetime

from tqdm import tqdm


def archive_logs_by_month(folder_path):
    # Debug: Print the folder path to check if it's correct
    print(f"Processing folder: {folder_path}")

    # Get list of all files in the folder
    try:
        files = os.listdir(folder_path)
        print(f"Found {len(files)} files in the folder.")
    except Exception as e:
        print(f"Error reading folder: {e}")
        return

    # Group files by month
    files_by_month = {}
    for file in files:
        if file.endswith((".log", ".html", ".json", ".txt")):
            file_path = os.path.join(folder_path, file)
            try:
                file_month = datetime.fromtimestamp(
                    os.path.getmtime(file_path)
                ).strftime("%Y-%m")
                if file_month not in files_by_month:
                    files_by_month[file_month] = []
                files_by_month[file_month].append(file_path)
            except Exception as e:
                print(f"Error processing file {file}: {e}")
                continue  # Skip this file if an error occurs

    # Debug: Print the number of files grouped by month
    print(f"Found {len(files_by_month)} months of log files to archive.")

    # Create zip archives and remove original files with progress bar
    for month, file_paths in files_by_month.items():
        zip_file_path = os.path.join(folder_path, f"{month}.zip")
        print(f"Creating zip archive for {month}: {zip_file_path}")

        # Ensure the zip file is opened in write mode with compression
        try:
            with zipfile.ZipFile(zip_file_path, "w", zipfile.ZIP_DEFLATED) as zipf:
                for file_path in tqdm(
                    file_paths, desc=f"Archiving {month}", unit="file"
                ):
                    try:
                        zipf.write(
                            file_path, os.path.basename(file_path)
                        )  # Write file to the zip
                        os.remove(file_path)  # Remove the original file
                        print(
                            f"Archived and removed {file_path}"
                        )  # Debug: Log each file being processed
                    except Exception as e:
                        print(f"Error processing file {file_path}: {e}")
                        continue  # Skip this file if an error occurs
        except Exception as e:
            print(f"Error creating zip file for {month}: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Archive log files by month.")
    parser.add_argument(
        "folder_path", type=str, help="Path to the folder containing log files."
    )
    args = parser.parse_args()

    # Ensure the folder path exists
    if not os.path.isdir(args.folder_path):
        print(
            f"Error: The specified folder path {args.folder_path} does not exist or is not a directory."
        )
    else:
        archive_logs_by_month(args.folder_path)
