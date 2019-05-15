from loltree import zsstree
from zss import simple_distance

from .parsing import parse_blob

def diff_edit_dist(diff):
    a_tree = parse_to_zss_tree(diff.a_blob)
    b_tree = parse_to_zss_tree(diff.b_blob)
    dist = simple_distance(a_tree, b_tree)
    return dist

def parse_to_zss_tree(blob):
    lolcode = parse_blob(blob)
    # lolcode is now a forest; make it a tree with this one weird trick
    lolcode.insert(0, blob.path)
    tree = zsstree(lolcode)
    return tree
