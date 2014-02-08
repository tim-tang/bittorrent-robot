# coding: utf-8
# Author tim.tang

from fabric.api import *
from fabric.operations import put, get
from fabric.colors import green, red
from monitor import Monitor

DEFAULT_HOST = ['173.255.253.43']
DEFAULT_USER = 'root'
DEFAULT_PASSWORD = 'tim.tang'

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


#def retrieve_remote_video(dir=DEFAULT_REMOTE_VIDEO_DIR):
#    dir_records = run("for i in %s*; do echo $i; done" % dir)
#    records = dir_records.replace("\r","").split("\n")
#    print (green(records))
#    """ 
#    Retrieve remote video to local dir 
#    """
#    for record in records:
#        retriever = Retriever(record)
#        threads.append(retriever)
#
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
