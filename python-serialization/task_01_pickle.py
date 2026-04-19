#!/usr/bin/python3
"""dfghjkl"""
import pickle


class CustomObject:
    """fghjkl"""
    dicti = {}
    def __init__(self, name, age, is_student):
        """ghjk"""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """ghj"""
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """fghjk"""
        with open(filename, "wb") as f:
            pickle.dump(self, f)

    @classmethod
    def deserialize(cls, filename):
        try:
            with open(filename, "rb") as f:
                data = pickle.load(f)
                return data
        except Exception:
            return None
