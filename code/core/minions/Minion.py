class Minion:
    __GENERATOR_PREFIX = 'm'
    __GENERATOR_COUNTER = 0
    @staticmethod
    def __generateInternalName():
        output = Minion.__GENERATOR_PREFIX+str(Minion.__GENERATOR_COUNTER)
        Minion.__GENERATOR_COUNTER += 1
        return output

    def __init__(self, name):
        self.__internalName = Minion.__generateInternalName()
        self.name = name
        self.feelings = {}