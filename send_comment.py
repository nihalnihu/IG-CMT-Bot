from instagrapi import Client
import time
from termcolor import colored
bot = Client()
username = input(colored("Enter Your Instagram Username: ", 'blue' ))
password = input(colored("Enter You Instagram Password: ", 'blue'))
print("Trying... To Login")
bot.login(username, password)
print(f"{username} Login Success..")

POSTID = input(colored("Enter Instagram Post ID: ", 'cyan'))
commentmsg = input(colored("Enter Comment Message: ", 'yellow'))
cmtcount = input("How Meny Comment To Send: ")
i=1
while i <= int(cmtcount):
     bot.media_comment(POSTID, commentmsg)
     print(colored(f"{username} Sended {i} Comment", 'green'))
     time.sleep(10)
     i+=1
print(colored(f"Successfully Sended {cmtcount} Comments", 'green'))
