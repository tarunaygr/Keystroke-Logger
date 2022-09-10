# Keystroke-Logger
A Keystroke logger written in Python.


The `game.exe` is run on a victim computer. The game will start the keystroke logger in the background. The keystroke logger will store all the keystrokes made and send them to a specfied IP address which will be running the `server.py` script. The server will then store the keystrokes locally.

The IP to which the keystrokes will be sent to can be configured in `game.py` file. The game will have to be rebuilt to an executable file after reconfiguring.
