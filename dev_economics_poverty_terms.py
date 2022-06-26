
# Function 2: Extract related words and phrases to poverty

def get_poverty_describing_words():
    url = 'https://relatedwords.org/relatedto/poverty'
    myurl = requests.get(url).text
    # print(myurl)
    soup = BeautifulSoup(myurl, 'lxml')

    data = json.loads(soup.find('script', type="text/json").text)
    data_terms = data['terms']
    for term in data_terms:
        print(term['word'])
