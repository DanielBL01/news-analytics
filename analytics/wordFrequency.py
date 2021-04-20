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
    
    # Return frequency dictionary, total number of values with counts > 0 and sample with greatest number of counts
    return fdist, fdist.B(), fdist.max()