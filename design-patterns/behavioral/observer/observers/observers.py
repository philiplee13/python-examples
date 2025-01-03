from abc import ABC, abstractmethod


class Observer(ABC):
    """
    Observer Interface - this will be the object that "subscribes" to a given subject
    Needs an "update" method -> gets the update from the subject
    """

    @abstractmethod
    def update(self, subject) -> None:
        pass


class ObserverOne(Observer):
    def update(self, subject) -> None:
        if subject._state > 10:
            print(f"State was more than 10 from {self.__class__.__name__}")


class ObserverTwo(Observer):
    def update(self, subject) -> None:
        if subject._state > 10:
            print(f"State was more than 10 from {self.__class__.__name__}")
