# MyGit Repository

This repository contains a simple HTML welcome page and a Python script to analyze Google search results for the keyword "盒马".

## Files

- `index.html` - A minimal HTML5 welcome page.
- `search_analyze.py` - Fetches Google search results for "盒马" and summarizes them using the OpenAI API. Requires `requests`, `beautifulsoup4`, and `openai` packages.

## Usage

1. Install dependencies:
   ```bash
   pip install requests beautifulsoup4 openai
   ```
2. Set the `OPENAI_API_KEY` environment variable with your OpenAI API key.
3. Run the script:
   ```bash
   python3 search_analyze.py
   ```

Due to restrictions in this environment, network access may be disabled, so the script may not run successfully here. Use your own environment with internet access.
