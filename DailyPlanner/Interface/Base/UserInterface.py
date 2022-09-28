from abc import ABC, abstractmethod, abstractproperty
class UserInterface(ABC):
    @abstractmethod
    def print(self, text : str):
        """Вывести текст (может содержать спец. символы переноса строки)"""
        
    @abstractmethod
    def read(self, promt):
        """Получить данные от пользователя"""
        
    @abstractmethod
    def getChoice(self):
        """Обработка клавиш во время выбора опций"""
        
    @abstractmethod
    def printList(self):
        """Вывод активируемых объектов"""
        
    @abstractmethod
    def clear(self):
        """Очищение экрана"""
        
    @abstractmethod
    def printDivider(self, ch : str = '='):
        """Отображение делителя между меню и задачами"""