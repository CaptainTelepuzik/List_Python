import random
from typing import Optional, List


class learning:

    _inner_list: Optional[List[int]] = []
    LEFT_LIST: Optional[List[int]] = []
    RIGHT_LIST: Optional[List[int]] = []
    SUM_LEFT_LIST: Optional[List[int]] = None
    SUM_RIGHT_LIST: Optional[List[int]] = None

    def __init__(self, *, start: Optional[int] = 0,
                 stop: Optional[int] = 10, count: Optional[int] = 10) -> None:
        self._inner_list.clear()
        for i in range(count):
            self._inner_list.append(random.randint(start, stop))

    @property
    def all_digit_is_odd(self) -> bool:
        bool_list = True
        for i in self._inner_list:
            if not i % 2 == 0:
                bool_list = False
            if not bool_list:
                break

        print(bool_list)

        return bool_list

    def digit_more(self, digit: int) -> List[int]:
        num = []
        for i in self._inner_list:
            if digit < i:
                num.append(i)

        print(num)

    def print_list(self):
        print(self._inner_list)

    def max(self):
        return max(self._inner_list)

    def min(self):
        return min(self._inner_list)

    def avg(self):
        return sum(self._inner_list)/len(self._inner_list)

    def half_list(self):
        if len(self._inner_list) % 2 == 0:
            for i in range(len(self._inner_list)):
                if i < len(self._inner_list)/2:
                    self.LEFT_LIST.append(self._inner_list[i])
                else:
                    self.RIGHT_LIST.append(self._inner_list[i])
        else:
            for i in range(len(self._inner_list)):
                if i < len(self._inner_list)/2 - 1:
                    self.LEFT_LIST.append(self._inner_list[i])
                elif i > len(self._inner_list)/2:
                    self.RIGHT_LIST.append(self._inner_list[i])

        self.SUM_LEFT_LIST = sum(self.LEFT_LIST)
        self.SUM_RIGHT_LIST = sum(self.RIGHT_LIST)

        half_list: str = (f'Левая сторона списка {self.LEFT_LIST}, Правая сторона списка {self.RIGHT_LIST}')

        return half_list

    def comparison_list(self):
        if self.SUM_RIGHT_LIST > self.SUM_LEFT_LIST:
            difference = self.SUM_RIGHT_LIST - self.SUM_LEFT_LIST
            print(f'Сумма правой стороны {self.SUM_RIGHT_LIST} больше суммы левой стороны'
                  f' {self.SUM_LEFT_LIST} на {difference}')
        elif self.SUM_RIGHT_LIST < self.SUM_LEFT_LIST:
            difference = self.SUM_LEFT_LIST - self.SUM_RIGHT_LIST
            print(f'Сумма левой стороны {self.SUM_LEFT_LIST} больше суммы правой стороны'
                  f' {self.SUM_RIGHT_LIST} на {difference}')
        else:
            print('Стороны равны')


