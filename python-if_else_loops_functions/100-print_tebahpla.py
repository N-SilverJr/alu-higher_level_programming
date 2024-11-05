#!/usr/bin/python3
# This program prints the ASCII alphabet in reverse order, alternating lowercase and uppercase

print("".join(
        "{}".format(chr(c) if c % 2 == 0 else chr(c).upper())
            for c in range(122, 96, -1)
            ), end="")

