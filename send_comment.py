# Don't Forget To follow On Instagram @nihh____al 

from instagrapi import Client
import time
from termcolor import colored

bot = Client()

#Enter Username and Password 
username = input(colored("\nEnter Your Instagram Username: ", 'blue' ))
password = input(colored("Enter You Instagram Password: ", 'blue'))
print("\nTrying... To Login")

#Login
bot.login(username, password)
print(f"\n{username} Login Success..")
time.sleep(2)

#Enter Post ID
POSTID = input(colored("\nEnter Instagram Post ID: ", 'cyan'))
time.sleep(.5)

#Enter Comment Message
commentmsg = input(colored("\nEnter Comment Message: ", 'yellow'))
time.sleep(.5)

#Enter How Meny Comments You Want To Send (int)
cmtcount = input("\nHow Meny Comment To Send: ")
time.sleep(.5)

#Set A time to Deley in Seconds
deley = input("\nHow Meny Times you want to set delay? (in seconds): ")

print(f"\nStarting... Send {commentmsg} To Post ID: {POSTID} ")
time.sleep(.5)

#loop Started
i=1
while i <= int(cmtcount):
     bot.media_comment(POSTID, commentmsg)
     print(colored(f"{username} Sended {i} Comment", 'green'))
     time.sleep(deley)
     i+=1
print(colored(f"Successfully Sended {cmtcount} Comments", 'green'))