import time
# import openai
from openai import OpenAI
import os

# 读取环境变量 "OPENAI_API_KEY"
openai_api_key = os.getenv("OPENAI_API_KEY")
# openai_api_key = os.environ.get("OPENAI_API_KEY")
print("OpenAI API Key:", openai_api_key)


def call_openai_api():
    try:
        client = OpenAI()
        response = client.chat.completions.create(
            model="gpt-4o-mini",  # 确保使用的是正确的模型
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "What day is it today?"}
            ],
            max_tokens=50
        )
        print(response.choices[0].message)
    except Exception as e:
        print(f"An error occurred: {e}")
        raise e
        time.sleep(10)  # 等待一段时间后重试


# for _ in range(1):
call_openai_api()
# time.sleep(1)  # 每次调用后等待一秒，避免过快频繁调用
