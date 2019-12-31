#!/bin/bash
mkdir /shared
cp .fbirc ~
echo "You will need to append the contents of add_to_smb.conf to /etc/samba/smb.conf"
echo "You will need to add 'python3 $(pwd)/play_slideshow.py' to the end of ~/.bashrc"
