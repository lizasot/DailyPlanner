from Objects.Base.Selected import Selected
from Objects.MenuOptions.Base.MenuOption import MenuOption

class AddNewTask(MenuOption):
    def __init__(self):
        self._content = 'Добавить новую задачу'
        self._selected = Selected.FALSE