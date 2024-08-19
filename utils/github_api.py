import requests

class GitHubAPI:
    def __init__(self, token):
        self.token = token
        self.headers = {'Authorization': f'token {self.token}'}

    def get_latest_release(self, repo_url):
        repo_name = "/".join(repo_url.rstrip('/').split('/')[-2:])
        api_url = f"https://api.github.com/repos/{repo_name}/releases/latest"
        response = requests.get(api_url, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        else:
            return None
