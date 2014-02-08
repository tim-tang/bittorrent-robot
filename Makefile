# Makefile for BitTorrent-robot
# Author tim.tang

.PHONY: help

help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo ""
	@echo "  watch     to sync remote video to local disk."
	@echo ""

watch:
	-fab preparation monitor_torrent
