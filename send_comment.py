from instagrapi import Client
import time
from termcolor import colored
import getpass
from colorama import Fore, Style
import os
import sys

bot = Client()

# Welcome banner
START = """
                      ▀█▀ █▀▀█
                       █  █ ▄▄
                      ▄█▄ █▄▄█

                   █▀▀█ █▀▄▀█ ▀▀█▀▀
                   █    █ █ █   █
                   █▄▄█ █   █   █
"""

# Social media info
SM = [
    "Telegram  : @TG_BotCreator",
    "GitHub    : darkhacker34",
    "YouTube   : @TerminalBots",
    "WhatsApp  : +91 9605945309"
]

# Print centered box with dynamic width
def print_centered_box(text):
    max_length = max(len(line) for line in SM + [text])
    horizontal_border_top = '╭' + '─' * (max_length + 4) + '╮'
    horizontal_border_bottom = '╰' + '─' * (max_length + 4) + '╯'
    padding_text = ' ' * ((max_length - len(text)) // 2)
    print(f"{Fore.LIGHTYELLOW_EX}           {horizontal_border_top}")
    print(f"           │{padding_text}  {text}  {padding_text} │")
    print(f"           {horizontal_border_bottom}{Fore.RESET}")

# Print social media box
def print_sm_box(sm_lines):
    max_length = max(len(line) for line in sm_lines)
    horizontal_border_top = '╭' + '─' * (max_length + 4) + '╮'
    horizontal_border_bottom = '╰' + '─' * (max_length + 4) + '╯'
    print(f"{Fore.LIGHTCYAN_EX}           {horizontal_border_top}")
    for line in sm_lines:
        padding = ' ' * (max_length - len(line))
        print(f"           │  {line}{padding}  │")
    print(f"           {horizontal_border_bottom}{Fore.RESET}")

# Clear console based on OS
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

clear_console()

# Display welcome message
print(colored(START, 'cyan'))
print_centered_box("IG CMT BOT-V2.1")
print_sm_box(SM)
time.sleep(1)
print(f"\n{Fore.LIGHTGREEN_EX}{Style.BRIGHT}✮ ᴅᴏɴ'ᴛ ᴡᴏʀʀʏ ᴡᴇ ᴄᴀɴ'ᴛ ꜱᴇᴇ ʏᴏᴜʀ ɪɴꜱᴛᴀɢʀᴀᴍ ᴜꜱᴇʀɴᴀᴍᴇ ᴏʀ ᴘᴀꜱꜱᴡᴏʀᴅ\nᴀɴᴅ ᴡᴇ ᴅᴏ ɴᴏᴛ ꜱᴛᴏʀᴇ ʏᴏᴜʀ ᴅᴇᴛᴀɪʟꜱ. ʏᴏᴜ ᴄᴀɴ ᴛʀᴜꜱᴛ ᴜꜱ.")

# Prompt for credentials
username = input(f"\n{Style.BRIGHT}{Fore.WHITE}Enter Your Instagram Username: ")
password = getpass.getpass(prompt=f"{Style.BRIGHT}{Fore.WHITE}Enter{Fore.LIGHTBLACK_EX} '{username}' {Fore.WHITE}Password: ")

# Login attempt with improved error handling
print(colored("\nAttempting to login...", 'green'))
try:
    bot.login(username, password)
    print(f"\n{Fore.LIGHTGREEN_EX}{username} Login Successful...")
    time.sleep(2)
except Exception as e:
    error_message = str(e).lower()
    if "credentials" in error_message or "password" in error_message:
        print(f"\n{Style.BRIGHT}{Fore.RED}Error: Invalid password! Please Double-Check Your Password.")
    elif "username" in error_message:
        print(f"\n{Style.BRIGHT}{Fore.RED}Error: Entered username '{username}' is incorrect!")
    else:
        print(f"\n{Style.BRIGHT}{Fore.RED}Error: {str(e)}")  # For any other unexpected errors
    sys.exit(1)

# Prompt for post ID
POSTID = input(colored(f"\n{Style.BRIGHT}Enter Instagram Post ID: ", 'cyan'))
time.sleep(0.5)

# Prompt for comment message
commentmsg = input(f"\n{Style.BRIGHT}{Fore.LIGHTYELLOW_EX}Enter Comment Message: {Fore.LIGHTWHITE_EX}")
time.sleep(0.5)

# Prompt for comment count
while True:
    try:
        cmtcount = int(input(f"\n{Fore.LIGHTYELLOW_EX}{Style.BRIGHT}How Many Comments To Send: {Fore.LIGHTWHITE_EX}"))
        break
    except ValueError:
        print(f"{Style.BRIGHT}{Fore.RED}Invalid Input, Please Enter A Valid Comment Count.")

time.sleep(0.5)

# Prompt for delay between comments
while True:
    try:
        deley = int(input(f"\n{Fore.LIGHTWHITE_EX}{Style.BRIGHT}How Many Seconds to Delay: "))
        break
    except ValueError:
        print(f"{Style.BRIGHT}{Fore.RED}Invalid Input, Please Enter A Valid Delay Time (In seconds).")

print(f"\n       If You Want To Stop?{Fore.LIGHTBLACK_EX} CTRL+C\n{Fore.RESET}")
time.sleep(0.5)

# Rounded box display for starting info
def print_rounded_box(content):
    lines = content.split('\n')
    max_length = max(len(line) for line in lines)
    top_border = '╭' + '─' * (max_length + 4) + '╮'
    bottom_border = '╰' + '─' * (max_length + 4) + '╯'
    print(f"{Fore.LIGHTYELLOW_EX}{top_border}")
    for line in lines:
        padding = ' ' * (max_length - len(line))
        print(f"│  {line}{padding}  │")
    print(f"{bottom_border}{Fore.RESET}")

# Start display with user details
FIRST = """
  ғʀᴏᴍ        : {}
  ᴘᴏsᴛ ɪᴅ     : {}
  ᴄᴏᴍᴍᴇɴᴛ ᴍsɢ : {}
  ᴛᴏᴛᴀʟ       : {}
"""
print_rounded_box(FIRST.format(username, POSTID, commentmsg, cmtcount))

R = "\t ʀᴇᴍᴀɪɴɪɴɢ   : {}"

# Loop for sending comments with error handling
i = 1
while i <= int(cmtcount):
    try:
        bot.media_comment(POSTID, commentmsg)
        print(f"{R.format(int(cmtcount)-i)}", end='', flush=True)
        print(f"\n\t sᴜᴄᴄᴇss     : {i}\t", end='', flush=True)
        time.sleep(int(deley))
        print("\033[F", end='', flush=True)
        i += 1
    except Exception as e:
        print(f"\n{Style.BRIGHT}{Fore.RED}Error while sending comment: {str(e)}")
        break

print(f"\n\n\n         {Fore.LIGHTGREEN_EX}{Style.BRIGHT}Successfully Sent {cmtcount} Comments")
