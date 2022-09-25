from abc import ABC, abstractmethod, abstractproperty
from Objects.Base.Selected import Selected

class ActivatedObj(ABC):
    @abstractproperty
    def content():
        """Контент, отображающий объект"""
    @abstractproperty
    def selected():
        """Состояние объекта"""
    @abstractmethod
    def emit():
        """Выполнить что-то при активации объекта"""