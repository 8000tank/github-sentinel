# llm.py

from openai import OpenAI


class LLMClient:
    def __init__(self):
        self.client = OpenAI()

    def summarize_issues_and_pulls(self, issues, pulls):
        content = f"Issues:\n{issues}\n\nPull Requests:\n{pulls}\n"
        response = self.client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that summarizes GitHub issues and pull requests."},
                {"role": "user", "content": content}
            ]
        )
        return response.choices[0].message.content
