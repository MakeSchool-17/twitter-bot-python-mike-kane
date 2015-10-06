import requests
import codecs

pages = []
for line in open('pages.txt', 'r'):
    pages.append(line.strip('\n'))

DIFFBOT_API_URL = 'http://api.diffbot.com/v3/article'
DIFFBOT_DEV_TOKEN = 'd3eb4b8e0748599261893959014a034d'


def get_article(article_url):
    # set params for API request
    params = {"token": DIFFBOT_DEV_TOKEN,
              "url": article_url,
              "discussion": False}

    res = requests.get(DIFFBOT_API_URL, params)  # calling Diffbot API
    res_obj = res.json()['objects'][0]
    return res_obj['text']

if __name__ == '__main__':
    import sys
    urls_file = open(sys.argv[1])
    with codecs.open('corpus.txt', 'w', encoding='utf-8') as output_file:

        corpus = ''
        fileCount = 0
        for line in urls_file:
            url = line.strip()
            article = get_article(url)
            corpus += article
            fileCount += 1
            print('file #{}, {} successfully written'.format(fileCount, url))

        output_file.write(corpus)
        print("Corpus successfully written to corpus.txt")
