import threading
import cmd
import re
from config.settings import GITHUB_API_TOKEN
from core.subscription import SubscriptionManager
from core.update_fetcher import UpdateFetcher
from core.reporter import Reporter
from core.scheduler import Scheduler
from utils.github_api import GitHubAPI
from core.llm import LLMClient


class GitHubSentinelCLI(cmd.Cmd):
    intro = "Welcome to GitHub Sentinel. Type help or ? to list commands.\n"
    prompt = "(GitHub Sentinel) "

    def __init__(self):
        super().__init__()
        self.subscription_manager = SubscriptionManager()
        self.update_fetcher = UpdateFetcher(GITHUB_API_TOKEN)

        # Initialize LLMClient with your OpenAI API key
        llm_client = LLMClient()
        # Initialize Reporter with LLMClient
        self.reporter = Reporter(llm_client)

        self.scheduler = Scheduler('daily', self.scheduled_task)
        self.scheduler_thread = threading.Thread(
            target=self.scheduler.start, daemon=True)
        self.scheduler_thread.start()

    def is_valid_repo_name(self, repo_name):
        if not repo_name:
            return False
        # Regex to check if the input is in [username]/[repository] format
        pattern = r'^[\w\-]+\/[\w\-]+$'
        return re.match(pattern, repo_name) is not None

    def prompt_for_valid_repo_name(self):
        while True:
            repo_name = input(
                "Please enter a valid GitHub repository name [username/repository]: ")
            if self.is_valid_repo_name(repo_name):
                return repo_name
            else:
                print("Invalid GitHub repository name. Please try again.")

    def do_add(self, repo_name):
        "Add a repository to the subscription list: add username/repository"
        if not self.is_valid_repo_name(repo_name):
            print("Invalid GitHub repository name.")
            repo_name = self.prompt_for_valid_repo_name()

        self.subscription_manager.add_subscription(repo_name)
        print(f"Subscribed to {repo_name}")

    def do_remove(self, repo_name):
        "Remove a repository from the subscription list: remove username/repository"
        if not self.is_valid_repo_name(repo_name):
            print("Invalid GitHub repository name.")
            repo_name = self.prompt_for_valid_repo_name()

        self.subscription_manager.remove_subscription(repo_name)
        print(f"Unsubscribed from {repo_name}")

    def do_list(self, arg):
        "List all subscribed repositories: list"
        subscriptions = self.subscription_manager.list_subscriptions()
        print("Subscribed repositories:")
        for repo in subscriptions:
            print(f" - {repo}")

    def do_fetch(self, repo_name):
        "Fetch the latest release information for a subscribed repository: fetch username/repository"
        if not self.is_valid_repo_name(repo_name):
            print("Invalid GitHub repository name.")
            repo_name = self.prompt_for_valid_repo_name()

        release_info = self.update_fetcher.fetch_latest_release(repo_name)
        report = self.reporter.generate_report(release_info)
        print(report)

    def do_quit(self, arg):
        "Quit the GitHub Sentinel: quit"
        print("Goodbye!")
        return True

    def scheduled_task(self):
        for repo_name in self.subscription_manager.list_subscriptions():
            release_info = self.update_fetcher.fetch_latest_release(repo_name)
            report = self.reporter.generate_report(release_info)
            print(f"Scheduled Update for {repo_name}:\n{report}")

            # Example command to generate report

    def do_generate_report(self, repo):
        """Generate a report for a subscribed repository: generate_report user/repo"""
        self.update_fetcher.generate_markdown_report(repo)
        markdown_file = f"{repo.replace(
            '/', '_')}_{GitHubAPI.get_current_date()}.md"
        self.reporter.generate_summary_report(markdown_file)


if __name__ == '__main__':
    GitHubSentinelCLI().cmdloop()
