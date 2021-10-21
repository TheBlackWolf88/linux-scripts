import random
import os
import tkinter
from pyopentdb import OpenTDBClient, Category, QuestionType, Difficulty
import json
import time
import signal


x = random.randrange(0, 100)
print(x)
if(x == 0 or x == 1):
    os.system("killall firefox")
    os.system("alacritty -e python3 /home/dan/.config/polybar/app.py")
    
