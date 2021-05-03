import sys

name = "A-small"
path = "2021/round1/"

sys.stdin = open(path + name + ".in")

testCases = int(input())

def solve():
    size = int(input())
    line = input().split()

    sorted_list = [line[0]]

    prev = line[0]
    operations = 0
    for cur in line[1:]:
        if len(prev) < len(cur):
            h = 'h'
        elif len(prev) == len(cur):
            if int(prev) >= int(cur):
                cur = cur+'0'
                operations += 1
        else:
            diff = len(prev) - len(cur)
            operations += diff
            if int(prev[:len(cur)]) < int(cur):
                cur += '0'*diff
            elif int(prev[:len(cur)]) > int(cur):
                cur += '0'*diff
                cur = cur+'0'
                operations += 1
            else:
                if prev[-1] == '9':
                    cur += '0'*(diff+1)
                    operations += 1
                else:
                    cur += prev[-1*diff:]
        prev = cur
        sorted_list.append(cur)
    # for i in range(1, size):
    #     if line[i] == line[i-1]:
    #         print('equals')
    #     print(line[i])

    print(sorted_list)

    return operations


for testCase in range(1, testCases + 1):
    
    print("Case #" + str(testCase) + ": " + ("%d" % solve()))