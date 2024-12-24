#!/bin/bash

# Define color variables
no="\033[1;33m"
green="\033[1;32m"
white="\033[0m"
prpl="\033[0;36m"


# Function to display update progress
update_progress() {
    printf "%b\n★ ɪɢ ᴄᴍᴛ ʙᴏᴛ Updating...%b\n" "$green" "$white"
    sleep 2
}

# Function to handle repository update
update_repository() {
    if ! git pull origin IGBot 2>/dev/null; then
        printf "%b\nLocal changes detected that would be overwritten by merge.%b\n" "$prpl" "$white" >&2
        printf "%b\nWould you like to stash your changes and proceed with the update? (y/n): %b" "$prpl" "$white"
        read -r choice
        if [[ $choice == "y" ]]; then
            if ! git stash; then
                printf "%b\nError: Failed to stash changes.%b\n" "$prpl" "$white" >&2
                return 1
            fi
            if ! git pull origin IGBot; then
                printf "%b\nError: Failed to update the repository.%b\n" "$prpl" "$white" >&2
                git stash pop >/dev/null 2>&1
                return 1
            fi
            printf "%b\nReapplying stashed changes...%b\n" "$prpl" "$white"
            if ! git stash pop; then
                printf "%b\nError: Failed to reapply stashed changes.%b\n" "$prpl" "$white" >&2
                return 1
            fi
        else
            printf "%b\nAborting update. Please resolve local changes manually.%b\n" "$prpl" "$white" >&2
            return 1
        fi
    fi
}

# Function to display a thank you message
display_thank_you_message() {
    printf "%b\nᴛʜᴀɴᴋs ғᴏʀ ᴜsɪɴɢ ᴛʜɪs ᴛᴏᴏʟ.\nsᴜᴘᴘᴏʀᴛ ᴜs YT: @terminalbots\n%b" "$prpl" "$white"
}

# Main function
main() {
    update_progress
    if ! update_repository; then
        exit 1
    fi
    display_thank_you_message
}

# Execute main function
main
