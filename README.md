# GitHub Sentinel

## 初始化配置

1. **配置环境变量**  
   在项目根目录下创建一个 `.env` 文件，用于存储 GitHub API Token 等配置信息。

   **`.env` 文件内容示例：**
   ```env
   GITHUB_API_TOKEN=your_github_token_here
   SCHEDULE_INTERVAL=daily
   ```

   使用 `python-dotenv` 库加载环境变量。你可以通过 `pip` 安装：

   ```bash
   pip install python-dotenv
   ```

   更新 `config/settings.py` 文件，加载 `.env` 文件中的环境变量。

   ```python
   import os
   from dotenv import load_dotenv

   load_dotenv()  # 加载 .env 文件中的环境变量

   GITHUB_API_TOKEN = os.getenv('GITHUB_API_TOKEN')
   SCHEDULE_INTERVAL = os.getenv('SCHEDULE_INTERVAL', 'daily')
   ```

2. **安装依赖**
   确保所有的依赖项都已经安装。你可以在 `requirements.txt` 中列出所需的库，并通过 `pip` 安装：

   ```bash
   pip install -r requirements.txt
   ```

3. **运行项目**
   现在，你可以运行项目并生成 langchain 仓库的最新 release 报告。

   ```bash
   python main.py
   ```
