class Feeling:
    __VALUE_DEFAULT_MIN = 0
    __VALUE_DEFAULT_MAX = 100
    TYPE_HUNGER = 0
    TYPE_THIRST = 1
    TYPE_LONELINESS = 2

    def __init__(self, value = round((__VALUE_DEFAULT_MIN+__VALUE_DEFAULT_MAX)*.5), minValue = __VALUE_DEFAULT_MIN, maxValue = __VALUE_DEFAULT_MAX):
        self.minValue = minValue
        self.maxValue = maxValue
        self.value = value

    def add(self, value):
        self.value = min(self.maxValue, self.value+value)

    ##
    # overriding int() cast

    def __int__(self):
        return self.value

    def __radd__(self, other):
        self.value = min(self.maxValue, self.value + other)
        return self.value

    def __rsub__(self, other):
        self.value = max(self.minValue, self.value - other)
        return self.value

    def __sub__(self, other):
        return self.__rsub__(other)