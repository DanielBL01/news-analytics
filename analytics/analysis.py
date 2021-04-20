from newspaper import Article

def getAnalysisResults(url):
    """Return the authors, publish date, text body, keywords and summary of article."""

    article = Article(url)
    article.download()
    article.parse()
    article.nlp()

    return article.authors, article.publish_date, article.text, article.keywords, article.summary