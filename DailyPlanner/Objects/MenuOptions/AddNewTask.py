from Objects.Base.Selected import Selected
from Objects.MenuOptions.Base.MenuOption import MenuOption

class AddNewTask(MenuOption):
    def __init__(self):
        self.content = 'Добавить новую задачу'
        self.__selected = Selected.FALSE