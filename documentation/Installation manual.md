# Scribase installation manual
After downloading the repository to your computer you can install the software as follows:

Please note that this guide is for windows, and may not work for other OS.

### Automatic install
Note: automatic installer is for windows only.

Run the Installer.cmd found in the download folder.

If the automatic installation does not work, you may want to use the manual method.

### Manual install
Note: use python or python3 in commands depending on your python installation.

Open a command prompt in the repository's folder and input these commands:

python -m venv venv

venv\scripts\activate

pip install -r requirements.txt

The installation should now be finished.

Please refer to the user manual for help in running the software.

### Linux install
If you're using a Linux machine, follow the previous manual installing guide but replace

venv\scripts\activate

with

source venv/bin/activate