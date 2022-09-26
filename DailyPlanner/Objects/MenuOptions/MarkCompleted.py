from Objects.Base.Selected import Selected
from Objects.MenuOptions.Base.MenuOption import MenuOption

class MarkCompleted(MenuOption):
    def __init__(self):
        self.content = 'Отметить выполненным'
        self.__selected = Selected.FALSE