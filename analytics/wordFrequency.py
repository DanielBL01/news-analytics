import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist

def filterText(text):
    """Return the array of words from removing punctuation and stop words from text."""
    # Initialize array object to be returned
    response = []
    # Remove all punctuation 
    tokenizer = nltk.RegexpTokenizer(r"\w+")
    words_without_punc = tokenizer.tokenize(text)

    # Remove all stop words
    stop_words = stopwords.words('english')
    for word in words_without_punc:
        if word.lower() not in stop_words:
            response.append(word.lower())

    # Return response object
    return response

def getWordFrequency(text):
    """Return arrays of keys/values of words with counts over 3, total number of unique words and most common word."""
    words = filterText(text)
    # Create a frequency dictionary
    fdist = FreqDist()
    for word in words:
        fdist[word] += 1

    filteredKeys = []
    filteredValues = []

    for key, value in fdist.items():
        if value > 1:
            filteredKeys.append(key)
            filteredValues.append(value)

    return filteredKeys, filteredValues, fdist.B(), fdist.max()