import random
import os
import tkinter
from pyopentdb import OpenTDBClient, Category, QuestionType, Difficulty
import json
import time
import signal

def handler(signum, frame):
    pass

def main():
    try:
        ans = input("Write the number: ")
        ans = int(ans)
        if ans == 0: return ans
        if ans > len(choices):
            print("u ok?")
            main()
        return ans
    except Exception:
        main()

signal.signal(signal.SIGINT, handler)
client = OpenTDBClient()
questions = client.get_questions(
    amount=1,
    difficulty=Difficulty.MEDIUM
)
questions = questions.to_serializable()
questions = questions[0]
print(questions["question"])
choices = questions["choices"]
i = 0
for c in choices:
    print(str(i)+" "+c)
    i += 1
# print(questions["answer_index"])
ans = main()
if(ans == questions["answer_index"]):
    print("Heh")
    os.system("exit")
else:
    print("Suckeeer!")
    time.sleep(1)
    os.system("reboot")
