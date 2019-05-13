import pytest

from lisp_proj_tree.hist_parsing import (
    parse_head_lisp_blob,
    parse_every_lisp_blob,
)

from .util import get_repo

def check_parse_all_no_fails(repo):
    t, f, r = parse_every_lisp_blob(repo)
    assert t > 0
    assert f == 0

def test_can_parse_woo():
    repo = get_repo('woo')
    check_parse_all_no_fails(repo)

def test_can_parse_cl_yaml():
    repo = get_repo('cl-yaml')
    check_parse_all_no_fails(repo)

@pytest.mark.skip
def test_can_parse_humbler():
    repo = get_repo('humbler')
    check_parse_all_no_fails(repo)
