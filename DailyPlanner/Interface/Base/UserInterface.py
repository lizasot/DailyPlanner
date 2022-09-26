from abc import ABC, abstractmethod, abstractproperty
class UserInterface(ABC):
    @abstractmethod
    def print(text : str):
        """Вывести текст (может содержать спец. символы переноса строки)"""
        
    @abstractmethod
    def read(promt):
        """Получить данные от пользователя"""
        
    @abstractmethod
    def getChoice():
        """Обработка клавиш во время выбора опций"""