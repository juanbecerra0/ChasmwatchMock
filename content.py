import git
from git_contributions_importer import *

repo = git.Repo("F:/Chasmwatch")
mock_repo = git.Repo("F:/GitHub/ChasmwatchMock")

importer = Importer([repo], mock_repo)
importer.set_author('becerrajuan007@gmail.com')
#importer.set_author('juanbecerra@u.boisestate.edu')
#importer.set_author('47235983+juanbecerra0@users.noreply.github.com')

importer.import_repository()
