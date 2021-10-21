#!/bin/bash
if [[ $(playerctl --player=firefox status) = "Paused" && ! $(playerctl --player=spotifyd status) = "Playing" && ! $(playerctl --player=spotifyd status) = "Paused" || $(playerctl --player=firefox status) = "Playing" ]]
then
    playerctl play-pause
else
    playerctl -l | grep spotifyd &> 0 && (playerctl -p spotifyd status | grep Playing &> 0 && playerctl -p spotifyd pause) || (playerctl -p spotifyd status | grep Paused &> 0 && playerctl -p spotifyd play)
fi