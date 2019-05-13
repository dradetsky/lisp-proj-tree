from lisp_proj_tree.parsing import (
    parse_blob
)

from .util import get_repo

# as of parse-lisp 0.0.0, or bdbf12b14e3375318bd3aad05d94905c7924e7eb,
# this should be ok.
def test_parse_good_file():
    repo = get_repo('woo')
    hct = repo.heads.master.commit.tree
    blob_ev = hct.trees[2].blobs[0]
    assert blob_ev.path == 'src/ev.lisp'

    out = parse_blob(blob_ev)
    assert out is not None
    # in-package, defpackage, in-package
    #
    # in theory, this can break on updates to woo. i mean, in theory.
    assert len(out) == 3
