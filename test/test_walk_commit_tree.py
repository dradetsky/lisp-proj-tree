from lisp_proj_tree.walk_commits import (
    walk_tree,
    walk_lisp_blobs
)

from .util import get_repo


def check_for_n_blobs(repo, n_blobs, walk_fn=walk_tree):
    hct = repo.heads.master.commit.tree
    blobs = list(walk_fn(hct))
    assert len(blobs) == n_blobs


def test_walk_head_file_counts():
    chirp_repo = get_repo('chirp')
    woo_repo = get_repo('woo')
    cl_yaml_repo = get_repo('cl-yaml')

    check_for_n_blobs(chirp_repo, 38)
    check_for_n_blobs(woo_repo, 46)
    check_for_n_blobs(cl_yaml_repo, 44)

def test_walk_head_lisp_file_counts():
    def check_lisp_for_n_blobs(repo, n_blobs):
        return check_for_n_blobs(repo, n_blobs, walk_fn=walk_lisp_blobs)

    chirp_repo = get_repo('chirp')
    woo_repo = get_repo('woo')
    cl_yaml_repo = get_repo('cl-yaml')

    check_lisp_for_n_blobs(chirp_repo, 32)
    check_lisp_for_n_blobs(woo_repo, 23)
    check_lisp_for_n_blobs(cl_yaml_repo, 17)
