import git
from git_contributions_importer import *

repo = git.Repo("D:/Chasmwatch")
mock_repo = git.Repo("D:/ChasmwatchMock")

importer = Importer([repo], mock_repo)
importer.set_author('becerrajuan007@gmail.com')

importer.import_repository()