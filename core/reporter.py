# reporter.py

class Reporter:
    def __init__(self, llm_client):
        self.llm_client = llm_client

    def generate_summary_report(self, markdown_file):
        with open(markdown_file, 'r') as file:
            content = file.read()

        # Extract issues and pull requests sections
        issues_section = self.extract_section(content, "## Issues")
        pulls_section = self.extract_section(content, "## Pull Requests")

        summary = self.llm_client.summarize_issues_and_pulls(
            issues_section, pulls_section)

        # Save the summary to a new Markdown file
        summary_filename = markdown_file.replace('.md', '_summary.md')
        with open(summary_filename, 'w') as file:
            file.write(summary)

        print(f"Summary report generated: {summary_filename}")

    @staticmethod
    def extract_section(content, header):
        start = content.find(header)
        end = content.find("## ", start + 1)
        if end == -1:
            end = len(content)
        return content[start:end].strip()
