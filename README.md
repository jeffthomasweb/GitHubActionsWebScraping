This project uses the free tier of GitHub Actions to run a webscraper. The YML files controling the scraping are located under .github/workflows. The parsed content is saved into output.txt and nyt.txt. 

One of the YML files is pasted below as an example.

```yml
name: Web scrape 

on:
  workflow_dispatch:
  schedule:
    - cron:  '* */12 * * *'
jobs:
  scheduled:
    runs-on: ubuntu-latest
    steps:
    - name: Check out this repo
      uses: actions/checkout@v3
      with:
        fetch-depth: 0
    - uses: actions/setup-python@v4
      with:
        python-version: '3.11'
        cache: 'pip'
    - run: pip install -r requirements.txt
    - name: Fetch latest data
      run: python3 scrape.py
    - name: Commit and push if it changed
      run: |-
        git config user.name "Automated"
        git config user.email "actions@users.noreply.github.com"
        git add -A
        timestamp=$(date -u)
        git commit -m "Latest data: ${timestamp}" || exit 0
        git push
```
