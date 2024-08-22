import os
from dotenv import load_dotenv

load_dotenv()  # 加载 .env 文件中的环境变量

GITHUB_API_TOKEN = os.getenv('GITHUB_API_TOKEN')
SCHEDULE_INTERVAL = os.getenv('SCHEDULE_INTERVAL', 'daily')

# print(f"git token: {GITHUB_API_TOKEN}, interval: {SCHEDULE_INTERVAL}")