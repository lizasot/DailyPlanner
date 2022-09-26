from time import sleep
import keyboard
from Interface.Base.UserInterface import UserInterface

class ConsoleInterface(UserInterface):
    def print(text : str):
        text_lines = text.split('\n')
        for x in text_lines:
            print(x)

    def printList(items : list):
        for x in items:
            print(str(x))

    def getChoice():
        sleep(0.8)
        key = keyboard.read_key()
        if key == 'up':
            return -1
        elif key == 'down':
            return 1
        elif key == 'enter':
            return 0

    def printDivider(ch : str = '='):
        print(ch*12)

    def read(promt : str = ''):
        print(promt,end = '')
        return input()