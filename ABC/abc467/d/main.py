def main():
    import sys

    input = sys.stdin.readline
    from itertools import combinations
    import numpy as np

    for _ in range(int(input())):
        px, py, qx, qy, rx, ry, sx, sy = map(int, input().split())

        pqx = qx - px
        pqy = qy - py

        rsx = sx - rx
        rsy = sy - ry

        if pqx * rsy != pqy * rsx:
            print("Yes")
        else:
            print(
                "Yes"
                if ((px + qx) - (rx + sx)) * pqx + ((py + qy) - (ry + sy)) * pqy == 0
                else "No"
            )


if __name__ == "__main__":
    main()
