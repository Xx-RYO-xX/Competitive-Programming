# https://hyperion64.hatenadiary.org/entry/20131215/p1

from math import sqrt

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

bunnshi = sqrt(
    (x1 - x2) ** 2
    + (x1 - x3) ** 2
    + 2 * sqrt(3) * (x1 - x3) * (y2 - y3)
    + 3 * (y2 - y3) ** 2
    + 2 * (-x1 + x2) * (-x1 + x3 + sqrt(3) * (-y2 + y3))
) * (
    sqrt(3) * (x1 - x2) ** 2
    + sqrt(3) * (x1 - x3) ** 2
    - 3 * (x1 - x3) * (y1 - y2)
    + (-x1 + x2) * (sqrt(3) * (x1 - x3) + 3 * (-y1 + y3))
    + sqrt(3) * (y1**2 + y2**2 - y2 * y3 + y3**3 - y1 * (y2 + y3))
)

bunnbo = (-2 * sqrt(3) * x1 + sqrt(3) * x2 + sqrt(3) * x3 - 2 * y2 + 3 * y3) * sqrt(
    x1**2
    + x2**2
    + x3**2
    + sqrt(2) * x3 * y1
    + y1**2
    - sqrt(3) * x3 * y2
    - y1 * y2
    + y2**2
    - x2 * (x3 - sqrt(3) * (y1 - y2))
    - y1 * y3
    - y2 * y3
    + y1**2
    - x1 * (x2 + x3 + sqrt(3) * (-y2 + y3))
)

print(bunnshi / bunnbo)
