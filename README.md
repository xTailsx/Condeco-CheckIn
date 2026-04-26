# Condeco Check-In Script

A Python script that automates checking in to Condeco desk bookings using Playwright and Chromium.

## Prerequisites

- Python 3.10+
- pip

## Installation

```bash
pip install keyring playwright
playwright install chromium
Setup
1. Save credentials to Windows Credential Manager
Run the importkeyring.py script once to store your Condeco credentials securely in Windows Credential Manager:

python importkeyring.py
IMPORTANT: Delete importkeyring.py immediately after running it. The script contains your password in plaintext and should not be kept on disk or committed to version control.

Remove-Item importkeyring.py
2. Verify credentials are stored
You can confirm your credentials were saved by checking Windows Credential Manager:

Open Control Panel > Credential Manager > Windows Credentials
Look for the Condeco entry under Generic Credentials
Usage
python condeco_checkin.py
The script will:

Retrieve your credentials from Windows Credential Manager via keyring
Launch a Chromium browser window (visible, not headless)
Log in to Condeco and check in to your booking
NOTE: If credentials are missing from Windows Credential Manager, the script will raise a ValueError and exit. Re-run the setup steps above to fix this.

Files
File	Description
condeco_checkin.py	Main check-in script
importkeyring.py	One-time credential setup script — delete after use
Security
Credentials are stored in Windows Credential Manager, not in files or environment variables.
importkeyring.py contains a plaintext password and must be deleted after the initial setup.
Do not commit importkeyring.py to version control. Add it to .gitignore as a safeguard.
