import os, os.path
#
# for root, dirs, files in os.walk('/home/pk/GITHUB/algorithms/exercises'):
#     for f in files:
#         fullpath = os.path.join(root, f)
#         if os.path.splitext(fullpath)[1] == '.txt':
#             pass
#             print(fullpath)


path = '/home/pk/GITHUB/algorithms/exercises'
# print(os.chdir(path))
# with os.scandir(path) as it:
#     for entry in it:
#         if not entry.name.startswith('.') and entry.is_file():
#             print(entry.name)

for root, dirs, files in os.walk(path):
    for name in files:
        print(os.path.join(root, name))
    # for name in dirs:
    #     print(os.path.join(root, name))

# The method walk() generates the file names in a directory tree by walking the tree either top-down or bottom-up.
# os.walk(top, topdown=True, onerror=None, followlinks=False)