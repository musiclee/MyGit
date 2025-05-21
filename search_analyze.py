import os
import requests
from bs4 import BeautifulSoup
import openai


def fetch_google_results(query, num_results=5):
    """Fetch Google search results."""
    url = "https://www.google.com/search"
    params = {"q": query, "hl": "zh-CN"}
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, params=params, headers=headers)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    results = []
    for item in soup.select('div.g')[:num_results]:
        title = item.find('h3')
        snippet = item.find('span', class_='aCOpRe')
        if title and snippet:
            results.append({
                "title": title.get_text(strip=True),
                "snippet": snippet.get_text(strip=True)
            })
    return results


def summarize_results(results):
    """Summarize search results using OpenAI."""
    openai.api_key = os.getenv("OPENAI_API_KEY")
    if not openai.api_key:
        raise RuntimeError("OPENAI_API_KEY environment variable not set")
    prompt = "\n".join(f"标题: {r['title']}\n摘要: {r['snippet']}" for r in results)
    prompt = (
        "请根据以下搜索结果总结有关'盒马'的主要信息，给出简要概述：\n" + prompt
    )
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5,
        max_tokens=300,
    )
    return completion.choices[0].message["content"].strip()


def main():
    results = fetch_google_results("盒马")
    summary = summarize_results(results)
    print("搜索摘要:\n")
    print(summary)


if __name__ == "__main__":
    main()
