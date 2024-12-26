"""
Factory Pattern
https://refactoring.guru/design-patterns/factory-method
"""

from abc import ABC, abstractmethod


class Account(ABC):
    @abstractmethod
    def get_balance(self) -> float:
        pass

    @abstractmethod
    def get_owner(self) -> str:
        pass

    @abstractmethod
    def get_type(self) -> str:
        pass
