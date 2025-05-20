def combination_k(s, k):
    '''
    字符串 s 中选取 k(0 <= k <= len(s)) 个元素，进行组合，以列表的形式返回所有可能的组合
    s --> 输入的字符串
    k --> 选取的元素的个数

    测试结果如下：
    combination_k('abc', 2) >>> ['ab', 'ac', 'bc']

    combination_k('c', 2)   >>> []
        combination_k('c', 2) 的递归内部解释如下：
            --> combination_k('c', 2)
                --> for i in combination_k('', 1):
                        c + i
                    # 由于 combination_k('', 1) 的返回结果是一个空列表，这 for 循环遍历不会被执行，所以返回初始设定的值 []
    '''
    # recursive basis
    if k == 0: return ['']
    # recursive chain
    subletters = []
    # 此处涉及到一个 python 遍历循环的特点：当遍历的对象为空（列表，字符串...）时，循环不会被执行，range(0) 也是一样
    for i in range(len(s)):
        for letter in combination_k(s[i + 1:], k - 1):
            subletters += [s[i] + letter]
    return subletters

#[152,235,548]
def combination_all(s):
    '''
    本函数配合 combination_k 函数实现全组合
    s --> 组合元素的样本
    以列表的形式返回所有长度可能的组合

    测试如下：
    combination_all('abc') >>> ['a', 'b', 'c', 'ab', 'ac', 'bc', 'abc']
    '''
    comb_list = []
    # 通过 for 循环调用 combination_k(s, k) 获取不同 k 值下的所有组合
    for i in range(1, len(s) + 1):
        comb_list += combination_k(s, i)
    return comb_list


def main():
    letter = 'abcdefghijklmnopqrstuvwxyz'
    print('组合及全组合计算器')
    print('组合总样本：' + letter)
    mode = eval(input('请选择运行模式：1 代表‘组合’； 2 代表‘全组合’:'))
    if mode == 1:
        print('您选择的是组合模式:')
        length = eval(input('请输入组合元素样本的长度:'))
        letter_numbers = eval(input('请输入入选组合元素的个数:'))
        print('您选择的组合样本是：' + letter[:length] + ',参与组合的元素个数是：' + str(letter_numbers))
        c_k = combination_k(letter[:length], letter_numbers)
        print(c_k)
    elif mode == 2:
        print('您选择的是全组合模式:')
        length = eval(input('请输入组合元素样本的长度:'))
        print('您选择的组合样本是：' + letter[:length])
        c_a = combination_all(letter[:length])
        print(c_a)


if __name__ == '__main__':
    main()
