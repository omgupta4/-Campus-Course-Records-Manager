# edu/ccrm/domain/Person.py
from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, id, full_name, email):
        self._id = id
        self._full_name = full_name
        self._email = email

    # Getters & Setters
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def full_name(self):
        return self._full_name

    @full_name.setter
    def full_name(self, value):
        self._full_name = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value

    # Abstract method
    @abstractmethod
    def get_profile(self):
        pass

    def __str__(self):
        return f"ID: {self._id}, Name: {self._full_name}, Email: {self._email}"