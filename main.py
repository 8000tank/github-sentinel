from config.settings import GITHUB_API_TOKEN
from core.update_fetcher import UpdateFetcher
from core.reporter import Reporter

def main():
    repo_url = "https://github.com/langchain-ai/langchain/"
    update_fetcher = UpdateFetcher(GITHUB_API_TOKEN)
    reporter = Reporter()

    release_info = update_fetcher.fetch_latest_release(repo_url)
    report = reporter.generate_report(release_info)

    print(report)

if __name__ == "__main__":
    main()
