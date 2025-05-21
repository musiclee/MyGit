import os
import requests
from bs4 import BeautifulSoup
import openai


def google_search(query, num_results=5):
    """Fetch results from Google Search."""
    url = "https://www.google.com/search"
    params = {"q": query, "num": num_results, "hl": "zh-CN"}
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, params=params, headers=headers)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    results = []
    for g in soup.select("div.g"):
        title_elem = g.find("h3")
        snippet_elem = g.find("span", class_="aCOpRe")
        if title_elem and snippet_elem:
            results.append({
                "title": title_elem.get_text(strip=True),
                "snippet": snippet_elem.get_text(strip=True)
            })
        if len(results) >= num_results:
            break
    return results


def summarize_results(results):
    """Send search snippets to OpenAI for summarization."""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY environment variable not set")
    openai.api_key = api_key
    content = "\n\n".join(f"Title: {r['title']}\nSnippet: {r['snippet']}" for r in results)
    prompt = (
        "请根据以下 Google 搜索结果，总结与关键字 '盒马' 相关的主要信息：\n\n" + content
    )
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
    )
    return response.choices[0].message.content.strip()


def main():
    query = "盒马"
    print(f"Searching Google for '{query}'...")
    results = google_search(query)
    for idx, r in enumerate(results, start=1):
        print(f"[{idx}] {r['title']} - {r['snippet']}")
    print("\nGenerating summary...\n")
    summary = summarize_results(results)
    print(summary)


if __name__ == "__main__":
    main()
