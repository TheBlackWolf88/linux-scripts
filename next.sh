#!/bin/bash
if [[ ! $(playerctl --player=spotifyd status) = "Playing" ]]
then
    playerctl next
else
    playerctl --player=spotifyd next
fi