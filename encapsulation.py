
# creating a protected class
class Protected:
    def __init__(self):
        self._protectedVar = 1

# creating an object to make use of the protected class
obj = Protected()
obj._protectedVar = 20
print(obj._protectedVar)


# creating a private class
class Private:
    def __init__(self):
        self.__privateVar = 10

# creating an object to use the private class
obj = Private()
obj.__privateVar = 15
print(obj.__privateVar)
