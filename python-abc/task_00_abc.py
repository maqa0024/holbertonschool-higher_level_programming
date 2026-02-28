#!/usr/bin/python3
"""Module that defines Animal abstract class, Dog and Cat subclasses."""
from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class for animals."""

    @abstractmethod
    def sound(self):
        """Return the sound the animal makes."""
        pass


class Dog(Animal):
    """A Dog class that inherits from Animal."""

    def sound(self):
        """Return the sound a dog makes."""
        return "Bark"


class Cat(Animal):
    """A Cat class that inherits from Animal."""

    def sound(self):
        """Return the sound a cat makes."""
        return "Meow"
