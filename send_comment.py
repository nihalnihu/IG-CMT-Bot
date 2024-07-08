# Don't Forget To follow On Instagram @nihh____al 

from instagrapi import Client
import time
from termcolor import colored

bot = Client()

#Enter Username and Password 
username = input(colored("Enter Your Instagram Username: ", 'blue' ))
password = input(colored("Enter You Instagram Password: ", 'blue'))
print("Trying... To Login")

#Login
bot.login(username, password)
print(f"{username} Login Success..")

#Enter Post ID
POSTID = input(colored("Enter Instagram Post ID: ", 'cyan'))

#Enter Comment Message
commentmsg = input(colored("Enter Comment Message: ", 'yellow'))

#Enter How Meny Comments You Want To Send (int)
cmtcount = input("How Meny Comment To Send: ")

#Set A time to Deley in Seconds
deley = input("How Meny Times you want to set delay? (in seconds): ")

#loop Started
i=1
while i <= int(cmtcount):
     bot.media_comment(POSTID, commentmsg)
     print(colored(f"{username} Sended {i} Comment", 'green'))
     time.sleep(deley)
     i+=1
print(colored(f"Successfully Sended {cmtcount} Comments", 'green'))
