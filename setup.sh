#!/bin/bash

# Define color codes
GREEN='\033[1;32m'
LIGHT_CYAN='\033[1;36m'
YELLOW='\033[1;33m'
BRIGHT_BLACK='\033[1;90m'
NC='\033[0m' # No color

# Function to set up a Python virtual environment
setup_virtualenv() {
  if [ ! -d "ig-cmt-bot-env" ]; then
    printf "${YELLOW}Creating virtual environment...${NC}\n"
    python3 -m venv ig-cmt-bot-env
  else
    printf "\n${YELLOW}Virtual environment already exists. Activating...${NC}\n"
  fi
}

# Function to install system dependencies
install_dependencies() {
  if command -v pkg &>/dev/null; then
    printf "\n${YELLOW}Installing dependencies in Termux...${NC}\n"
    pkg install python libjpeg-turbo -y
  elif command -v apt &>/dev/null; then
    printf "\n${YELLOW}Installing dependencies on Debian/Ubuntu...${NC}\n"
    sudo apt update
    sudo apt install python3 python3-pip libjpeg-dev python3-venv -y
  elif command -v dnf &>/dev/null; then
    printf "\n${YELLOW}Installing dependencies on Fedora...${NC}\n"
    sudo dnf install python3 python3-pip libjpeg-turbo-devel -y
  elif command -v pacman &>/dev/null; then
    printf "\n${YELLOW}Installing dependencies on Arch Linux...${NC}\n"
    sudo pacman -Syu python python-pip libjpeg-turbo --noconfirm
  elif command -v zypper &>/dev/null; then
    printf "\n${YELLOW}Installing dependencies on OpenSUSE...${NC}\n"
    sudo zypper install python3 python3-pip libjpeg8-devel
  else
    printf "\n${YELLOW}Unsupported environment. Please install dependencies manually.${NC}\n"
    exit 1
  fi
}

# Function to install Python libraries if not already installed
install_python_libs() {
  local packages=("Pillow" "instagrapi==2.0.0" "termcolor" "colorama")
  for package in "${packages[@]}"; do
    if ! python3 -c "import ${package%%==*}" &>/dev/null; then
      printf "\n${YELLOW}Installing ${package}...${NC}\n"
      pip install "${package}" --no-cache-dir
    else
      printf "\n${GREEN}${package} is already installed.${NC}\n"
    fi
  done
}

# Main script execution
clear
install_dependencies

clear
setup_virtualenv
source ig-cmt-bot-env/bin/activate

printf "\n${YELLOW}Upgrading pip...${NC}\n"
pip install --upgrade pip

printf "\n${YELLOW}Installing required Python libraries...${NC}\n"
install_python_libs

clear
printf "${LIGHT_CYAN}"
cat << "EOF"

╔══╦═══╗  ╔═══╦═╗╔═╦════╗ ╔══╗╔═══╦════╗
╚╣╠╣╔═╗║  ║╔═╗║║╚╝║║╔╗╔╗║ ║╔╗║║╔═╗║╔╗╔╗║
 ║║║║ ╚╝  ║║ ╚╣╔╗╔╗╠╝║║╚╝ ║╚╝╚╣║ ║╠╝║║╚╝
 ║║║║╔═╗  ║║ ╔╣║║║║║ ║║   ║╔═╗║║ ║║ ║║
╔╣╠╣╚╩═║  ║╚═╝║║║║║║ ║║   ║╚═╝║╚═╝║ ║║
╚══╩═══╝  ╚═══╩╝╚╝╚╝ ╚╝   ╚═══╩═══╝ ╚╝ 🅅 3.0

EOF
chmod +x send_comment.sh get_post_id.sh update.sh
printf "${YELLOW}Now Run ${BRIGHT_BLACK}./get_post_id.sh${YELLOW}${NC}\n"
