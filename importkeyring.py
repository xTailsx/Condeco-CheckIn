import keyring

keyring.set_password("condeco", "username", "USERNAME")
keyring.set_password("condeco", "password", "PASSWORD")

print("Saved credentials to Windows Credential Manager.")