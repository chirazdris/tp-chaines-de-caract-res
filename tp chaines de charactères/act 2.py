def replace_many(s, L1, L2):
    for i in range(len(L1)):
        s = s.replace(L1[i], L2[i])
    return s


result = replace_many("aabc", ['a', 'b', 'c'], ['b', 'a', 'd'])
print(result)

