#!/usr/bin/env python3

import os
import platform
import subprocess
import venv

VENV_DIR = "venv"


def create_venv():
    """Create the virtual environment if it doesn't exist."""
    if not os.path.exists(VENV_DIR):
        print(f"Creating virtual environment in {VENV_DIR}...")
        venv.create(VENV_DIR, with_pip=True)
    else:
        print(f"Virtual environment already exists in {VENV_DIR}.")


def install_requirements():
    """Install dependencies from requirements.txt."""
    print("Installing dependencies from requirements.txt...")
    subprocess.run(
        [
            os.path.join(
                VENV_DIR, "bin" if platform.system() != "Windows" else "Scripts", "pip"
            ),
            "install",
            "-r",
            "requirements.txt",
        ],
        check=True,
    )


def run_script():
    """Run the main archive_log_files.py script."""
    # Define the parameters to pass to the script (adjust folder path as needed)
    script_params = ["./logs/"]  # Update this as per your need

    # Build the command to run the script with the parameters using the virtual environment's Python
    command = [
        os.path.join(
            VENV_DIR,
            "bin" if platform.system() != "Windows" else "Scripts",
            "python",
        ),
        "archive_log_files.py",
    ] + script_params  # Append the parameters

    # Run the script
    subprocess.run(command, check=True)


def main():
    # Step 1: Create the virtual environment if it doesn't exist
    create_venv()

    # Step 2: Install requirements (if needed)
    install_requirements()

    # Step 3: Run the Python script (archive_log_files.py)
    run_script()


if __name__ == "__main__":
    main()
