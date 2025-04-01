import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {
    'User-Agent': 'Mozilla/5.0'
}

def google_scholar_search(query, year_from, num_results=50):
    base_url = 'https://scholar.google.com/scholar'
    params = {
        'q': query,
        'as_ylo': year_from,
        'hl': 'ko',
        'num': num_results
    }
    response = requests.get(base_url, headers=headers, params=params)
    return response

def parse_papers(html):
    soup = BeautifulSoup(html, 'html.parser')
    results = []
    for entry in soup.select('.gs_ri'):
        title = entry.select_one('.gs_rt').text
        abstract = entry.select_one('.gs_rs').text
        results.append({'제목': title, '초록': abstract})
    return results

query = '"AI 서비스" "기업 이미지" "감성분석" OR "sentiment analysis"'
year_from = 2020
num_results = 50

response = google_scholar_search(query, year_from, num_results)
papers = parse_papers(response.text)

df = pd.DataFrame(papers)
df.to_excel('AI_Service_Corporate_Image_Papers.xlsx', index=False)
