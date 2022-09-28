from Objects.Base.ActivatedObj import ActivatedObj
from Objects.Base.Selected import Selected

class Task(ActivatedObj):
    def __init__(self):
        self._content = ''
        self._selected = Selected.FALSE

    def __init__(self, content : str):
        self._content = content
        self._selected = Selected.FALSE

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, content):
        if type(content) is str:
            self._content = content
        else:
            self._content = ''

    @property
    def selected(self):
        return self._selected

    @selected.setter
    def selected(self, selected):
        if selected == Selected.CHOSEN or selected == 2:
            self._selected = Selected.CHOSEN
        elif selected == True or selected == Selected.TRUE or selected == 1:
            self._selected = Selected.TRUE
        else:
            self._selected = Selected.FALSE

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