# 搜索分析脚本

该仓库包含一个简单的示例脚本 `search_analyze.py`，用于在 Google 搜索 "盒马" 并利用 OpenAI API 总结搜索结果。

## 依赖

- Python 3
- `requests`
- `beautifulsoup4`
- `openai`

可通过以下命令安装：

```bash
pip install requests beautifulsoup4 openai
```

## 使用方法

1. 在终端设置环境变量 `OPENAI_API_KEY` 为你的 OpenAI API Key。
2. 运行脚本：

```bash
python3 search_analyze.py
```

脚本会打印针对 "盒马" 关键字的搜索结果摘要。

