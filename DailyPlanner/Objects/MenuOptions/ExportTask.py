from Objects.Base.Selected import Selected
from Objects.MenuOptions.Base.MenuOption import MenuOption

class ExportTask(MenuOption):
    def __init__(self):
        self._content = 'Экспортировать задачи'
        self._selected = Selected.FALSE