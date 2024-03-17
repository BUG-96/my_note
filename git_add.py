import subprocess
import sys

commit_msg = "add"

try:
    subprocess.call(['git', 'add', '.'])
    subprocess.call(['git', 'commit', '-m', commit_msg])
    print("add success")
except Exception as e:
    print("\033[91m add faile ...\033[0m")


    
