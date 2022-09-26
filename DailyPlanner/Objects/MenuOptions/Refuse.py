from Objects.Base.Selected import Selected
from Objects.MenuOptions.Base.MenuOption import MenuOption

class Refuse(MenuOption):
    def __init__(self):
        self.content = 'Отказаться'
        self.__selected = Selected.FALSE