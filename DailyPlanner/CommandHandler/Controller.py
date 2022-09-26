class Controller():
    def __init__(self):
        self.task_list = []
        self.menu_options = []

    def __init__(self, menu_options : list):
        self.task_list = []
        self.menu_options = menu_options

    @property
    def task_list(self):
        return self.__task_list

    @property
    def menu_options(self):
        return self.__menu_options

    @task_list.setter
    def content(self, task_list):
        if type(task_list) is list:
            self.__task_list = task_list
        else:
            self.__task_list = task_list

    @menu_options.setter
    def content(self, menu_options):
        if type(menu_options) is list:
            self.__menu_options = menu_options
        else:
            self.__menu_options = menu_options

    def getTasks(self):
        return self.task_list

    def getOptions(self):
        return self.menu_options

    def start(self):
        return self.menu_options