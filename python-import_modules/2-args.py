#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    count = len(sys.argv)
    if count == 0:
        print("0 arguments.")
    else:
        print("{} argument{}:".format(count, "" if count == 1 else "s"))
        for i in range(1, count):
            print("{}: {}".format(i, sys.argv[i]))
