# coding: utf-8
# Author tim.tang

import threading
from fabric.api import *
from retriever import Retriever
from fabric.colors import green, red
from time import sleep

class Monitor(threading.Thread):
    
    """"
    Default sleep interval
    """
    DEFAULT_MONITOR_INTERVAL = 60
    DEFAULT_REMOTE_VIDEO_DIR = '/root/Downloads/'

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        """ 
        Monitor remote transmission status 
        """
        while True:
            status = run("transmission-remote -l")
            #status = run("transmission-remote -l | awk '{print $1 $2 $8 $9}'| grep 'seeding' ")
            print (green(status))
            if status:
                print (green('Ready to stop seeding and synchronize with local.'))
                #TODO: make dict for torrent record
            sleep(DEFAULT_MONITOR_INTERVAL)


        def retrieve_remote_video(self, dir, records):
            for key, val in records.items():
                stop_seeding(key)
                retriever = Retriever(dir+ record)
                retriever.start()

        def stop_seeding(self, torrent_id):
            """
            Stop seeding for specified torrent.
            """
            run('transmission-remote -t %s -S' % torrend_id)
            run('transmission-remote -t %s -r' % torrend_id)
            print (green('Stop seeding and delete tansmission task - [%s].' %  torrend_id))

