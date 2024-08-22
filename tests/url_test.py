
repo_url = "https://github.com/DjangoPeng/GitHubSentinel"
repo_name = "/".join(repo_url.rstrip('/').split('/')[-2:])
print(repo_name)
api_url = f"https://api.github.com/repos/{repo_name}/releases/latest"
print(api_url)