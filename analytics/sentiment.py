import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

def sentimentAnalysis(text):
    net_sentiment = 0
    num_sent = 0
    sia = SentimentIntensityAnalyzer()
    sent_text = nltk.sent_tokenize(text)
    for sentence in sent_text:
        num_sent +=1
        compound = sia.polarity_scores(sentence)['compound']
        print(compound)
        net_sentiment += compound
    
    net_sentiment = net_sentiment / num_sent
    if net_sentiment == 0:
        return 'NEUTRAL'
    elif net_sentiment > 0 and net_sentiment < 0.5:
        return 'POSITIVE'
    elif net_sentiment > 0 and net_sentiment >= 0.5:
        return 'HIGHLY POSITIVE'
    elif net_sentiment < 0 and net_sentiment > -0.5:
        return 'NEGATIVE'
    else:
        return 'HIGHLY NEGATIVE'