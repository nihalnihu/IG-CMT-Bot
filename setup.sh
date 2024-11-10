#!/bin/bash

# Define color codes
GREEN='\033[1;32m'
YELLOW='\033[1;33m'
BRIGHT_BLACK='\033[1;90m'
NC='\033[0m' # No color

# Install required packages
clear
echo -e "\n${YELLOW}Installing git...${NC}"
pkg install git -y

clear
echo -e "\n${YELLOW}Installing python...${NC}"
pkg install python -y

clear
echo -e "\n${YELLOW}Installing libjpeg-turbo...${NC}"
pkg install libjpeg-turbo -y

# Install Python packages with pip

clear
echo -e "\n${YELLOW}Installing Libraries...${NC}"
pip install Pillow --no-cache-dir
pip install instagrapi==2.0.0
pip install termcolor
pip install colorama

# Success message
clear
echo -e "\n\n${GREEN}All dependencies have been installed successfully!${NC}\n"

# Final prompt to run get_post_id.py
echo -e "${YELLOW}Now run ${BRIGHT_BLACK}python get_post_id.py${YELLOW}${NC}\n"
