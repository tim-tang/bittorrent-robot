# Makefile for BitTorrent-robot
# Author tim.tang

.PHONY: help

help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo ""
	@echo "  watch         to sync remote video to local disk."
	@echo "  torrent       to upload and append torrent task into remote transmission."
	@echo "  clean-pyc     to clean project *.pyc files."
	@echo ""

# start to watch transmission status
watch:
	-fab preparation monitor_torrent

# add torrent files to remote transmission
torrent:
	-fab preparation append_torrent

# clean pyc files
clean-pyc:
	-find . -name '*.pyc' -exec rm -f {} + 
	-find . -name '*.pyo' -exec rm -f {} + 
	-find . -name '~' -exec rm -f {} + 
