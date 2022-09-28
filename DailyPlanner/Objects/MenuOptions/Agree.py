from Objects.Base.Selected import Selected
from Objects.MenuOptions.Base.MenuOption import MenuOption

class Agree(MenuOption):
    def __init__(self):
        self._content = 'Согласиться'
        self._selected = Selected.FALSE