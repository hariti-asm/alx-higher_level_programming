#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) - 1 == 0:
        print("0")
    else:
        sum_add = 0
        for i in range(len(sys.argv) - 1):
            add = int(sys.argv[i + 1])
            sum_add += add
        print("{}".format(sum_add))
