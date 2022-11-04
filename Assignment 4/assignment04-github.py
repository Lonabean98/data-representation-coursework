from github import Github
from config import config as cfg
apikey = cfg["git@github.com:Lonabean98/Assignment-04.git"]

# use your own key
g = Github(apikey)
for repo in g.get_user().get_repos():
    print(repo.name)
