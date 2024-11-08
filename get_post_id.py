from instagrapi import Client
from termcolor import colored
from colorama import Fore, Style
import time

GetMediaID = Client()

STR = """

░█▀▀█ █▀▀ ▀▀█▀▀ 　
░█─▄▄ █▀▀ ──█── 　
░█▄▄█ ▀▀▀ ──▀── 　

░█▀▀█ █▀▀█ █▀▀ ▀▀█▀▀ 　 ▀█▀ █▀▀▄
░█▄▄█ █──█ ▀▀█ ──█── 　 ░█─ █──█
░█─── ▀▀▀▀ ▀▀▀ ──▀── 　 ▄█▄ ▀▀▀─
"""
def print_in_box(text):
    # Determine the length of the text
    length = len(text)
    # Create the top and bottom border of the box
    horizontal_border = '+' + '-' * (length + 2 - 5) + '+'        # Print the box with the text inside
    print(f"{Fore.LIGHTYELLOW_EX}    {horizontal_border}")        print(f"   | {text} |")
    print(f"    {horizontal_border}")                         
ABOUT = """
    . . . . . . . . . . . . . . . . . . . . . .
    . Telegram   : @ATG_BotCreator   .
    . GitHub     : darkhacker34    .
    . YouTube    : @TerminalBots    .
    . WhatsApp   : +91 9605945309   .
    . . . . . . . . . . . . . . . . . . . . . .
"""

print(colored(STR, 'light_cyan'))
print_in_box(f"{Fore.LIGHTYELLOW_EX}IG CMT BOT-V2.0 By")
print(colored(ABOUT, 'cyan'))
time.sleep(.5)

post_url = input(f"\n{Fore.LIGHTWHITE_EX}{Style.BRIGHT}Paste Instagram Post URL: ")
print(colored("\nGetting...", 'green'))
time.sleep(2)
postID = GetMediaID.media_pk_from_url(post_url)
time.sleep(.5)
print(f"\n{Fore.LIGHTYELLOW_EX}Post ID: {postID}\n\n{Fore.LIGHTGREEN_EX}{Style.BRIGHT}Copy{Fore.LIGHTWHITE_EX}{Style.BRIGHT} The Post ID, {Fore.LIGHTGREEN_EX}Run {Fore.LIGHTBLACK_EX}python send_comment.py\n")
