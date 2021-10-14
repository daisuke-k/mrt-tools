import sys
import PrefixASPath

USAGE="""
Usage: {} [mrt filename]
"""

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(USAGE.format(sys.argv[0]), file=sys.stderr)

    filename = sys.argv[1]

    d = PrefixASPath.PrefixASPath(filename)
    for prefix, prefixlen, aspaths in d:
        print("{}/{},{}".format(prefix, prefixlen, "-".join(aspaths)))
