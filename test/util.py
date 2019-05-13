from os import path

from git import Repo

def get_repo(name):
    repos_base = 'data'
    repo_path = path.join(repos_base, name)
    repo = Repo(repo_path)
    return repo
