# coding: utf-8
# Author tim.tang

import threading
from fabric.api import *
from fabric.operations import put, get
from fabric.colors import green, red

DEFAULT_LOCAL_MOVIE_DIR = './'

class Retriever(threading.Thread):

    """ 
    Threaded  remote video retriever 
    """

    def __init__(self, record):
        self.record = record
        threading.Thread.__init__(self)

    def run(self):
        """ 
        Retrieve remote video to local dir 
        """
        get(self.record, DEFAULT_LOCAL_MOVIE_DIR)
        print (green('Synchronize video - [%s] complete!' % self.record))
        destroy_remote_video(self.record)


    def destory_remote_video(self, record):
        """ 
        Destroy remote video after retrieve complete 
        """
        run('rm -rf %s' % record)
        print (green('Destroy remote video - [%s] finished!' % record))
