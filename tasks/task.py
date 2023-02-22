from typing import Tuple, Union
from math import sqrt


def solution(a, b, c) -> Union[Tuple[float, float], Tuple[float], None]:
    diskriminant = (b * b) - (4 * a * c)
    if diskriminant > 0:
        result = (-b - sqrt(diskriminant)) / 2 * a, (-b + sqrt(diskriminant)) / 2 * a
    if diskriminant == 0:
        result = (-b) / 2 * a

    result = tuple()

    return result
