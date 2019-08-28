def longestCommonPrefix(strs):
    prefix = ''
    # * is the unpacking operator, essential here
    # zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。
    # nums = ['flower','flow','flight']
    # for i in zip(*nums):    print(i)
    #('f', 'f', 'f')('l', 'l', 'l')('o', 'o', 'i')('w', 'w', 'g')
    
    for z in zip(*strs):   
        bag = set(z)
        if len(bag) == 1:
            prefix += bag.pop()
        else:
            break
    return prefix

print(longestCommonPrefix(["flower","flow","flight"]))