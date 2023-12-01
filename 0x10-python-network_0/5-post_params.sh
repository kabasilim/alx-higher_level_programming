#!/bin/bash
# takes in a URL, sends a POST request to the passed URL
curl -sX POST "$1" -d "email=test@gmail.com&subject=I will always be here for PLD"here for PLD" "$1"
