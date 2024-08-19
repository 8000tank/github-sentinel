from utils.github_api import GitHubAPI

class UpdateFetcher:
    def __init__(self, token):
        self.github_api = GitHubAPI(token)

    def fetch_latest_release(self, repo_url):
        release_info = self.github_api.get_latest_release(repo_url)
        return release_info
