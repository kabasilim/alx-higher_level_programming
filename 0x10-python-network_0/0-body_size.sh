#!/bin/bash
# Bash script that takes in a URL, sends a request to that URL
curl -I -s "$1" | grep "Content-Length:" | cut -d " " -f 2
