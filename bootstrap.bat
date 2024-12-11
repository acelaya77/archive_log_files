
@echo off
SET VENV_DIR=venv

:: Check if the virtual environment directory exists
IF NOT EXIST "%VENV_DIR%" (
    echo Creating a virtual environment...
    python -m venv %VENV_DIR%
) ELSE (
    echo Virtual environment already exists.
)

:: Activate the virtual environment
echo Activating the virtual environment...
call %VENV_DIR%\Scripts\activate.bat

:: Install dependencies from requirements.txt
echo Installing dependencies from requirements.txt...
pip install -r requirements.txt

:: Run the Python script (replace 'archive_log_files.py' with your script's filename)
echo Running the Python script...
python archive_log_files.py /path/to/logs  :: Adjust the folder path as needed

:: Deactivate the virtual environment
deactivate
