import sys
sys.path.append("..")

import os
from random import choice
from Interface.Base.UserInterface import UserInterface
from Interface.ConsoleInterface import ConsoleInterface
from Objects.MenuOptions.Base.MenuOption import MenuOption
from Objects.Base.Selected import Selected
from Objects.MenuOptions.Agree import Agree
from Objects.MenuOptions.Refuse import Refuse

class Controller():
    def __init__(self):
        self.task_list = []
        self.menu_options = []
        self.out = ConsoleInterface()

    def __init__(self, out : UserInterface):
        self.task_list = []
        self.menu_options = []
        self.out = out

    @property
    def task_list(self):
        return self.__task_list

    @property
    def menu_options(self):
        return self.__menu_options

    @property
    def out(self):
        return self.__out

    @task_list.setter
    def task_list(self, task_list):
        if type(task_list) is list:
            self.__task_list = task_list
        else:
            self.__task_list = []

    @menu_options.setter
    def menu_options(self, menu_options):
        if type(menu_options) is list:
            self.__menu_options = menu_options
        else:
            self.__menu_options = []

    @out.setter
    def out(self, out):
        if type(out) is UserInterface:
            self.__out = out
        else:
            self.__out = ConsoleInterface()

    def getTasks(self):
        return self.task_list

    def getOptions(self):
        return self.menu_options
    
    def setSelected(l : list, ind : int, select : Selected):
        l[ind].selected = select
    
    def choiceHandler(choice : int, choice_ind : int, l : list):
        if choice == -1 and choice_ind != 0:
            choice_ind -= 1
        elif choice == 1 and choice_ind != len(l) - 1:
            choice_ind += 1
        return choice_ind
    
    def importTasks(self, file_import = 'import.txt'):
        self.out.print('Импортируются задачи...')

    def start(self, file_import = 'import.txt'):
        accord : list = [Agree(), Refuse()]
        if os.path.exists(file_import):
            choice = 1
            choice_ind = 0
            while choice != 0:
                self.setSelected(accord, choice_ind, Selected.TRUE)
                self.out.print(f'Импортировать задачи из файла {file_import}?')
                choice = self.out.getChoice()
                if choice != 0:
                    choice_ind = self.choiceHandler(choice, choice_ind, accord)
            if choice_ind == 0:
                self.importTasks(self)