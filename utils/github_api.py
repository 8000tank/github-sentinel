import requests
import os


class GitHubAPI:
    def __init__(self, github_api_token):
        self.github_api_token = github_api_token
        self.headers = {'Authorization': f'token {self.github_api_token}'}
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

    def fetch_issues(self, repo):
        url = f"{self.base_url}/repos/{repo}/issues"
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed to fetch issues for {repo}")
            return None

    def fetch_pull_requests(self, repo):
        url = f"{self.base_url}/repos/{repo}/pulls"
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed to fetch pull requests for {repo}")
            return None

    def save_to_markdown(self, repo, issues, pulls):
        filename = f"{repo.replace('/', '_')}_{self.get_current_date()}.md"
        with open(filename, 'w') as file:
            file.write(
                f"# {repo} - Update Report ({self.get_current_date()})\n\n")
            file.write("## Issues\n")
            for issue in issues:
                file.write(f"- {issue['title']} (#{issue['number']})\n")
            file.write("\n## Pull Requests\n")
            for pr in pulls:
                file.write(f"- {pr['title']} (#{pr['number']})\n")
        print(f"Markdown report generated: {filename}")

    @staticmethod
    def get_current_date():
        from datetime import datetime
        return datetime.now().strftime('%Y-%m-%d')
