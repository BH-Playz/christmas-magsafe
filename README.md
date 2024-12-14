# christmas-magsafe
Christmas Magsafe blinking script
## Preperation
You NEED Battery installed to use this script.

1. Install brew (if not already installed)
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
2. Install battery:
```
brew install batt
sudo brew services start batt
```
3. Install python

Now open the application and enter your password to run as sudo.
And your MagSafe LED should be blinking Green and Orange!

TO ENSURE THAT IT WON'T BE STUCK ON ORANGE/GREEN, ALWAYS STOP THE SCRIPT WITH CTRL+C.
