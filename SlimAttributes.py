from pympler import asizeof


class RangeNumber:
    def __init__(self, min, max):
        self._min_value = min
        self._max_value = max

    def __set_name__(self, owner, name):
        self._attribute_name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self._attribute_name]

    def __set__(self, instance, value):
        if not isinstance(value, int) or value < self._min_value or value > self._max_value:
            raise ValueError(f"Invalid Value(out of range[{self._min_value}, {self._max_value}])")

        instance.__dict__[self._attribute_name] = value


class RangeWord:
    def __init__(self, min_word, max_word):
        self._min_word = min_word
        self._max_word = max_word

    def __set_name__(self, owner, name):
        self._attribute_name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self._attribute_name]

    def __set__(self, instance, value):
        if not isinstance(value, str) or len(value) < self._min_word or len(value) > self._max_word:
            raise ValueError(f"Invalid value(out of range[{self._min_word}, {self._max_word}])")

        instance.__dict__[self._attribute_name] = value


class AgeClass:
    __slots__ = ("age")


    def __init__(self, age):
        self.age = age


class Product:
    __slots__ = ("title", "price")

    def __init__(self, title, price):
        self.title = title
        self.price = price


class Person:
    __slots__ = ("firstname", "lastname", "__dict__")

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname


# product1 = Product("Iphone 13 ", 1000)

person1 = Person("ar", "shabdin")
print(person1.firstname, person1.lastname)
