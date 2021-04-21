import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist

def filterText(text):
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
    words = filterText(text)
    # Create a frequency dictionary
    fdist = FreqDist()
    for word in words:
        fdist[word] += 1

    filteredKeys = []
    filteredValues = []

    for key, value in fdist.items():
        if value > 3:
            filteredKeys.append(key)
            filteredValues.append(value)

    # Return frequency dictionary and total number of outcomes where count > 0 and most common word
    return filteredKeys, filteredValues, fdist.B(), fdist.max()