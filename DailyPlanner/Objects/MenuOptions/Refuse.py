from Objects.Base.Selected import Selected
from Objects.MenuOptions.Base.MenuOption import MenuOption

class Refuse(MenuOption):
    def __init__(self):
        self._content = 'Отказаться'
        self._selected = Selected.FALSE