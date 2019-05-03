# Scribase installation manual
After downloading the repository to your computer you can install the software as follows:

Please note that this guide is for windows, and may not work for other OS.

## How to install locally
### Automatic install
Note: automatic installer is for windows only.

Run the `Installer.cmd` found in the download folder.

If the automatic installation does not work, you may want to use the manual method.

### Manual install
Note: use python or python3 in commands depending on your python installation.

Open a command prompt in the repository's folder and input these commands:

1. `python -m venv venv`

2. `venv\scripts\activate`

3. `pip install -r requirements.txt`

The installation should now be finished.

Please refer to the user manual for help in running the software.

### Linux install
If you're using a Linux machine, follow the previous manual installing guide but replace

`venv\scripts\activate`

with

`source venv/bin/activate`

## How to install to Heroku
You will need to have installed git and heroku on your PC.

To use this software on Heroku, you'll need gunicorn. You'll need venv for this step `venv\scripts\activate` or `venv/bin/activate`.
* pip install gunicorn

Next follow through these commands:
* heroku create [custom-name]
* git remote add heroku https://git.heroku.com/[custom-name].git
* git add .
* git commit -m "[custom-commit-name]"
* git push heroku master

You can now find the software at https://[custom-name].herokuapp.com/
