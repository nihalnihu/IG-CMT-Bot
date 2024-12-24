from instagrapi import Client
import time
from termcolor import colored
import getpass
from colorama import Fore, Style
import os
import sys
import random
import subprocess

bot = Client()

START = """
                      ▀█▀ █▀▀█
                       █  █ ▄▄
                      ▄█▄ █▄▄█

                   █▀▀█ █▀▄▀█ ▀▀█▀▀
                   █    █ █ █   █
                   █▄▄█ █   █   █
"""

SM = [
    "Telegram  : @TG_BotCreator",
    "GitHub    : darkhacker34",
    "YouTube   : @TerminalBots",
    "WhatsApp  : +91 9605945309"
]

def print_centered_box(text):
    max_length = max(len(line) for line in SM + [text])
    horizontal_border_top = '╭' + '─' * (max_length + 4) + '╮'
    horizontal_border_bottom = '╰' + '─' * (max_length + 4) + '╯'
    padding_text = ' ' * ((max_length - len(text)) // 2)
    print(f"{Fore.LIGHTYELLOW_EX}           {horizontal_border_top}")
    print(f"           │{padding_text}  {text}  {padding_text} │")
    print(f"           {horizontal_border_bottom}{Fore.RESET}")

def print_sm_box(sm_lines):
    max_length = max(len(line) for line in sm_lines)
    horizontal_border_top = '╭' + '─' * (max_length + 4) + '╮'
    horizontal_border_bottom = '╰' + '─' * (max_length + 4) + '╯'
    print(f"{Fore.LIGHTCYAN_EX}           {horizontal_border_top}")
    for line in sm_lines:
        padding = ' ' * (max_length - len(line))
        print(f"           │  {line}{padding}  │")
    print(f"           {horizontal_border_bottom}{Fore.RESET}")

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

clear_console()

print(colored(START, 'cyan'))
print_centered_box("IG CMT BOT-V3.0")
print_sm_box(SM)
time.sleep(1)
print(f"\n{Fore.LIGHTGREEN_EX}{Style.BRIGHT}✮ ᴅᴏɴ'ᴛ ᴡᴏʀʀʏ ᴡᴇ ᴄᴀɴ'ᴛ ꜱᴇᴇ ʏᴏᴜʀ ɪɴꜱᴛᴀɢʀᴀᴍ ᴜꜱᴇʀɴᴀᴍᴇ ᴏʀ ᴘᴀꜱꜱᴡᴏʀᴅ\nᴀɴᴅ ᴡᴇ ᴅᴏ ɴᴏᴛ ꜱᴛᴏʀᴇ ʏᴏᴜʀ ᴅᴇᴛᴀɪʟꜱ. ʏᴏᴜ ᴄᴀɴ ᴛʀᴜꜱᴛ ᴜꜱ.\n")

while True:
    username = input(f"\n{Style.BRIGHT}{Fore.WHITE}Enter Your Instagram Username: ").strip()
    if username: 
        break  
    print(f"{Style.BRIGHT}{Fore.RED}Username cannot be empty. Please enter a valid username.")

while True:
    password = getpass.getpass(prompt=f"{Style.BRIGHT}{Fore.WHITE}Enter{Fore.LIGHTBLACK_EX} '{username}' {Fore.WHITE}Password: ").strip()
    if password:
        break 
    print(f"{Style.BRIGHT}{Fore.RED}Password cannot be empty. Please enter a valid password.")

print("\nAttempting to login...")
try:
    bot.login(username, password)
    print(f"\n{Fore.LIGHTGREEN_EX}{username} Login Successful...")
    time.sleep(.5)
except Exception as e:
    error_message = str(e).lower()
    if "credentials" in error_message or "password" in error_message:
        print(f"\n{Style.BRIGHT}{Fore.RED}Error: Invalid password! Please Double-Check Your Password.")
    elif "username" in error_message:
        print(f"\n{Style.BRIGHT}{Fore.RED}Error: Entered username '{username}' is incorrect!")
    else:
        print(f"\n{Style.BRIGHT}{Fore.RED}Error: {str(e)}")  
    sys.exit(1)

print(f"\n{Fore.YELLOW}!Run {Fore.LIGHTBLACK_EX}'./get_post_id.sh'{Fore.YELLOW} if You Don't Have Target POST ID!{Fore.RESET}")

while True:
    POSTID = input(f"\n{Fore.LIGHTCYAN_EX}Enter Instagram Post ID: {Fore.RESET}").strip()
    if not POSTID.isdigit():
        print(f"{Style.BRIGHT}{Fore.RED}Invalid Post ID. Please enter a valid POST ID.")
    else:
        try:
            bot.media_info(POSTID)
            break 
        except Exception:
            print(f"{Style.BRIGHT}{Fore.RED}Invalid Post ID. Please enter a valid POST ID.")
    time.sleep(0.3)

while True:
    try:
        comment_types_input = input(f"\n{Style.BRIGHT}{Fore.BLUE}How Many Type Comments You Want to Set (Press Enter to Skip): {Fore.RESET}").strip()
        if not comment_types_input:  # If input is empty
            print(f"{Fore.LIGHTYELLOW_EX}Randomly Select Comments from 'comments.txt'...{Fore.RESET}")
            if not os.path.exists('comments.txt'):
                print(f"{Style.BRIGHT}{Fore.RED}Error: 'comments.txt' file not found in the current directory!{Fore.RESET}")
                sys.exit(1)
            with open('comments.txt', 'r', encoding='utf-8') as file:
                comments = [line.strip() for line in file if line.strip()]
            if not comments:
                print(f"{Style.BRIGHT}{Fore.RED}Error: 'comments.txt' is empty! Please add comments to the file and try again.{Fore.RESET}")
                sys.exit(1)
            break

        comment_types = int(comment_types_input)
        if comment_types > 0:
            comments = []
            for i in range(1, comment_types + 1):
                while True:
                    comment = input(f"\n{Style.BRIGHT}{Fore.CYAN}Enter Comment Message {i}: {Fore.RESET}").strip()
                    if comment:
                        comments.append(comment)
                        break
                    else:
                        print(f"{Style.BRIGHT}{Fore.RED}You can't leave it empty. Please Enter a Comment Message.")
            break
    except ValueError:
        print(f"{Style.BRIGHT}{Fore.RED}Invalid Input. Please enter a valid number of comment types.")

while True:
    try:
        cmtcount = int(input(f"\n{Fore.LIGHTYELLOW_EX}{Style.BRIGHT}How Many Comments To Send: {Fore.LIGHTWHITE_EX}"))
        break
    except ValueError:
        print(f"{Style.BRIGHT}{Fore.RED}Invalid Input, Please Enter A Valid Comment Count.")

time.sleep(0.5)

while True:
    try:
        deley = int(input(f"\n{Fore.LIGHTWHITE_EX}{Style.BRIGHT}How Many Seconds to Delay: "))
        if not deley >= 30:
            print(f"{Style.BRIGHT}{Fore.RED}⚠️ Instagram Alert: The minimum delay time is 30 seconds. Please follow the limits to protect your account! ⏳")
        else:
            break
    except ValueError:
        print(f"{Style.BRIGHT}{Fore.RED}Invalid Input, Please Enter A Valid Delay Time (In seconds).")

print(f"\n       If You Want To Stop?{Fore.LIGHTBLACK_EX} CTRL+C\n{Fore.RESET}")
time.sleep(0.5)


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

# Initial box
FIRST = f"""
  ғʀᴏᴍ             : {username}
  ᴘᴏsᴛ ɪᴅ          : {POSTID}
  ᴛᴏᴛᴀʟ            : {cmtcount}
"""
print_rounded_box(FIRST)

# Loop to send comments
i = 1
while i <= cmtcount:
    try:
        commentmsg = random.choice(comments)
        bot.media_comment(POSTID, commentmsg)
        remaining = cmtcount - i

        # Clear previous output and move to the next line
        sys.stdout.write("\033[F\033[K")  # Move up one line and clear

        # Dynamically update rounded box with Remaining, Success, and Comment on a new line
        BOX_CONTENT = f"""
  Remaining: {remaining}
  Success: {i}
  Comment: {commentmsg}
"""
        print_rounded_box(BOX_CONTENT)

        if remaining > 0:
            time.sleep(deley)

        i += 1  # Increment the counter

    except Exception as e:
        print(f"\nError while sending comment: {str(e)}")
        break

# Print final summary in a new rounded box
FINAL = f"Successfully Sent {i - 1} Comments"
print_rounded_box(FINAL)
