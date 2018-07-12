import os
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

