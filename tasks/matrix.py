from typing import List


class Matrix:
    def __init__(self, _array: List[List[int]]):
        """
        This class takes only List of Lists. Example: [[], [], []]
        :param _array: List[List[int]]
        """
        self._array = _array

    def rotate(self) -> List:
        """
        Function to rotate the matrix 90 degrees clockwise
        :return: List[List]
        """
        __temp_array = list(reversed(self._array))
        return [
                    [
                        __temp_array[__external][__internal] for __external in range(len(__temp_array))
                    ] for __internal in range(len(__temp_array[0]))
                ]

    def make_spiral(self) -> List:
        """
        Function to make spiral from numbers in matrix
        :return: List
        """
        __temp_array = [__i for __i in self._array]
        __result = []
        while len(__temp_array) > 0:
            __result += __temp_array.pop(0)
            __temp_array = \
                [
                    __item3 for __item3 in [
                        __item2 for __item2 in reversed([list(_item1) for _item1 in list(zip(*__temp_array))])
                    ]
                ]
        return __result


if __name__ == '__main__':
    raise RuntimeError('Only as module')
