from Objects.Base.Selected import Selected
from Objects.MenuOptions.Base.MenuOption import MenuOption

class ExportTask(MenuOption):
    def __init__(self):
        self.content = 'Экспортировать задачи'
        self.__selected = Selected.FALSE