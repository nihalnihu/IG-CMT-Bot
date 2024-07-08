from instagrapi import Client
from termcolor import colored
import time

GetMediaID = Client()

print("\nStarting...")
time.sleep(3)

post_url = input(colored("\nPaste Instagram Post URL: ", 'light_grey'))
print(colored("\nGetting...", 'green'))
time.sleep(2)
postID = GetMediaID.media_pk_from_url(post_url)
time.sleep(.5)
print(colored(f"\nPost ID: {postID}\n", 'light_blue'))