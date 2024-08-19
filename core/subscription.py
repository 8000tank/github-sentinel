class SubscriptionManager:
    def __init__(self):
        self.subscriptions = []

    def add_subscription(self, repo_url):
        if repo_url not in self.subscriptions:
            self.subscriptions.append(repo_url)

    def remove_subscription(self, repo_url):
        if repo_url in self.subscriptions:
            self.subscriptions.remove(repo_url)

    def list_subscriptions(self):
        return self.subscriptions
