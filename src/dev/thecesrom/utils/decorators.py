"""thecesrom.dev utils decorators."""


class classproperty(property):  # pylint: disable=invalid-name
    def __get__(self, cls, owner):
        return classmethod(self.fget).__get__(None, owner)()
