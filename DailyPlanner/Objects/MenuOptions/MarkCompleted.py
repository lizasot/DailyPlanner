from Objects.Base.Selected import Selected
from Objects.MenuOptions.Base.MenuOption import MenuOption

class MarkCompleted(MenuOption):
    def __init__(self):
        self._content = 'Отметить выполненным'
        self._selected = Selected.FALSE