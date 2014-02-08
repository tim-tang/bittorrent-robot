# Makefile for BitTorrent-robot
# Author tim.tang

.PHONY: help

help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo ""
	@echo "  watch         to sync remote video to local disk."
	@echo "  clean-pyc     to clean project *.pyc files."
	@echo ""

# start to watch transmission status
watch:
	-fab preparation monitor_torrent

# clean pyc files
clean-pyc:
	-find . -name '*.pyc' -exec rm -f {} + 
	-find . -name '*.pyo' -exec rm -f {} + 
	-find . -name '~' -exec rm -f {} + 
