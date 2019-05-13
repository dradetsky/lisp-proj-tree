def is_file_ext_in(filepath, ext_list):
    matches = [is_file_ext(filepath, ext) for ext in ext_list]
    return any(matches)


def is_file_ext(filepath, ext):
    return filepath.endswith('.' + ext)
