# This is a demo task.
#
# Write a function:
#
# def solution(A)
#
# that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.
#
# For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.
#
# For another example, given A = [1, 2, 3], the function should return 4.
#
# Given A = [−1, −3], the function should return 1.
#
# Assume that:
#
# N is an integer within the range [1..100,000];
# each element of array A is an integer within the range [−1,000,000..1,000,000].
# Complexity:
#
# expected worst-case time complexity is O(N);
# expected worst-case space complexity is O(N), beyond input storage (not counting the storage required for input arguments).
# Elements of input arrays can be modified.

A = [1, 3, 6, 4, 1, 2, 5]
B = [2]
C= [1, 2, 3]
# def solution(A):
#     sorted_list = sorted(A)
#     a = max(sorted_list)
#     for x in range(0, len(A)):
#         if len(A) > 1 and a > 0 and x > 0 and sorted_list[x] != sorted_list[x+1] + 1:
#             return sorted_list[x] + 1
#     if a <= 0:
#         return 1
#     elif len(A) == 1 and A[0] not in [0,1]:
#         return a - 1
#     else:
#         return a + 1
#
# # print(solution(A))
# print(solution(A))

def solution(a):
    positives = frozenset((value for value in a if value > 0))
    print(positives)
    for i in range(1, len(a) + 1):
        print(i)
    return next((i for i in range(1, len(a) + 2) if not i in positives), 1)

print(solution(C))