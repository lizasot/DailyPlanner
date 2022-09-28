from Objects.Base.Selected import Selected
from Objects.MenuOptions.Base.MenuOption import MenuOption

class DeleteTask(MenuOption):
    def __init__(self):
        self._content = 'Удалить задачу'
        self._selected = Selected.FALSE