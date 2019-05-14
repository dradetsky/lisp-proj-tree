# XXX: possibly undesirable direct dependency on sly; should we fully
# encapsulate within parser?
from sly.lex import LexError

from .parsing import (
    debug_parse_blob,
    parse_blob
)

from .walk_commits import (
    master_begin_to_end,
    master_last_20,
    walk_lisp_blobs,
    walk_changed_lisp_blobs,
)

# this is kinda for dev; don't intend to use for real
def parse_every_lisp_blob(repo):
    total = 0
    fails = 0

    for cmt in master_begin_to_end(repo):
        for blob in walk_changed_lisp_blobs(cmt):
            total += 1
            fails += report_fail_blob(cmt, blob)

    repo_name = repo.remote().url
    ratio = fails/total
    ret = [
        total,
        fails,
        ratio
    ]
    print(repo_name)
    print('t:{} f:{}'.format(total, fails))
    print(ratio)
    return ret


def parse_head_lisp_blob(repo):
    total = 0
    fails = 0

    cmt = repo.heads.master.commit
    tree = cmt.tree
    for blob in walk_lisp_blobs(tree):
        print(blob.path)
        total += 1
        fails += report_fail_blob(cmt, blob)

    repo_name = repo.remote().url
    print(repo_name)
    print('t:{} f:{}'.format(total, fails))
    print(fails/total)


def fail_summary(cmt, blob, msg=''):
    summary = '{path} {sha} {date} {msg}'.format(
        path=blob.path,
        sha=cmt.hexsha,
        date=cmt.committed_datetime,
        msg=msg
    )
    return summary

def report_fail_blob(cmt, blob):
    try:
        ret, par, _, _ = debug_parse_blob(blob)
        if ret is None:
            return 1
        elif has_errors(par):
            breakpoint()
            return 1
        else:
            return 0
    except LexError as e:
        print(fail_summary(cmt, blob, e.args[0]))
        return 1


def has_errors(par):
    status = hasattr(par, 'errorok') and not par.errorok
    return status
