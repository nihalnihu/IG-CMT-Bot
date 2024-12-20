# Define color codes
GREEN='\033[1;32m'
LIGHT_CYAN='\033[1;36m'
YELLOW='\033[1;33m'
BRIGHT_BLACK='\033[1;90m'
NC='\033[0m' # No color

# Function to create virtual environment and install packages
setup_virtualenv() {
  # Create a virtual environment if it doesn't exist
  if [ ! -d "ig-cmt-bot-env" ]; then
    echo -e "\n${YELLOW}Creating a Python virtual environment...${NC}"
    python3 -m venv ig-cmt-bot-env
  else
    echo -e "\n${YELLOW}Virtual environment already exists. Activating...${NC}"
  fi

}

# Function to install dependencies
install_dependencies() {
  if command -v pkg &>/dev/null; then
    # Termux environment
    echo -e "\n${YELLOW}Installing python...${NC}"
    pkg install python -y

    echo -e "\n${YELLOW}Installing libjpeg-turbo...${NC}"
    pkg install libjpeg-turbo -y

  elif command -v apt &>/dev/null; then
    # Debian/Ubuntu/Kali-based Linux
    echo -e "\n${YELLOW}Installing python...${NC}"
    sudo apt update
    sudo apt install python3 python3-pip libjpeg-dev python3-venv -y

  elif command -v dnf &>/dev/null; then
    # Fedora-based Linux
    echo -e "\n${YELLOW}Installing python...${NC}"
    sudo dnf install python3 python3-pip libjpeg-turbo-devel -y

  elif command -v pacman &>/dev/null; then
    # Arch-based Linux
    echo -e "\n${YELLOW}Installing python...${NC}"
    sudo pacman -Syu python python-pip libjpeg-turbo --noconfirm

  elif command -v zypper &>/dev/null; then
    # OpenSUSE-based Linux
    echo -e "\n${YELLOW}Installing python...${NC}"
    sudo zypper install python3 python3-pip libjpeg8-devel

  else
    echo -e "\n${YELLOW}Unsupported environment. Please install dependencies manually.${NC}"
    exit 1
  fi
}

# Install dependencies
clear
install_dependencies

# Setup virtual environment
clear
setup_virtualenv
# Activate the virtual environment
source ig-cmt-bot-env/bin/activate

# Upgrade pip and install required packages
echo -e "\n${YELLOW}Upgrading pip...${NC}"
pip install --upgrade pip

echo -e "\n${YELLOW}Installing Libraries...${NC}"
pip install Pillow --no-cache-dir
pip install instagrapi==2.0.0
pip install termcolor
pip install colorama

# Final clear and display success message with large text
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
chmod +x send_comment.sh get_post_id.sh
# Final prompt to run get_post_id.py
echo -e "${YELLOW}Now Run ${BRIGHT_BLACK}bash get_post_id.sh${YELLOW}${NC}\n"
