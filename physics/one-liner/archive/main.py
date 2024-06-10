from instagrapi import Client
from instagrapi.exceptions import TwoFactorRequired
import os
import json

USERNAME = os.getenv("INSTA_USERNAME")
PASSWORD = os.getenv("INSTA_PASSWORD")


SESSION_FILE = "session.json"


cl = Client()





def login(username, password):
    CODE = input("Enter the 2FA code: ")
    cl.login(username, password, verification_code=CODE)
    
    if cl.user_id:
        print("Login successful!")
    else:
        print("Login failed.")

def save_session(client, filepath):
    with open(filepath, "w") as f:
        json.dump(client.get_settings(), f)
    print("Session saved!")

def load_session(client, filepath):
    with open(filepath, "r") as f:
        settings = json.load(f)
    client.set_settings(settings)
    print("Session loaded!")


## add progress bar while login happening



if os.path.exists(SESSION_FILE):
    load_session(cl, SESSION_FILE)
else:
    login(USERNAME, PASSWORD)
    save_session(cl, SESSION_FILE)



print(cl.account_info().dict())
