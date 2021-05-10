import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist

def filterText(text):
    """Return the array of words from removing punctuation and stop words from text."""

    response = []
    tokenizer = nltk.RegexpTokenizer(r"\w+")
    words_without_punc = tokenizer.tokenize(text)
    stop_words = stopwords.words('english')
    for word in words_without_punc:
        if word.lower() not in stop_words:
            response.append(word.lower())

    return response

def getWordFrequency(text):
    """Return arrays of keys/values of words with counts over 3, total number of unique words and most common word."""
    
    words = filterText(text)
    fdist = FreqDist()
    for word in words:
        fdist[word] += 1
    filteredKeys = []
    filteredValues = []
    for key, value in fdist.items():
        if value >= 3:
            filteredKeys.append(key)
            filteredValues.append(value)

    return filteredKeys, filteredValues, fdist.B(), fdist.max()