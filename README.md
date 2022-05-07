# AndrewBot
A Discord bot that is an Andrew soundboard.

Packages installed:
Discord (discord.py)
youtube_dl
Flask
ffmpeg (This must be manually downloaded and put into your PATH variable)
PyNaCl

Requirements:
- Python 3.10 or later installed
- 

Instructions on set up:
- Install Python 3.10 or later
- Install the following packages using 'pip install':
    1) Discord (discord.py API)
    2) youtube_dl
    3) Flask
    4) PyNaCl
- Setting up ffmpeg:
    1) Download ffmpeg zip file from the ffmpeg website
    2) Extract the zip into a folder
    3) Rename the folder to "ffmpeg" and move the folder to your 
        local disk (C:/) folder or into another folder of your preference
    4) Open up "Edit system environment variables" from the control panel
    5) Go to the "Advanced" tab, and then click "Environment Variables..."
    6) In "System Variables" section, find "Path" in the "Variable" column and
        double click on it. Another window should open up called
        "Edit environment variable"
    7) Click the "New" button, and add the path of the ffmpeg folder you
        placed into your file system
    8) ffmpeg should now be installed on your system
- To execute the Python program: python main.py