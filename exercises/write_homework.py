# def get_words(in_file_name, out_file_name):
#
#     with open(in_file_name, 'w') as f:
#         for line in f:
#             with open(out_file_name, 'w') as g:
#                 g.writelines((str(line) for line in f))
#
#
# get_words('listahtml', 'output')

def get_words(in_file_name, out_file_name):

    with open(in_file_name, 'r') as f:
        for line in f:
            with open(out_file_name, 'w') as g:
                g.writelines((str(line)[18:] for line in f))

get_words('listahtml', 'output')