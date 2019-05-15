lisp_file_extensions = [
    'lisp',
    'lsp',
    'asd'
]

def is_lisp_blob(blob):
    filename = blob.name
    return is_file_ext_in(filename, lisp_file_extensions)


def is_file_ext_in(filepath, ext_list):
    matches = [is_file_ext(filepath, ext) for ext in ext_list]
    return any(matches)


def is_file_ext(filepath, ext):
    return filepath.endswith('.' + ext)
