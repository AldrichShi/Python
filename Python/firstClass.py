# -*- coding: utf-8 -*-
# firstClass.py
# @author King
# @description
# @created 2019-06-21T14:38:04.507Z+08:00
# @last-modified 2019-06-21T14:59:00.791Z+08:00
#


class Person(object):
    def __init__(self, name, age):
        self._name = name
        self._age = age
    # ???---getter ??
    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    # ??? setter
    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 18:
            print('%s??????,', self._name)
        else:
            print("%s?????", self._name)


def main():
    person = Person('??', 20)
    person.play()
    person.age = 40
    person.play()


if __name__ == "__main__":
    main()
