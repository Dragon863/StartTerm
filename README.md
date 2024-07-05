## StartTerm

![Screenshot](https://i.imgur.com/hj4kRtm.png)

StartTerm is a simple dashboard like a browser's "New Tab" page, but for your terminal. It has support for pulling the weather, your local IP, the time and battery percentage. It is fairly simple so should be easy to modify to your liking. Wallpaper support is also included, which renders any PNG or JPEG image to coloured unicode blocks, although this will only work on terminal emulators with true-colour support. There are configurable shortcuts which can be set up to run commands at the bottom of the screen. 

# Installation

To get started, clone the repo, run `pip install -r requirements.txt` and configure the example.env file to your preferences. Then you can rename it to .env and run main.py to start the program. You can also add it to your .bashrc or .zshrc to start it on login. Shortcuts can be configured in the shortcuts.json file. 