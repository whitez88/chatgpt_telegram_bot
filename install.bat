@echo off

echo You can rerun this script to update the installation.

echo Checking for Python 3.10...

py -3.10 --version >nul 2>&1
if %errorlevel%==0 (
    echo Python 3.10 is already installed.
) else (
    echo Python 3.10 is not installed. Downloading installer...
    curl https://www.python.org/ftp/python/3.10.10/python-3.10.10-amd64.exe -o python-3.10.10-amd64.exe

    echo Installing Python 3.10...
    python-3.10.10-amd64.exe /quiet InstallAllUsers=1 PrependPath=1

    echo Cleaning up installer...
    del python-3.10.10-amd64.exe
)

echo Creating virtual environment...
py -3.10 -m venv venv

echo Updating pip and wheel...
venv\Scripts\python.exe -m pip install --upgrade pip

venv\Scripts\pip.exe install -r requirements.txt