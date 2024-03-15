import threading 
import time

class NumberPrintingThread(threading.Thread):
    def __init__(self, n ,sleeptime):
        threading.Thread.__init__(self)
        self.__n= n
        self.__sleeptime= sleeptime
    
    def run(self):
        for i in range(1, self.__n):
            print(f"Number: " + str(i))
            time.sleep(self.__sleeptime)

class CharacterPrintingThread(threading.Thread):
    def __init__(self, n ,sleeptime):
        threading.Thread.__init__(self)
        self.__n= n
        self.__sleeptime= sleeptime
    
    def run(self):
        start_char= "A"
        for i in range(1, self.__n):
            print(f"Letter: " + chr(ord(start_char)+i))
            time.sleep(self.__sleeptime)


if __name__ == "__main__":
    #create instances
    thread_numbers= NumberPrintingThread(n=10, sleeptime=1)
    thread_chars=  CharacterPrintingThread(n=13, sleeptime=1)
    
    thread_numbers.start()
    thread_chars.start()
    thread_numbers.join() #terminate 
    thread_chars.join() 


#2 printing tasks with delay between each print
import threading
import time
def printnumbers(n):
    for i in range(1,n):
        print(str(i))
        time.sleep(1)

def printchar(n):
    startchar="A"
    for i in range(1,n):
        print(chr(ord(startchar)+i))
        time.sleep(1)

if __name__ == "__main__":
    threadnum= threading.Thread(target=printnumbers, args=(10,))
    threadchar=threading.Thread(target=printchar, args=(13,))
    threadnum.start()
    threadchar.start()
    threadnum.join()
    threadchar.join()



