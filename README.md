# Alexa Whatsapp
Selenium powered whatsapp bot using this [awesome gentleman's library](https://github.com/mukulhase/WebWhatsAPI)

## Setup
If you're running python3 like most normal people, install Anaconda and create a python2 environment by following 
[these](https://stackoverflow.com/questions/24405561/how-to-install-2-anacondas-python-2-7-and-3-4-on-mac-os-10-9) instructions. 

Switch to your python2 environment by doing `source activate python2` or just `activate python2` if you're on Windows.


`pip install webwhatsapi` to install the dependencies.

Get a cleverbot key from [here](https://www.cleverbot.com/api/) and add it to `secret.py`
 
**Optional**: Get a youtube api key from [here](https://console.developers.google.com/apis) to fetch youtube results.

Run the script using `python index.py`.

Run the script on whatever browser you're not using so if you're on chrome run it on firefox, if you're using firefox normally just.. uh... stop using firefox.

Make sure to add a profile so you don't have to scan a QR code every time.

## Features
* Talk to alexa by mentioning her name or pinging her (it's actually cleverbot but shhh) and have her 
  respond anywhere including in group chats.
* Change the name she is listening for with `!respond <name>`.
* Fetch youtube video information and the link with `!youtube <video name>`.

## Limitations
* Your phone must be connected to the internet, if you're already using whatsapp 
that means the bot has to be running on a separate phone from the one you're using.

* Whatsapp, especially on old phones has a habit of not receiving messages unless you're active on your phone
meaning that there's a chance that leaving your phone with whatsapp running could eventually cause problems.

* The script must be running with an instance of firefox open at all times which makes it very difficult to host the script in a server.


## TODO:
- [ ] Convert to an event-based system than an infinite while loop for checking messages. 
Though this is more of a problem with the library rather than the implementation itself.

## Notes
If possible, this could work a little better with a mobile emulator as it would stop receiving messages less frequently. 
