# -*- coding: utf-8 -*-
"""
Drop in replacement to simulate some java classes for api compatability.

Created on Mon Dec 16 23:04:32 2019

@author: wolf
"""
import enum



class Enum(enum.Enum):

    @classmethod
    def valueOf(cls, key):
        for attrib in dir(cls):
            if attrib.lower() == key.lower():
                return cls[attrib]

        raise KeyError("invalid enum key")



class ArrayList:
    
    def __init__(self, *data):
        if data is None:
            data = []

        self._list = list(data)

    def as_list(self):
        return self._list

    def add(self, *args):
        if len(args) == 1:
            self._list.append(args[0])

        elif len(args) == 2:
            self.insert(*args)

    def remove(self, value):
        self._list.remove(value)

    def get(self, index):
        return self._list[index]

    def size(self):
        return len(self._list)

    def contains(self, value):
        return (value in self._list)

    def isEmpty(self):
        return len(self._list) > 0

    def clear(self):
        self._list = []

    def addAll(self, other):
        self[len(self):] = other

    def __add__(self, other):
        if isinstance(other, ArrayList):
            other = other._list
        joined = ArrayList()
        joined._list = self._list + other
        return joined
    
    def __len__(self):
        return self.size()

    def __getitem__(self, index):
        return self._list[index]

    def __setitem__(self, index, value):
        self._list[index] = value

    def __contains__(self, value):
        return value in self._list

    def __iter__(self):
        return iter(self._list)


class HashMap:
    def __init__(self, data=None):
        if data is None:
            data = {}

        self.data = data

    def remove(self, key):
        if key in self.data:
            del self.data[key]

    def __delitem__(self, key):
        del self.data[key]

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        self.data[key] = value

    def __contains__(self, value):
        return value in self.data

    def __iter__(self):
        return iter(self.data)


class LinkedList:
    pass


class BufferedReader:
    def __init__(self, path):
        self.io = open(path)

    def readLine(self):
        self.io.readline()

    def close(self):
        self.io.close()
