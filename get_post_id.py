from instagrapi import Client
from termcolor import colored
from colorama import Fore, Style
import time
import os

# Clear screen for better appearance
os.system("clear")

# Initialize Instagram client
GetMediaID = Client()

# Define ASCII Art and ABOUT information
STR = """
█▀▀█ █▀▀█ █▀▀ ▀▀█▀▀ 　 ▀█▀ █▀▀▄
█▄▄█ █  █ ▀▀█   █   　  █  █  █
█    ▀▀▀▀ ▀▀▀   ▀   　 ▄█▄ ▀▀▀
"""

ABOUT = [
    "Telegram   : @TG_BotCreator",
    "GitHub     : darkhacker34",
    "YouTube    : @TerminalBots",
    "WhatsApp   : +91 9605945309"
]

def print_stylish_about_box(about_lines):
    # Determine the max line length for consistent borders
    max_length = max(len(line) for line in about_lines)
    # Fancy border components
    top_border = f"╭{'─' * (max_length + 2)}╮"
    bottom_border = f"╰{'─' * (max_length + 2)}╯"

    # Print the top border, each line of ABOUT text centered within the border, and the bottom border
    print(colored(top_border, "cyan"))
    for line in about_lines:
        # Center each line in the box with padding spaces
        print(colored(f"│ {line.ljust(max_length)} │", "cyan"))
    print(colored(bottom_border, "cyan"))

def print_centered_box(text, box_length=None):
    # Find the length of the text for centering, or use the provided box length
    length = box_length if box_length else len(text)
    horizontal_border = f"╭{'─' * (length + 2)}╮"
    bottom_border = f"╰{'─' * (length + 2)}╯"

    # Center the label and display it with the box
    print(colored(horizontal_border, "light_yellow"))
    print(colored(f"│ {text.center(length)} │", "light_yellow"))
    print(colored(bottom_border, "light_yellow"))

# Displaying the ASCII Art aligned to the left
print(colored(STR, 'light_cyan'))

# Display "IG CMT BOT-V2.1" label centered within the ABOUT section
max_about_length = max(len(line) for line in ABOUT)  # Find the max length of ABOUT for consistent centering
print_centered_box("IG CMT BOT-V2.1", max_about_length)

# Directly display ABOUT information in a stylish bordered box (no extra space)
print_stylish_about_box(ABOUT)
time.sleep(0.5)

# Get Instagram post URL from user with input validation
post_url = input(f"\n{Fore.LIGHTWHITE_EX}{Style.BRIGHT}Paste Instagram Post URL: ")

# Validate that the URL is non-empty, is an Instagram URL, and specifically a post/reel/IGTV URL
while not post_url.strip() or "instagram.com" not in post_url or not any(path in post_url for path in ["/p/", "/reel/", "/tv/"]):
    if not post_url.strip():
        print(colored("You can't leave it empty. Please enter an Instagram POST URL.", "red"))
    else:
        print(colored("Wrong URL! Please enter a valid Instagram POST URL.", "red"))
    post_url = input(f"{Fore.LIGHTWHITE_EX}{Style.BRIGHT}Paste Instagram Post URL: ")

print(colored("\nTrying... to Get POST ID", 'green'))
time.sleep(2)

# Retrieve and display the post ID
try:
    postID = GetMediaID.media_pk_from_url(post_url)
except Exception as e:
    print(colored(f"Error retrieving post ID: {str(e)}", "red"))
    exit()
time.sleep(0.5)
print(f"\n{Fore.LIGHTYELLOW_EX}Post ID: {postID}\n\n{Fore.LIGHTGREEN_EX}{Style.BRIGHT}Copy{Fore.LIGHTWHITE_EX}{Style.BRIGHT} the Post ID, "
      f"{Fore.LIGHTGREEN_EX}then run {Fore.LIGHTBLACK_EX}python send_comment.py\n")
