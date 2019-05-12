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

