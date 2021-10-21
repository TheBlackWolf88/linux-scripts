#!/bin/bash
if [ $(pgrep "spotifyd") ]
then
	spt
else
	spotifyd
	spt
fi
