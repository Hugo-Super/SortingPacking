# ToDo 封装和可视化

# 导包
from typing import List
import random


# import time #测时用
# 拉重量数据，需要与小车编号进行对应
#初始化
fishlist = []
selectfishindex = []
TARGET = 3000   #一箱目标总值
PermissionError = 10    #误差范围
ThresholdValue = 900    #阈值
CarNumber = 6   #小车总数

# 排列组合算法函数
def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    def dfs(candidates, begin, size, path, res, target, ):
        # if target < 0:
        # return
        if -PermissionError < target < PermissionError:
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


# ToDo 模拟读取到PLC发来加了一条鱼的重量信息
def infish():
    fish = random.randint(200, 300)
    return fish


# ToDo 将当前这第一块鱼片装箱
def packfish(movefish: int):
    print("将当前这第一块鱼片重量为%d装箱了..." % movefish)


# ToDo 将当前这第一块鱼片丢弃
def abandonfish(movefish: int):
    print("将当前这第一块鱼片重量为%d丢弃了..." % movefish)


# 换一个新箱子
def changebox():
    target = TARGET
    print("换了一个新箱子")
    return target



# tks = time.time()  #测时用
target = changebox()
while True:

    # 判断目标值是否达到阈值以下
    if target < ThresholdValue:
        selectfishlist = combinationSum(fishlist, target)
        print(selectfishlist)
        if len(selectfishlist) == 0:
            print("此次排列组合没有排出，正在重新排列...")
            movefish = fishlist.pop(0)
            abandonfish(movefish)
            fishlist.append(infish())
            print(str(fishlist) + "没排出")
            continue
        else:
            print(str(fishlist) + "排出了")
            onlyselectfishlist = selectfishlist[0]  # 排出多种情况选第一种，鱼片下得早
            print(onlyselectfishlist)

            for onlyselectfish in onlyselectfishlist:  # 得到每一个鱼片的值，去找到对应的index编号
                selectfishindex.append(fishlist.index(onlyselectfish))
                print(selectfishindex)

            for i in range(len(fishlist)):  # 以当前到达阈值后为基准，从0开始迭代
                if i in selectfishindex:  # 判断是否到了相应index编号，没有：废弃当前鱼片；有：装箱当前鱼片
                    movefish = fishlist.pop(0)
                    packfish(movefish)
                    fishlist.append(infish())
                    print(str(fishlist) + "排出了，且装箱后")
                    continue
                else:
                    movefish = fishlist.pop(0)
                    abandonfish(movefish)
                    fishlist.append(infish())
                    print(str(fishlist) + "排出了，且废弃后")
                    continue
        print(str(fishlist) + "一轮鱼片循环前")

        target = changebox()
        selectfishindex.clear()
        continue

    # 判断列表是否装到足够的小车个数
    if len(fishlist) == CarNumber:
        movefish = fishlist.pop(0)
        packfish(movefish)
        fishlist.append(infish())
        target = target - movefish
        print("现在的target值是：%d" % target)
        continue

    fishlist.append(infish())
    print(fishlist)

# tjs = time.time()#测时用
# print(tjs-tks)#测时用

# 选择装箱：
# 1.阈值前直接装箱
# 2.判定阈值
# 3.阈值后调用排列组合算法求最优解装箱
# 4.整个结构实现循环 箱子盛满 换一个
