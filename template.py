import sys

name = "A-small"
path = ""

sys.stdin = open(path + name + ".in")

testCases = int(input())

def solve():
    line = input().split()
    cmd = line[0]
    n = int(line[1])
    a = [float(x) for x in line[2:]]

    if cmd == "median":
        a.sort()
        res = a[n // 2]
    elif cmd == "mean":
        res = sum(a) / float(len(a))

    return res


for testCase in range(1, testCases + 1):
    
    print("Case #" + str(testCase) + ": " + ("%.10f" % solve()))