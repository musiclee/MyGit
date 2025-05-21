"""
Search Google for the keyword "\u76d2\u9a6c" and summarize the results using an LLM.

Requirements:
- requests
- beautifulsoup4
- openai

Set the environment variable OPENAI_API_KEY for summarization.
Note: This script requires network access which may not be available
in all environments.
"""

import os
import requests
from bs4 import BeautifulSoup
import openai


def fetch_results(query: str) -> str:
    """Fetch the HTML content of Google search results."""
    url = "https://www.google.com/search"
    params = {"q": query, "hl": "zh-CN"}
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, params=params, headers=headers)
    response.raise_for_status()
    return response.text


def parse_results(html: str) -> str:
    """Parse titles and snippets from Google search results."""
    soup = BeautifulSoup(html, "html.parser")
    collected = []
    for g in soup.select("div.g"):
        title = g.select_one("h3")
        snippet = g.select_one("span.aCOpRe") or g.select_one("div.IsZvec")
        if title and snippet:
            collected.append(f"{title.get_text(strip=True)} - {snippet.get_text(strip=True)}")
    return "\n".join(collected)


def summarize(text: str) -> str:
    """Use OpenAI API to summarize text."""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY environment variable not set")
    openai.api_key = api_key
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "\u8bf7\u7b80\u8981\u6458\u8981\u4ee5\u4e0b\u641c\u7d22\u7ed3\u679c"},
            {"role": "user", "content": text},
        ],
        max_tokens=200,
    )
    return response.choices[0].message["content"].strip()


def main() -> None:
    query = "\u76d2\u9a6c"  # "\u76d2\u9a6c" in Chinese
    html = fetch_results(query)
    results_text = parse_results(html)
    print("Raw results:\n", results_text)
    summary = summarize(results_text)
    print("\nSummary:\n", summary)


if __name__ == "__main__":
    main()
