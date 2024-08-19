class Reporter:
    def generate_report(self, release_info):
        if release_info:
            report = (
                f"Latest Release for {release_info['name']}:\n"
                f"Tag: {release_info['tag_name']}\n"
                f"Published at: {release_info['published_at']}\n"
                f"Author: {release_info['author']['login']}\n"
                f"URL: {release_info['html_url']}\n"
                f"Body: {release_info['body']}\n"
            )
        else:
            report = "No release information found."
        return report
