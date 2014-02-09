# coding: utf-8
# Author tim.tang

import os
import urllib
from fabric.api import *
from fabric.operations import put, get
from fabric.colors import green, red
from monitor import Monitor
from fabric.contrib.files import exists

DEFAULT_HOST = ['****']
DEFAULT_USER = '***'
DEFAULT_PASSWORD = '****'
DEFAULT_LOCAL_TORRENTS_DIR = './torrents/'
DEFAULT_REMOTE_TORRENTS_DIR = '/var/lib/transmission-daemon/info/torrents/'

def preparation():
    """ 
    Setup remote Linode VPS basic info
    """
    env.user = DEFAULT_USER
    env.hosts = DEFAULT_HOST
    env.password = DEFAULT_PASSWORD 


def monitor_torrent():
    """
    Monitoring remote transmission status
    """
    print (green('Monitoring remote transmission status.'))
    monitor = Monitor()
    monitor.start() 
    monitor.join()


def append_torrent():
    """
    Upload then append torrent to transmission download tasks
    """
    if not os.path.exists(DEFAULT_LOCAL_TORRENTS_DIR):
        print (red('Torrent directory -[%s] not exists!' % DEFAULT_LOCAL_TORRENTS_DIR))
        return

    local_torrents = os.listdir(DEFAULT_LOCAL_TORRENTS_DIR)
    for torrent in local_torrents:
        new_torrent = urllib.quote(torrent.encode('utf-8'))
        os.rename(DEFAULT_LOCAL_TORRENTS_DIR+torrent, DEFAULT_LOCAL_TORRENTS_DIR+new_torrent)
        remote_torrent_path = DEFAULT_REMOTE_TORRENTS_DIR + new_torrent
        if exists(remote_torrent_path):
            print (red('Torrent file - [%s] already exists!' % remote_torrent_path))
            continue
        local_torrent_path = DEFAULT_LOCAL_TORRENTS_DIR + new_torrent
        put(local_torrent_path, DEFAULT_REMOTE_TORRENTS_DIR)
        run("transmission-remote -a %s" % remote_torrent_path)


#def retrieve_remote_torrents(dir):
#    torrents = run("for i in %s*; do echo $i; done" % dir)
#    records = torrents.replace("\r","").split("\n")
#    print (green(records))
#    """ 
#    Retrieve remote video to local dir 
#    """
#    return records:
        

#def start_all():
#    """ 
#    Start all retrieve threads 
#    """
#    for proc in threads:
#        proc.start()
#
#def join_all():
#    """
#    Waits untill all the retrieve executed.
#    """
#    for proc in threads:
#        proc.join()
