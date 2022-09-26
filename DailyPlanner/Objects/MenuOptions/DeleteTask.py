from Objects.Base.Selected import Selected
from Objects.MenuOptions.Base.MenuOption import MenuOption

class DeleteTask(MenuOption):
    def __init__(self):
        self.content = 'Удалить задачу'
        self.__selected = Selected.FALSE