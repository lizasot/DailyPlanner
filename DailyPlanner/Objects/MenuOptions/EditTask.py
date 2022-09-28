from Objects.Base.Selected import Selected
from Objects.MenuOptions.Base.MenuOption import MenuOption

class EditTask(MenuOption):
    def __init__(self):
        self._content = 'Отредактировать задачу'
        self._selected = Selected.FALSE