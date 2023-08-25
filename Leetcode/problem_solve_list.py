import os
import re
import sys

base_path = os.path.dirname(os.path.abspath(__file__))
#print(base_path)


dir_list = os.listdir(base_path)
dir_list.pop(dir_list.index('problem_solve_list.py'))
dir_list.sort(key=lambda x: int(re.search(r'(\d+)', x).group()))


# Open the file in write mode
with open("output.txt", "w") as file:
    # Redirect the standard output to the file
    original_stdout = sys.stdout
    sys.stdout = file
    
    for dir_name in dir_list:
        print(f"* [{dir_name}](https://github.com/PinkR1ver/JudeW-Problemset/tree/master/Leetcode/" + dir_name.replace(' ', '%20') + ")")
        
    # Restore the standard output
    sys.stdout = original_stdout
        