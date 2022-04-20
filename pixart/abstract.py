from abc import ABCMeta, abstractmethod


class Shape(metaclass=ABCMeta):
    def __eq__(self, other):
        if (
            self.edge == other.edge
            and self.eyes == other.eyes
            and self.mouth == other.mouth
        ):
            return True
        return False

    @property
    @abstractmethod
    def edge(self):
        pass

    @property
    @abstractmethod
    def eyes(self):
        pass

    @property
    @abstractmethod
    def mouth(self):
        pass

    @abstractmethod
    def make(self, **kwargs):
        pass


class Color(metaclass=ABCMeta):
    def __eq__(self, other):
        if (
            self.skin == other.skin,
            self.eyes == other.eyes
        ):
            return True
        return False

    @property
    @abstractmethod
    def skin(self):
        pass

    @property
    @abstractmethod
    def eyes(self):
        pass

    @abstractmethod
    def make(self, **kwargs):
        pass


class Character(metaclass=ABCMeta):
    def __eq__(self, other):
        if (
            self.shape == other.shape
            and self.color == other.color
            and self.attributes == other.attributes
        ):
            return True
        return False

    @classmethod
    def get_factory(cls, modname, classname):
        mod = __import__(modname)
        factory = getattr(mod, classname)
        return factory()

    @property
    @abstractmethod
    def shape(self):
        pass

    @property
    @abstractmethod
    def color(self):
        pass

    @property
    @abstractmethod
    def attributes(self):
        pass

    @abstractmethod
    def create(self, num, **kwargs):
        pass
