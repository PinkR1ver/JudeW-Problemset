from email.mime import base
import os

basePath = r'/home/pinkr1ver/Documents/Github Projects/PinkR1ver-leetcode'

def has_number(input_string:str):
    return any(i.isdigit() for i in input_string)

for i in os.listdir(basePath):
    if has_number(i) and os.path.isdir(i):
        for j in os.listdir(i):
            if ".cpp" not in j:
                print(j)
                os.remove(os.path.join(basePath, i, j))
