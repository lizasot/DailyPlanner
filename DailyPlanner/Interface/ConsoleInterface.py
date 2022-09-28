from time import sleep
import keyboard
from Interface.Base.UserInterface import UserInterface

class ConsoleInterface(UserInterface):
    def print(self, text : str):
        text_lines = text.split('\n')
        for x in text_lines:
            print(x)

    def printList(self, items : list):
        for x in items:
            print(str(x))

    def getChoice(self):
        sleep(0.3)
        key = keyboard.read_key()
        while key != 'up' and key != 'down' and key != 'enter':
            key = keyboard.read_key()
        if key == 'up':
            return -1
        elif key == 'down':
            return 1
        elif key == 'enter':
            return 0

    def printDivider(self, ch : str = '='):
        print(ch*12)

    def read(self, promt : str = ''):
        print(promt,end = '')
        return input()

    def clear(self):
        print('\n'*100)