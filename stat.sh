#!/bin/bash

if [ ! $(pgrep "spotifyd") ] 
then
    playerctl metadata --format "{{artist}} : {{title}}"
else
    python3 .config/polybar/sptstat.py
fi
