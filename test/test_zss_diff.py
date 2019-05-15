import pytest

from lisp_proj_tree.diff_ops import (
    get_incr_diff_idx
)
from lisp_proj_tree.zss_diff import (
    parse_to_zss_tree,
    diff_edit_dist
)

from .util import get_repo

@pytest.mark.skip
def test_calc_zss_for_known_woo_diff():
    repo = get_repo('woo')
    # want 764b62b7be3f6fcecf0385d5d9e910ed643ccc39
    cmt = [c for c in repo.iter_commits(max_count=5)][-1]
    diff_idx = get_incr_diff_idx(cmt)
    diff = diff_idx[0]
    dist = diff_edit_dist(diff)
    assert dist == 58

@pytest.mark.skip
def test_blob_to_zss():
    repo = get_repo('woo')
    # want 764b62b7be3f6fcecf0385d5d9e910ed643ccc39
    cmt = [c for c in repo.iter_commits(max_count=5)][-1]
    diff_idx = get_incr_diff_idx(cmt)
    diff = diff_idx[0]
    blob = diff.a_blob
    tree = parse_to_zss_tree(blob)
