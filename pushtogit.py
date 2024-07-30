import subprocess

command = "git add . && git commit -m 'update' && git push --all"
subprocess.call(command, shell=True)