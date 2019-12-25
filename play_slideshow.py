from subprocess import Popen
from subprocess import run
from time import sleep
from glob import glob
from functools import reduce

# These are customizable:

# This is the directory/folder that is watched for changes.
presentationdir = '/shared/Presentation/'
# This is the inotify command.
# inotifywait watches a directory (folder) and waits until one of the listed
# actions occurs.
inotifycmd = ['inotifywait','-e','create,modify,delete',presentationdir]
# Number of seconds to wait after first file change in the directory before
# restarting the slideshow
wait_time = 120
# File patterns to watch for.  * matches any characters
glob_strings = ['*.PNG','*.png','*.GIF','*.gif','*.JPG','*.jpg']

def sortedglob (globstr):
    '''
    Returns a sorted (alphabetically) list of files that match the string globstr.
    For example, if globstr is "*.jpg", returns a list of all files in the current
    directory that end in .jpg
    '''
    globlist = glob(globstr)
    globlist.sort()
    return(globlist)

def getfbicmd ():
    '''
    Creates an fbi command line.
    fbi is the Linux utility that displays images fullscreen without needing a window manager.
    The format is "fbi <files>" where <files> is one or more image file(s).
    First we generate a list of glob strings for possible image files, e.g. "*.jpg".
    Feel free to add your own if they are not covered here.
    Next, for each glob string, we get the files associated with it, and return it as a list.
    Next, we sort the entire list.
    Add the "fbi" command at the beginning of the line, and return the whole thing as a list.
    '''
    global presentationdir, glob_strings
    globlist = list(map(lambda x: presentationdir + x, glob_strings))
    filelist = reduce(lambda x, y: x + y, (map(sortedglob, globlist)))
    filelist.sort()
    filelist.insert(0, 'fbi')
    return(filelist)

def slideshow ():
    '''
    Build the fbi command using getfbicmd, and start the process using Popen.
    The process number is stored in myproc.
    Loop forever:  block on inotifycmd, which means wait until something interesting
    happens in that directory/folder.
    Once something happens, wait for 2 minutes (120 seconds) to allow for changes to settle down.
    (It is assumed that multiple files will change as files are added/removed.  Rather than
     restart for each new file change, we wait for 2 minutes to allow all changes to take effect.)
    After 2 minutes, we kill the old fbi command and create a new one and launch it.
    '''
    global inotifycmd, wait_time
    myproc = Popen(getfbicmd())
    while (True):
        run(inotifycmd)
        sleep(wait_time)
        myproc.terminate()
        myproc = Popen(getfbicmd())

slideshow()
