from instagrapi import Client
from termcolor import colored

getbot = Client()
username = input("Enter Username: ")
password = input("Enter Password: ")

getbot.login(username, password)

post_url = input("Paste Instagram Post URL: ")
postID = getbot.media_pk_from_url(post_url)
print(colored(f"Post ID: {postID}", 'green'))
