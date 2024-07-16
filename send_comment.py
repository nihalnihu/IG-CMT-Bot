# Don't Forget To follow On Instagram @nihh____al

from instagrapi import Client
import time
from termcolor import colored
import getpass
from colorama import Fore, Style
import os
import sys

bot = Client()

START = """
         __     ______    
        /\ \   /\  ___\   
        \ \ \  \ \ \__ \  
         \ \_\  \ \_____\ 
          \/_/   \/_____/ 
        ______     __    __     ______  
       /\  ___\   /\ "-./  \   /\__  _\ 
       \ \ \____  \ \ \-./\ \  \/_/\ \/ 
        \ \_____\  \ \_\ \ \_\    \ \_\ 
         \/_____/   \/_/  \/_/     \/_/ 
  """                                                              
                  
SM = """
          . . . . . . . . . . . . . .. . 
          . Telegram  : @TG_BotCreator .
          . GitHub    : darkhacker34   .
          . YouTube   : @TerminalBots  .
          . WhatsApp  : +91 9605945309 .
          . . . . . . . . . . . . . . .."""

def print_in_box(text):

  length = len(text)
  
  horizontal_border = '+' + '-' * (length + 2) + '+'
  
  print(f"{Fore.LIGHTYELLOW_EX}             ", horizontal_border)
  print(f"              | {text} |")
  print("             ", horizontal_border)

os.system("clear")

print(colored(START, 'cyan'))
print_in_box("IG CMT BOT-V2.0 By")
print(SM)
time.sleep(1)
print(f"\n{Fore.LIGHTGREEN_EX}{Style.BRIGHT}✮ ᴅᴏɴ'ᴛ ᴡᴏʀʀʏ ᴡᴇ ᴄᴀɴ'ᴛ ꜱᴇᴇ ʏᴏᴜʀ ɪɴꜱᴛᴀɢʀᴀᴍ ᴜꜱᴇʀɴᴀᴍᴇ ᴏʀ ᴘᴀꜱꜱᴡᴏʀᴅ\nᴀɴᴅ ᴡᴇ ᴅᴏ ɴᴏᴛ ꜱᴛᴏʀᴇ ʏᴏᴜʀ ᴅᴇᴛᴀɪʟꜱ. ʏᴏᴜ ᴄᴀɴ ᴛʀᴜꜱᴛ ᴜꜱ.")
#Enter Username and Password
username = input(f"\n{Style.BRIGHT}{Fore.WHITE}Enter Your Instagram Username: ")
password = getpass.getpass(prompt=f"{Style.BRIGHT}{Fore.WHITE}Enter{Fore.LIGHTBLACK_EX} '{username}' {Fore.WHITE}Password: ")

print(colored("\nTrying... To Login", 'green'))
#Login
bot.login(username, password)
print(f"\n{Fore.LIGHTGREEN_EX}{username} Login Success...")
time.sleep(2)

#Enter Post ID
POSTID = input(colored(f"\n{Style.BRIGHT}Enter Instagram Post ID: ", 'cyan'))
time.sleep(.5)

#Enter Comment Message
commentmsg = input(f"\n{Style.BRIGHT}{Fore.LIGHTYELLOW_EX}Enter Comment Message: {Fore.LIGHTWHITE_EX}")
time.sleep(.5)

#Enter How Meny Comments You Want To Send (int)
cmtcount = input(f"\n{Fore.LIGHTYELLOW_EX}{Style.BRIGHT}How Meny Comment To Send: {Fore.LIGHTWHITE_EX}")
time.sleep(.5)

#Set A time to Deley in Seconds
deley = input(f"\n{Fore.LIGHTWHITE_EX}{Style.BRIGHT}How Meny Times you want to set delay? (in seconds): ")

print(f"\n       If You Want To Stop?{Fore.LIGHTBLACK_EX} CTRL+C\n{Fore.RESET}")
time.sleep(.5)

FIRST = """
\t  Started Commenting...
\t ──────────────────────
\t ғʀᴏᴍ        : {}
\t ᴘᴏsᴛ ɪᴅ     : {}
\t ᴄᴏᴍᴍᴇɴᴛ ᴍsɢ : {}
\t ᴛᴏᴛᴀʟ       : {}
\t ───────────────────────
"""

print(FIRST.format(username, POSTID, commentmsg, cmtcount))
R = "\t ʀᴇᴍᴀɪɴɪɴɢ   : {}"

#loop Started

i=1
while i <= int(cmtcount):
  bot.media_comment(POSTID, commentmsg)
  print(f"{R.format(int(cmtcount)-i)}", end='', flush=True)
  print(f"\n\t sᴜᴄᴄᴇss     : {i}\t", end='', flush=True)
  time.sleep(int(deley))
  print("\033[F", end='', flush=True)
  i+=1

print(f"\n\n\n         {Fore.LIGHTGREEN_EX}{Style.BRIGHT}Successfully Sended {cmtcount} Comments")