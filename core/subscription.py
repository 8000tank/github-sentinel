import os
import json

class SubscriptionManager:
    def __init__(self):
        self.subscriptions_file = os.path.join(os.path.dirname(__file__), '..', 'subscriptions.json')
        self.subscriptions = self.load_subscriptions()

    def load_subscriptions(self):
        """Load subscriptions from the JSON file."""
        if os.path.exists(self.subscriptions_file):
            with open(self.subscriptions_file, 'r') as file:
                return json.load(file)
        else:
            return []

    def save_subscriptions(self):
        """Save the current subscriptions to the JSON file."""
        with open(self.subscriptions_file, 'w') as file:
            json.dump(self.subscriptions, file, indent=4)

    def add_subscription(self, repo_name):
        """Add a repository to the subscription list in [username]/[repository] format."""
        if repo_name not in self.subscriptions:
            self.subscriptions.append(repo_name)
            self.save_subscriptions()
            print(f"Subscribed to {repo_name}")
        else:
            print(f"Already subscribed to {repo_name}")

    def remove_subscription(self, repo_name):
        """Remove a repository from the subscription list in [username]/[repository] format."""
        if repo_name in self.subscriptions:
            self.subscriptions.remove(repo_name)
            self.save_subscriptions()
            print(f"Unsubscribed from {repo_name}")
        else:
            print(f"Not subscribed to {repo_name}")

    def list_subscriptions(self):
        """List all subscribed repositories in [username]/[repository] format."""
        return self.subscriptions
