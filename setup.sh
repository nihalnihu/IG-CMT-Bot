#!/bin/bash

# Define color codes
GREEN='\033[1;32m'
LIGHT_CYAN='\033[1;36m'
YELLOW='\033[1;33m'
BRIGHT_BLACK='\033[1;90m'
NC='\033[0m' # No color

# Function to install packages
install_packages() {
  echo -e "${YELLOW}Installing required packages...${NC}"
  
  if [ "$TERMUX" = "true" ]; then
    echo -e "${YELLOW}Detected Termux.${NC}"
    pkg install python -y
    pkg install libjpeg-turbo -y
  elif [ "$OS" = "debian" ]; then
    echo -e "${YELLOW}Detected Debian/Ubuntu.${NC}"
    sudo apt update
    sudo apt install python3 python3-pip libjpeg-dev -y
  elif [ "$OS" = "fedora" ]; then
    echo -e "${YELLOW}Detected Fedora.${NC}"
    sudo dnf install python3 python3-pip libjpeg-turbo-devel -y
  else
    echo -e "${YELLOW}Unsupported platform. Exiting.${NC}"
    exit 1
  fi
}

# Function to install Python libraries
install_python_libraries() {
  echo -e "${YELLOW}Installing Python libraries...${NC}"
  pip install Pillow --no-cache-dir
  pip install instagrapi==2.0.0
  pip install termcolor
  pip install colorama
}

# Detect platform
if [ -n "$(command -v pkg)" ]; then
  TERMUX="true"
elif [ -f /etc/os-release ]; then
  source /etc/os-release
  if [[ "$ID" == "ubuntu" || "$ID" == "debian" ]]; then
    OS="debian"
  elif [[ "$ID" == "fedora" ]]; then
    OS="fedora"
  fi
else
  echo -e "${YELLOW}Could not detect the platform. Exiting.${NC}"
  exit 1
fi

# Clear screen and start installation
clear
install_packages
install_python_libraries

# Display success message
clear
echo -e "${LIGHT_CYAN}"

cat << "EOF"

╔══╦═══╗  ╔═══╦═╗╔═╦════╗ ╔══╗╔═══╦════╗
╚╣╠╣╔═╗║  ║╔═╗║║╚╝║║╔╗╔╗║ ║╔╗║║╔═╗║╔╗╔╗║
 ║║║║ ╚╝  ║║ ╚╣╔╗╔╗╠╝║║╚╝ ║╚╝╚╣║ ║╠╝║║╚╝
 ║║║║╔═╗  ║║ ╔╣║║║║║ ║║   ║╔═╗║║ ║║ ║║
╔╣╠╣╚╩═║  ║╚═╝║║║║║║ ║║   ║╚═╝║╚═╝║ ║║
╚══╩═══╝  ╚═══╩╝╚╝╚╝ ╚╝   ╚═══╩═══╝ ╚╝ 🅅2.1

EOF

echo -e "\n${GREEN}All Dependencies Have Been Installed Successfully!${NC}\n"
echo -e "${YELLOW}Now Run ${BRIGHT_BLACK}python get_post_id.py${YELLOW}${NC}\n"
