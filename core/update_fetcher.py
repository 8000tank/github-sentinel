from utils.github_api import GitHubAPI


class UpdateFetcher:
    def __init__(self, token):
        self.github_api = GitHubAPI(token)

    def fetch_latest_release(self, repo_url):
        return self.github_api.get_latest_release(repo_url)

    def fetch_issues_and_pulls(self, repo):
        """Fetch issues and pulls requests from the specified repo."""
        issues = self.github_api.fetch_issues(repo)
        pulls = self.github_api.fetch_pull_requests(repo)

        if issues is None or pulls is None:
            print(f"Failed to fetch issues and pulls data for {repo}")
            return None

        return issues, pulls

    def generate_markdown_report(self, repo):
        """Fetch data and generate a Markdown report for the specified repo."""
        issues, pulls = self.fetch_issues_and_pulls(repo)

        # Save the results to a Markdown file
        self.github_api.save_to_markdown(repo, issues, pulls)
