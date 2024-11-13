no="\033[1;33m"

echo -e ${no}"\n\tPlease Subscribe My YouTube Channel"
sleep 3

yt_url="https://youtube.com/@terminalbots"
termux-open-url "$yt_url"

green="\033[1;32m"
white="\033[0m"
prpl="\033[0;36m"
echo -e ${green}"\n★ ɪɢ ᴄᴍᴛ ʙᴏᴛ Updating..."
echo -e ${white}
sleep 2
git pull origin IGBot
echo -e ${prpl}"\nᴛʜᴀɴᴋs ғᴏʀ ᴜsɪɴɢ ᴛʜɪs ᴛᴏᴏʟ.\n       sᴜᴘᴘᴏʀᴛ ᴜs\n"

