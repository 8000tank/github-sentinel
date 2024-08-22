import requests

class GitHubAPI:
    def __init__(self, token):
        self.token = token
        self.base_url = "https://api.github.com"

    def get_latest_release(self, repo_name):
        """Fetch the latest release information for a given repository in [username]/[repository] format."""
        url = f"{self.base_url}/repos/{repo_name}/releases/latest"
        headers = {
            "Authorization": f"token {self.token}",
            "Accept": "application/vnd.github.v3+json"
        }
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()
