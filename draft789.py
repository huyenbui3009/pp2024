import subprocess
import os 

os.chdir(r"C:\Users\buing\Downloads\PYTHON")
try:
    # Execute the Python script "file_donot_exist.py"
    result = subprocess.run(["python", "tinker.py"], capture_output=True, text=True, check=True)
    print(result.stdout)
except subprocess.CalledProcessError as e:
    print(f"Error: {e}")
    print(f"Standard Error: {e.stderr}")

import subprocess

p = subprocess.Popen(["python", "--help"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

output, errors = p.communicate()
print(output)
"""" """

import threading
import time
class BackgroundThread(threading.Thread):
    def __init__(self, sleepTime):
        threading.Thread.__init__(self)
        self.__sleepTime = sleepTime

    def run(self):
        time.sleep(self.__sleepTime)
        print(f"Finished sleeping {self.__sleepTime}s")

# Creating an instance of BackgroundThread with sleep time of 10 seconds
backgroundThread = BackgroundThread(10)

# Starting the background thread
backgroundThread.start()  # note no args here

# Waiting for the background thread to finish
backgroundThread.join()

# This will be printed by the main thread after the background thread finishes sleeping
print("Finished main thread")

import threading
import time

def background_task():
    print("Background thread is running.")
    time.sleep(15)
    print("Background thread finished.")

# Create a background thread
background_thread = threading.Thread(target=background_task)

# Start the background thread
background_thread.start()

# Continue with the main thread
print("Main thread continues.")

# Wait for the background thread to finish (optional)
background_thread.join()

# Continue with the main thread
print("Main thread finished.")

import threading, pickle
def save(data, files):
    for i, file in enumerate(files):
        with open(file, 'wb') as f:
            pickle.dump(data[i], f)
    
def load(files):
    for file in files:
        with open(file, 'rb') as f:
            loaded_data= pickle.load(f)
            print(loaded_data)
# Data to be saved
data1 = {'name': 'John', 'age': 30, 'city': 'New York'}
data2= {'name': 'John', 'age': 30, 'city': 'New York'}
datalist=[data1, data2]
# File to save data
file_to_save = ['data1.pickle','data2.pickle']

# Create thread to save data
save_thread = threading.Thread(target=save, args=(datalist, file_to_save,))

# Create thread to load data
load_thread = threading.Thread(target=load, args=(file_to_save,))

# Start saving thread
save_thread.start()

# Wait for saving thread to finish
save_thread.join()

# Start loading thread
load_thread.start()

# Wait for loading thread to finish
load_thread.join()

# class BackgroundThread(threading.Thread):
#     def __init__(self, target, args=()):
#         threading.Thread.__init__(self, target=target, args=args)

# def save_background(datas, files):
#     save_thread = BackgroundThread(target=save, args=(datas, files))
#     save_thread.start()
#     return save_thread

# def load_background(file_path):
#     load_thread = BackgroundThread(target=load, args=(file_path,))
#     load_thread.start()
#     return load_thread
