import os

# def solution(file_object):
#     d = []
#     with open(file_object, 'r') as f:
#         for line in f:
#             line.split("\n")
#             try:
#                 if -1000000000 < int(line.strip()) < 1000000000:
#                     # d.append(int(line.strip()))
#                     yield int(line.strip())
#             except:
#                 pass
# import io
#
f = "137\n-104\n2 58\n       +0\n++3\n+1\n 23.9\n2000000000\n-0\nfive\n -1\n"
# def solution(f):
#     # with open(file_object, 'r') as f:
#     #     for line in f:
#     # d = [x.strip() for x in f.splitlines()]
#     for x in io.StringIO(f):
#         try:
#             if -1000000000 < int(x) < 1000000000:
#                 yield int(x.strip())
#         except:
#             pass

import io
def solution(file_object):
    with open(file_object, 'r') as f:
        for line in f:
            for x in io.StringIO(line):
                try:
                    if -1000000000 < int(x) < 1000000000:
                        yield int(x.strip())
                except:
                    pass

for i in solution('file2'):
    print(i)


# for line in io.StringIO(f):
#     print(line.strip())

# solution('file2')

