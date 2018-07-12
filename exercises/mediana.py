# from statistics import median
#
# print(median([1, 3, 6, 4]))

lm = [[1, 3, 6, 4], [1, 22, 13, 4], [11, 33, 9, 4]]

# def median(lst):
#     sortedLst = sorted(lst)
#     lstLen = len(lst)
#     index = (lstLen - 1) // 2
#
#     if (lstLen % 2):
#         return sortedLst[index]
#     else:
#         return (sortedLst[index] + sortedLst[index + 1])/2.0
#
# print(median(lm))

def median(l):
    half = len(l) // 2
    l.sort()
    if not len(l) % 2:
        return (l[half - 1] + l[half]) / 2.0
    return l[half]

a = [median(x) for x in lm]

print(a)