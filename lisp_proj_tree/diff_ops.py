from .util import is_lisp_blob

# TODO: (de)compose generators
def iter_incr_diff_idxs(repo, **kwargs):
    for cmt in reversed(list(repo.iter_commits(**kwargs))):
        incr_diff_idx = get_incr_diff_idx(cmt)
        yield incr_diff_idx

def get_incr_diff_idx(cmt):
    parent = commit_parent(cmt)
    incr_diff_idx = cmt.diff(parent)
    return incr_diff_idx

# TODO: check reasoning regarding choice of parent; does this work for
# all cases of multiple parents?
def commit_parent(cmt):
    parent = cmt.parents[0]
    return parent

def iter_lisp_blob_diffs(diff_idx):
    for diff in diff_idx:
        if is_lisp_blob(diff.a_blob) and is_lisp_blob(diff.b_blob):
            yield diff
