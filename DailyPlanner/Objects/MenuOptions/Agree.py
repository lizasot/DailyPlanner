from Objects.Base.Selected import Selected
from Objects.MenuOptions.Base.MenuOption import MenuOption

class Agree(MenuOption):
    def __init__(self):
        self.content = 'Согласиться'
        self.__selected = Selected.FALSE