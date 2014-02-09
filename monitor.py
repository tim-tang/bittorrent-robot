# coding: utf-8
# Author tim.tang

import threading
import sys
from fabric.api import *
from retriever import Retriever
from fabric.colors import green, red
from time import sleep
from fabric.contrib.files import exists

class Monitor(threading.Thread):
    
    """"
    Default sleep interval 60 seconds.
    """
    DEFAULT_MONITOR_INTERVAL = 60
    DEFAULT_REMOTE_VIDEO_DIR = '/root/Downloads/'
    TORRENT_STATUS = 'Seeding'
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        """ 
        Monitor remote transmission status 
        """
        while True:
            status = run("transmission-remote -l")
            max_line = run("transmission-remote -l|awk 'END{print NR}'")
            seeding_torrents = run("transmission-remote -l|awk 'NR>1 && NR<%s {print $0}'" % max_line)
            if seeding_torrents: 
                torrents = seeding_torrents.split("\n")
                records = {}
                for torrent in torrents:
                    torrent_detail = filter(None, torrent.split('  '))
                    print (green('transmission status info - %s' % torrent_detail))
                    if torrent_detail[7].strip() != self.TORRENT_STATUS:
                        continue
                    records[torrent_detail[0].strip()] = torrent_detail[8]
                if len(records) > 0: 
                    print (green('Ready to stop seeding and synchronize to local.'))
                    self.retrieve_remote_video(records)

            sleep(self.DEFAULT_MONITOR_INTERVAL)


    def retrieve_remote_video(self, records):
        """
        Retrieve video from remote server.
        """
        for key, val in records.items():
            torrent_path = (self.DEFAULT_REMOTE_VIDEO_DIR+val).encode('utf-8')
            #existence = exists(torrent_path, use_sudo=False, verbose=True)
            #if not existence:
            #    print (red('Downloaded video not exists on path - %s' %torrent_path))
            #    continue
            retriever = Retriever(torrent_path)
            retriever.start()
            self.stop_seeding(key)


    def stop_seeding(self, torrent_id):
        """
        Stop seeding for specified torrent.
        """
        run('transmission-remote -t %s -S' % torrent_id)
        run('transmission-remote -t %s -r' % torrent_id)
        print (green('Stop seeding and delete tansmission task - [%s].' %  torrent_id))
