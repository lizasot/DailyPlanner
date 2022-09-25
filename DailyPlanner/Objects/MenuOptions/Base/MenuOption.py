from Objects.Base.ActivatedObj import ActivatedObj
from Objects.Base.Selected import Selected

class MenuOption(ActivatedObj):
    def __init__(self):
        self.content = 'Пункт меню'
        self.__selected = Selected.FALSE

    @property
    def content(self):
        return self.__content

    @property
    def selected(self):
        return self.__selected

    @selected.setter
    def selected(self, selected):
        if selected == Selected.CHOSEN or selected == 2:
            self.__selected = Selected.FALSE
        elif selected == True or selected == Selected.TRUE or selected == 1:
            self.__selected = Selected.TRUE
        else:
            self.__selected = Selected.FALSE

    def getContent(self):
        return self.content

    def getSelected(self):
        return self.selected

    def emit(self):
        return self

    def __str__(self):
        if self.selected == Selected.TRUE:
            ch = '*'
        elif self.selected == Selected.CHOSEN:
            ch = '>'
        else:
            ch = ' '
        return f'[{ch}] {self.content}'