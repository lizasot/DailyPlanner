from Objects.Base.Selected import Selected
from Objects.MenuOptions.Base.MenuOption import MenuOption

class EditTask(MenuOption):
    def __init__(self):
        self.content = 'Отредактировать задачу'
        self.__selected = Selected.FALSE