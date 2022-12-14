import datetime
import json
import os

from Interface.Base.UserInterface import UserInterface
from Interface.ConsoleInterface import ConsoleInterface
from Objects.MenuOptions.Base.MenuOption import MenuOption
from Objects.Base.Selected import Selected

from Objects.Task import Task

from Objects.MenuOptions.Agree import Agree
from Objects.MenuOptions.Refuse import Refuse

from Objects.MenuOptions.MarkCompleted import MarkCompleted
from Objects.MenuOptions.AddNewTask import AddNewTask
from Objects.MenuOptions.EditTask import EditTask
from Objects.MenuOptions.DeleteTask import DeleteTask
from Objects.MenuOptions.ImportTask import ImportTask
from Objects.MenuOptions.ExportTask import ExportTask

class Controller():
    def __init__(self, out : UserInterface = ConsoleInterface()):
        self.task_list = []
        self.menu_options = [MarkCompleted(), AddNewTask(), EditTask(), DeleteTask(), ImportTask(), ExportTask()]
        self.out = out

    @property
    def task_list(self):
        return self.__task_list

    @task_list.setter
    def task_list(self, task_list):
        if type(task_list) is list:
            self.__task_list = task_list
        else:
            self.__task_list = []

    @property
    def menu_options(self):
        return self.__menu_options

    @menu_options.setter
    def menu_options(self, menu_options):
        if type(menu_options) is list:
            self.__menu_options = menu_options
        else:
            self.__menu_options = []

    @property
    def out(self):
        return self.__out

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
    
    def choiceHandler(self, choice : int, choice_ind : int, l : list):
        if choice == -1 and choice_ind != 0:
            choice_ind -= 1
        elif choice == 1 and choice_ind != len(l) - 1:
            choice_ind += 1
        return choice_ind
    
    def importTasks(self, file_import = 'import.json'):
        if os.path.exists(file_import):
            with open(file_import, 'r') as f:
                json_object = json.load(f)
            self.task_list = [Task(x) for x in json_object]
    
    def exportTasks(self, file_export = 'export.json'):
        with open(file_export, 'w') as f:
            json.dump([x.content for x in self.task_list], f)

    def displayTaskList(self):
        if len(self.task_list) > 0:
            self.out.printList(self.task_list)
            self.out.printDivider()

    def getOption(self, options : list, repeat):
        choice = 1
        choice_ind = 0
        while choice != 0:
            self.out.clear()
            #self.out.print(f'?????????????????????????? ???????????? ???? ?????????? {file_import}?')
            repeat()
            options[choice_ind].selected = Selected.TRUE
            self.out.printList(options)
            choice = self.out.getChoice()
            if choice != 0:
                options[choice_ind].selected = Selected.FALSE
                choice_ind = self.choiceHandler(choice, choice_ind, options)
        return options[choice_ind]

    def deleteTask(self, task):
        self.task_list.remove(task)

    def completeTask(self, task, file_log):
        with open(file_log, 'a') as f:
            date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f'{date_time} {task.content}\n')
        self.deleteTask(task)

    def editTask(self, task):
        task.selected = Selected.CHOSEN
        self.out.print(str(task))
        self.out.print('?????????????? ?????????? ?????????? ?????????????????? ????????????: ')
        task.content = self.out.read()
        task.selected = Selected.FALSE

    def selectTask(self, option):
        if len(self.task_list) == 0:
            self.out.clear()
            self.out.print('???? ?????????????? ?????????? ?? ????????????.')
            self.out.print('?????????????? Enter, ?????????? ????????????????????...')
            self.out.getChoice()
            option = None
        else:
            text_for_repeat = lambda: self.out.print(str(option))
            option = self.getOption(self.task_list, text_for_repeat)
        return option

    def start(self, file_import = 'save.json'):
        file_export = 'save.json'
        file_log = 'log.txt'
        accord : list = [Agree(), Refuse()]
        # ???????? ???????????? ???????? ?????? ?????????????? - ???????????????????? ??????????????????????????
        if os.path.exists(file_import):
        #if False:
            text_for_repeat = lambda: self.out.print(f'?????????????????????????? ???????????? ???? ?????????? {file_import}?')
            if type(self.getOption(accord, text_for_repeat)) == Agree:
                self.importTasks(file_import)

        end = False
        while not end:
            text_for_repeat = lambda: self.displayTaskList()
            option = self.getOption(self.menu_options, text_for_repeat)
            if type(option) == MarkCompleted:
                option.selected = Selected.CHOSEN
                task = self.selectTask(option)
                option.selected = Selected.FALSE
                if task != None:
                    self.completeTask(task, file_log)
            elif type(option) == AddNewTask:
                self.out.clear()
                option.selected = Selected.CHOSEN
                self.out.print(str(option))
                self.out.print('?????????????? ????????????: ')
                new_task = self.out.read()
                self.task_list.append(Task(new_task))
                option.selected = Selected.FALSE
            elif type(option) == EditTask:
                option.selected = Selected.CHOSEN
                task = self.selectTask(option)
                option.selected = Selected.FALSE
                if task != None:
                    self.editTask(task)
            elif type(option) == DeleteTask:
                option.selected = Selected.CHOSEN
                task = self.selectTask(option)
                option.selected = Selected.FALSE
                if task != None:
                    self.deleteTask(task)
            elif type(option) == ImportTask:
                self.importTasks(file_import)
                option.selected = Selected.FALSE
            elif type(option) == ExportTask:
                self.exportTasks(file_export)
                option.selected = Selected.FALSE