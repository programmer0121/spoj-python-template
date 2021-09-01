import sys

def read(): return int(input())
def nums(): return numsL(input().strip())
def numsL(line): return list(map(int, line.split()))
def words(): return input().strip().split()
def lines(): return [l.strip() for l in sys.stdin.readlines()]
def disp(arr, sep=' '): print(sep.join([str(x) for x in arr]))
def flatten(arr): return [elem for row in arr for elem in row]

