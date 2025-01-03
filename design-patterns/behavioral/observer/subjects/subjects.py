from typing import List
from random import randrange

from abc import ABC, abstractmethod


class Subject(ABC):
    """
    Subject Interface - This will be the object that the observers are "subscribing" to
    Needs an "notify" method
    Needs a method to "add" and "remove" observers
    """

    @abstractmethod
    def notify(self) -> None:
        """
        Notifies all subscribed observers
        """
        pass

    @abstractmethod
    def add(self, observer) -> None:
        pass

    @abstractmethod
    def remove(self, observer) -> None:
        pass


class ConcreteSubject(Subject):
    _state: int = 0

    _observers = []

    def notify(self):
        for observer in self._observers:
            observer.update(self)

    def add(self, observer):
        self._observers.append(observer)

    def remove(self, observer):
        self._observers.remove(observer)

    def random_number(self) -> None:
        print(f"{self.__class__.__name__}: I'm doing something important.")
        self._state = randrange(10, 20)

        print(f"{self.__class__.__name__}: My state has just changed to: {self._state}")
        self.notify()
