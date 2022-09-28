from Objects.Base.Selected import Selected
from Objects.MenuOptions.Base.MenuOption import MenuOption

class ImportTask(MenuOption):
    def __init__(self):
        self._content = 'Импортировать задачи'
        self._selected = Selected.FALSE