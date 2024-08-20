import re
import threading
import cmd
from config.settings import GITHUB_API_TOKEN
from core.subscription import SubscriptionManager
from core.update_fetcher import UpdateFetcher
from core.reporter import Reporter
from core.scheduler import Scheduler

class GitHubSentinelCLI(cmd.Cmd):
    intro = "Welcome to GitHub Sentinel. Type help or ? to list commands.\n"
    prompt = "(GitHub Sentinel) "

    def __init__(self):
        super().__init__()
        self.subscription_manager = SubscriptionManager()
        self.update_fetcher = UpdateFetcher(GITHUB_API_TOKEN)
        self.reporter = Reporter()
        self.scheduler = Scheduler('daily', self.scheduled_task)
        self.scheduler_thread = threading.Thread(target=self.scheduler.start, daemon=True)
        self.scheduler_thread.start()

    def is_valid_repo_url(self, repo_url):
        if not repo_url:
            return False
        # Regex to check if the URL is a valid GitHub repository
        pattern = r'^https:\/\/github\.com\/[\w\-]+\/[\w\-]+\/?$'
        return re.match(pattern, repo_url) is not None

    def prompt_for_valid_repo_url(self):
        while True:
            repo_url = input("Please enter a valid GitHub repository URL: ")
            if self.is_valid_repo_url(repo_url):
                return repo_url
            else:
                print("Invalid GitHub repository URL. Please try again.")

    def do_add(self, repo_url):
        "Add a repository to the subscription list: add https://github.com/user/repo"
        if not self.is_valid_repo_url(repo_url):
            print("Invalid GitHub repository URL.")
            repo_url = self.prompt_for_valid_repo_url()
        
        self.subscription_manager.add_subscription(repo_url)
        print(f"Subscribed to {repo_url}")

    def do_remove(self, repo_url):
        "Remove a repository from the subscription list: remove https://github.com/user/repo"
        if not self.is_valid_repo_url(repo_url):
            print("Invalid GitHub repository URL.")
            repo_url = self.prompt_for_valid_repo_url()
        
        self.subscription_manager.remove_subscription(repo_url)
        print(f"Unsubscribed from {repo_url}")

    def do_list(self, arg):
        "List all subscribed repositories: list"
        subscriptions = self.subscription_manager.list_subscriptions()
        print("Subscribed repositories:")
        for repo in subscriptions:
            print(f" - {repo}")

    def do_fetch(self, repo_url):
        "Fetch the latest release information for a subscribed repository: fetch https://github.com/user/repo"
        if not self.is_valid_repo_url(repo_url):
            print("Invalid GitHub repository URL.")
            repo_url = self.prompt_for_valid_repo_url()
        
        release_info = self.update_fetcher.fetch_latest_release(repo_url)
        report = self.reporter.generate_report(release_info)
        print(report)

    def do_quit(self, arg):
        "Quit the GitHub Sentinel: quit"
        print("Goodbye!")
        return True

    def scheduled_task(self):
        for repo_url in self.subscription_manager.list_subscriptions():
            release_info = self.update_fetcher.fetch_latest_release(repo_url)
            report = self.reporter.generate_report(release_info)
            print(f"Scheduled Update for {repo_url}:\n{report}")

if __name__ == '__main__':
    GitHubSentinelCLI().cmdloop()
