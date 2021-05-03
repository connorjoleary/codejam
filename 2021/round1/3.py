import sys

name = "A-small"
path = "2021/round1/"

sys.stdin = open(path + name + ".in")

testCases = int(input())

def solve():
    nums = (input().split())
    n, q = nums
    n = int(n)
    q = int(q)
    for i in range(int(n)):  
        ans, score = (input().split())
        score = int(score)
        if score > q/2:
            ans = [a == 'T' for a in ans]
        else:
            ans = [a != 'T' for a in ans]
            score = q - score
        print(ans)
        
    return int(n)


for testCase in range(1, testCases + 1):
    
    print("Case #" + str(testCase) + ": " + ("%d" % solve()))