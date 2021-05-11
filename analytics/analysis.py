from newspaper import Article

def getAnalysisResults(url):
    article = Article(url)
    article.download()
    article.parse()
    article.nlp()

    return article.text, article.summary