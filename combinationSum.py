from typing import List
import random
#import math


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        def dfs(candidates, begin, size, path, res, target, ):
            # if target < 0:
            # return
            if -10< target < 10:
                res.append(path)
                return

            for index in range(begin + 1, size):
                dfs(candidates, index, size, path + [candidates[index]], res, target - candidates[index])

        size = len(candidates)
        if size == 0:
            return []
        path = []
        res = []
        dfs(candidates, 0, size, path, res, target)
        return res

# candidates 候选数组
# begin      搜索起点
# len        冗余变量，是 candidates 里的属性，可以不传
# target     每减去一个元素，目标值变小
# path       从根结点到叶子结点的路径，是一个栈
# res        结果集列表


def RandomTest():
    fish = random.sample(range(200, 300), 8)
    print("生成的随机鱼片列："+str(fish))
    target = random.randint(900, 1100)
    print("此次模拟的随机阈值："+str(target))
    print(Solution.combinationSum(self=1, candidates=fish, target=target))

def main():
    RandomTest()


if __name__ == "__main__":
    main()
    print("程序结束")