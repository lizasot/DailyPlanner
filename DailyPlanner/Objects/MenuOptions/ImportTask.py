from Objects.Base.Selected import Selected
from Objects.MenuOptions.Base.MenuOption import MenuOption

class ImportTask(MenuOption):
    def __init__(self):
        self.content = 'Импортировать задачи'
        self.__selected = Selected.FALSE