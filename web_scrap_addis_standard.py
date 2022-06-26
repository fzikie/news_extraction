from bs4 import BeautifulSoup
import requests
import json
from lxml.builder import unicode


## Function 1: Extract years of news from the Addis Standard News Article wesite: https://addisstandard.com/

def extract_all_news():
    news_to_write = open('ethiopia_addis_standard_social_affairs.txt', 'a')
    url = 'https://addisstandard.com/social-affairs/page/'
    index = 1
    eth_standard_social_news = []
    while True:
        if index == 1:
            url = 'https://addisstandard.com/social-affairs'
        url_text = requests.get(url).text
        soup = BeautifulSoup(url_text, 'lxml')
        news_pointers = soup.find_all('h3', class_='eltdf-pt-six-title')
        # print(social_news)
        index += 1
        url = 'https://addisstandard.com/social-affairs/page/' + str(index) + '/'
        if not news_pointers:
            break
        this_edition = []
        for pointer in news_pointers:
            news_url = pointer.a['href']
            news_url_text = requests.get(news_url).text
            news_soup = BeautifulSoup(news_url_text, 'lxml')
            news = news_soup.find('div', class_='eltdf-content')
            news_date = news.find('div', itemprop='dateCreated')
            date = news_date.a.getText().strip()
            news_title = news.find('div', class_='eltdf-title-subtitle-holder')
            news_title_inner = news_title.find('div', class_='eltdf-title-subtitle-holder-inner')
            header = news_title.h1.getText().strip()
            social_news = news.find_all('h3', class_='eltdf-pt-six-title')
            # print(f'Date: {date}')
            # print(f'Header: {header}')
            news_paragraphs = []
            for paragraph in news_soup.find_all('p'):
                if paragraph.text.startswith('©') or paragraph.text.startswith(
                        'Follow Us') or paragraph.text.startswith('Sorry, the comment form is closed at this time'):
                    pass
                else:
                    try:
                        news_paragraphs.append([paragraph.text])
                    except Exception:
                        pass
            this_edition.append({'Date': date, 'Header': header, 'news_paragraphs': news_paragraphs})

        eth_standard_social_news.append(this_edition)

    with open('ethiopia_addis_standard_social_affairs.txt', 'w') as file:
        for news_edition in eth_standard_social_news:
            try:
                file.write('%s\n' % news_edition)
            except Exception:
                pass
        file.close()


if __name__==__main__:
  extract_all_news()


# # Function 2: Extract related words and phrases to poverty
# def get_poverty_describing_words():
#     url = 'https://relatedwords.org/relatedto/poverty'
#     myurl = requests.get(url).text
#     # print(myurl)
#     soup = BeautifulSoup(myurl, 'lxml')
#
#     data = json.loads(soup.find('script', type="text/json").text)
#     data_terms = data['terms']
#     for term in data_terms:
#         print(term['word'])


