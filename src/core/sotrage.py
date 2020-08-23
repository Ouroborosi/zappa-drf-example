import uuid

from abc import ABC, abstractmethod

class Storage(ABC):
    """
    The interface defines the CRUD functions for different storagy
    """

    @abstractmethod
    def get(self, id: uuid, condition: dict = None):
        pass

    @abstractmethod
    def save(self, data):
        pass

    @abstractmethod
    def delete(self, id: uuid):
        pass