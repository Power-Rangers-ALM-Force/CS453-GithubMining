from github import Github


# Helper class for identifying the process smells
class GitHubDataFetcher:

    def __init__(self, token, repo_owner, repo_name):
        self.github_inst = Github(token)
        self.repo = self.github_inst.get_repo(repo_owner + '/' + repo_name)
        self.commits = self.repo.get_commits()
        self.issues = self.repo.get_issues()

    def get_issues(self):
        return self.issues

    def get_commits(self):
        return self.commits
