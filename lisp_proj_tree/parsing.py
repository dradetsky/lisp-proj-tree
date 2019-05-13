from parse_lisp import parse

def parse_blob(blob):
    code = read_blob(blob)
    in_str = '(' + code + ')'
    lol = parse(in_str)
    return lol

def read_blob(blob):
    code_bytes = blob.data_stream.read()
    code = code_bytes.decode('utf8')
    return code

def debug_parse_blob(blob):
    from parse_lisp import debug_parse

    code = read_blob(blob)
    in_str = '(' + code + ')'
    ret  = debug_parse(in_str)
    return ret
