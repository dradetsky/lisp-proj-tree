from .util import is_lisp_blob

def master_begin_to_end(repo):
    for cmt in reversed(list(repo.iter_commits())):
        yield cmt

def master_last_20(repo):
    for cmt in repo.iter_commits(max_count=20):
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


def walk_lisp_blobs(tree):
    for blob in walk_tree(tree):
        if is_lisp_blob(blob):
            yield blob

def walk_changed_lisp_blobs(cmt):
    changed_paths = cmt.stats.files.keys()
    tree = cmt.tree

    return walk_given_lisp_blobs(tree, changed_paths)

def walk_given_lisp_blobs(tree, given_paths):
    for blob in walk_tree(tree):
        if is_lisp_blob(blob) and (blob.path in given_paths):
            yield blob
