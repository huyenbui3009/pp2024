import os
import subprocess as sp
import signal

def os_module():
    while True:
        cmd = input("$ ")
        pid = os.getpid()
        if cmd == "exit":
            os.kill(pid, signal.SIGTERM)
            break
        if cmd.startswith("cd"): 
            relative_path = cmd[3:]
            absolute_path = os.path.abspath(relative_path)
            os.chdir(absolute_path) 
        else:
            os.system(cmd)
          
def subprocess_module():
    while True:
        cmd = input("$ ")
        if cmd == "exit":
            sp.anotherProcess.terminate()
        if cmd.startswith("cd"):
            relative_path = cmd[3:]
            absolute_path = os.path.abspath(relative_path)
            os.chdir(absolute_path)
        else:
            sp.Popen(cmd.split(), stdin=sp.PIPE, stdout=sp.PIPE, text=True).communicate()
            # split: turn into list of string command/arguments

def main():
    while True:
        choice = input("os or subprocess? ")
        if choice =="os":
            os_module()
        if choice=="subprocess":
            subprocess_module()
        else:
            print("invalid choice")
            continue

if __name__ == "__main__":
    main()
