from .util import is_file_ext_in

def master_begin_to_end(repo):
    for cmt in reversed(list(repo.iter_commits())):
        yield cmt


def commit_lisp_blobs(cmt):
    pass


def walk_tree(tree):
    blobs = tree.blobs
    subtrees = tree.trees

    while blobs or subtrees:
        if blobs:
            new_blob = blobs.pop(0)
            yield new_blob
        elif subtrees:
            new_subtree = subtrees.pop(0)
            blobs += new_subtree.blobs
            subtrees += new_subtree.trees
        else:
            raise ValueError('lolwut')

def is_lisp_blob(blob):
    lisp_file_extensions = [
        'lisp',
        'lsp',
        'asd'
    ]

    filename = blob.name
    return is_file_ext_in(filename, lisp_file_extensions)


def walk_lisp_blobs(tree):
    for blob in walk_tree(tree):
        if is_lisp_blob(blob):
            yield blob

def walk_changed_lisp_blobs(cmt):
    changed_paths = cmt.stats.files.keys()
    tree = cmt.tree

    for blob in walk_tree(tree):
        if is_lisp_blob(blob) and (blob.path in changed_paths):
            yield blob
