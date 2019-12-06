from subprocess import Popen
from subprocess import run
from time import sleep
from glob import glob
from functools import reduce

presentationdir = '/shared/Presentation/'
inotifycmd = ['inotifywait','-e','create,modify,delete',presentationdir]


def sortedglob (globstr):
    globlist = glob(globstr)
    globlist.sort()
    return(globlist)

def getfbicmd ():
    globlist = list(map(lambda x: presentationdir + x, ['*.PNG','*.png','*.GIF','*.gif','*.JPG','*.jpg']))
    filelist = reduce(lambda x, y: x + y, (map(sortedglob, globlist)))
    filelist.sort()
    filelist.insert(0, 'fbi')
    return(filelist)

def slideshow ():
    myproc = Popen(getfbicmd())
    while (True):
        run(inotifycmd)
        sleep(120)
        myproc.terminate()
        myproc = Popen(getfbicmd())

slideshow()
