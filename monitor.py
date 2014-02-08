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

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        """ 
        Monitor remote transmission status 
        """
        try:
            while True:
                status = run("transmission-remote -l")
                #print (green(status))
                seeding_torrents = run("transmission-remote -l|awk 'NR>1 {print $1 \"|\" $8 \"|\"$9}'")
                #print (green(seeding_torrents))
                if seeding_torrents: 
                    torrents = seeding_torrents.split("\n")
                    records = {}
                    for torrent in torrents:
                        torrent_detail = torrent.split('|')
                        if torrent_detail[1] != 'seeding':
                            continue
                        records[torrent_detail[0]] = torrent_detail[2]

                    if len(records) > 0: 
                        print (green('Ready to stop seeding and synchronize with local.'))
                        retrieve_remote_video(records)

                sleep(self.DEFAULT_MONITOR_INTERVAL)
        except KeyboardInterrupt:
            sys.exit(0)


        def retrieve_remote_video(self, records):
            for key, val in records.items():
                torrent_path = self.DEFAULT_REMOTE_VIDEO_DIR+value
                if not exists(torrent_path): 
                    print (red('Downloaded video not exists on path - [%s]' % torrent_path))
                    continue
                stop_seeding(key)
                retriever = Retriever(torrent_path)
                retriever.start()

        def stop_seeding(self, torrent_id):
            """
            Stop seeding for specified torrent.
            """
            run('transmission-remote -t %s -S' % torrend_id)
            run('transmission-remote -t %s -r' % torrend_id)
            print (green('Stop seeding and delete tansmission task - [%s].' %  torrend_id))
