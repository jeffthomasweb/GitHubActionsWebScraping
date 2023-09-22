This webscraper runs twice a day using the free tier of GitHub Actions. It will get the text from the 3 RSS feeds and place the parsed 
text into a file called output.txt. 

There's another scraper in this project that scrapes the New York Times website on the weekends.

A sample YML file for the scraping actions is below.

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
