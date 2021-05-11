import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist

def filterText(text):
    response = []
    tokenizer = nltk.RegexpTokenizer(r"\w+")
    words_without_punc = tokenizer.tokenize(text)
    stop_words = stopwords.words('english')
    for word in words_without_punc:
        if word.lower() not in stop_words:
            response.append(word.lower())

    return response

def getWordFrequency(text):
    words = filterText(text)
    fdist = FreqDist()
    for word in words:
        fdist[word] += 1
    filteredKeys = []
    for key, value in fdist.items():
        if value >= 3:
            filteredKeys.append(key)

    return filteredKeys, fdist.max()