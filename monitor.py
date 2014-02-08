# coding: utf-8
# Author tim.tang

import threading
from fabric.api import *
from retriever import Retriever
from fabric.colors import green, red
from time import sleep

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
        while True:
            status = run("transmission-remote -l")
            print (green(status))
            seeding_torrent = run("transmission-remote -l |awk 'NR>1 {printf('%s|%s\n', $1, $9)} | grep 'seeding' ")
            if seeding_torrent: 
                torrents = seeding_torrent.split("\n")
                records = {}
                for torrent in torrents:
                    torrent_detail = torrent.split('|')
                    records[torrent_detail[0]] = torrent_detail[1] 

                print (green('Ready to stop seeding and synchronize with local.'))
                retrieve_remote_video(records)

            sleep(DEFAULT_MONITOR_INTERVAL)


        def retrieve_remote_video(self, records):
            for key, val in records.items():
                torrent_path = DEFAULT_REMOTE_VIDEO_DIR+value
                exists = run('[ -d %s -o -f %s ] % torrent_path')
                if not exists: 
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
