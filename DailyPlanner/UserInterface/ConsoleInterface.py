class ConsoleInterface():
    def print(text : str):
        text_lines = text.split('\n')
        for x in text_lines:
            print(x)

    def printList(items : list):
        for x in items:
            print(str(x))

    def printDivider(ch : str = '='):
        print(ch*12)

    def read(promt : str = ''):
        print(promt,end = '')
        return input()