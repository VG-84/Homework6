#dz6-2

class Road:
    __asp_mass = 25

    def __init__(self, length, width):
        self._length = float(length)
        self._width = float(width)

    def asp_sum(self, data = 1):
        return self._length * self._width * self.__asp_mass * data