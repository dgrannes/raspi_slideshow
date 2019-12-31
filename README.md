# raspi_slideshow
Files for making a slideshow program on the raspberry pi

Files:
- .fbirc: gets copied to home directory:
` cp .fbirc ~`
- monitor_o*: files to turn monitor on and off (both bash and csh versions)
- play\_slideshow.py: Python file that runs the slideshow
- README.md: this file
- LICENSE: description of license for this code
- setup.bash: script that attempts to get some files in the right place
- add\_to\_smb.conf: a file to be appended to the end of /etc/samba/smb.conf
- crontab\_example.pi: an example crontab file. Edit it to change the times/dates for on/off, and execute
` crontab FILE` where FILE is the name of the file, e.g. crontab\_example.pi
 
