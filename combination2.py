def combine(n: int, k: int):
    res = []
    path = []
    def backtrack(n, k, StartIndex):
        if len(path) == k:
            res.append(path[:])
            return
        for i in range(StartIndex, n-(k-len(path)) + 2):
            path.append(i)
            backtrack(n, k, i+1)
            path.pop()
    backtrack(n, k, 1)
    print(res)

def main():
    combine(4,2)

if __name__ == '__main__':
    main()



