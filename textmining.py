# Sarah Zazyczny Text Mining 

from imdbpie import Imdb
from nltk import * 
from nltk.sentiment.vader import SentimentIntensityAnalyzer

imdb = Imdb()
# print(imdb.search_for_title("Clueless")[0])
reviews = imdb.get_title_user_reviews("tt0112697")

import pprint
# pprint.pprint(reviews)

# scores for reviewA, reviewB, reviewC
reviewA = (reviews['reviews'][0]['reviewText'])
Ascore = SentimentIntensityAnalyzer().polarity_scores(reviewA)

reviewB = (reviews['reviews'][1]['reviewText'])
Bscore = SentimentIntensityAnalyzer().polarity_scores(reviewB)

reviewC = (reviews['reviews'][2]['reviewText'])
Cscore = SentimentIntensityAnalyzer().polarity_scores(reviewC)

# test any review within by changing the [0]
reviewtest = (reviews['reviews'][0]['reviewText'])
scoretest = SentimentIntensityAnalyzer().polarity_scores(reviewtest)

# SIMPLIFIED WITH FUNCTION
# function to print movie review sentiment score
def review_sentiment_score(n):
    """
    Generates sentiment analysis score based on selected review.
    Input 'n' = index number of movie review (order of reviews on imdb)
    """
    review = (reviews['reviews'][n]['reviewText'])
    score = SentimentIntensityAnalyzer().polarity_scores(review)
    return score


# To tokenize into list of words
#https://medium.com/tensorist/classifying-yelp-reviews-using-nltk-and-scikit-learn-c58e71e962d9
import nltk
from nltk.corpus import stopwords
import string

def text_process(text):
    '''
    Takes in a string of text, then performs the following:
    1. Remove all punctuation
    2. Remove all stopwords
    3. Return the cleaned text as a list of words
    '''
    nopunc = [char for char in text if char not in string.punctuation]
    nopunc = ''.join(nopunc)
    
    return [word for word in nopunc.split() if word.lower() not in stopwords.words('english')]

# tokems for reviewA, reviewB, reviewC
tokensA = text_process(reviewA)
fdistA = FreqDist(tokensA) 

tokensB = text_process(reviewB)
fdistB = FreqDist(tokensB) 

tokensC = text_process(reviewC)
fdistC = FreqDist(tokensC) 

# tokenize any review within by changing the [0] in the prior statement for reviewtest
tokenstest = text_process(reviewtest)
fdisttest = FreqDist(tokenstest) 

# SIMPLIFIED WITH FUNCTION
# function to print frequency distribution of words
def freqdist_tokens(n):
    """
    Generates frequency distribution of tokenized words in movie review.
    Input 'n' = index number of movie review (order of reviews on imdb)
    """
    review = (reviews['reviews'][n]['reviewText'])
    tokens = (text_process((review)))
    # print(tokens)
    fdist = FreqDist(tokens)
    return fdist

# ideas for testing
# https://www.nltk.org/book/ch01.html

def main():
    # type(reviews) # dictionary
    # print(reviews.keys())
    # print(reviews.values())

    # print(reviews['reviews'][0]['author']['displayName'])
    # print(reviews['reviews'][0]['reviewText'])

    #print(reviewA)
    # print(Ascore)
    # print(len(reviewA))
    # print(reviewA.count("Cher"))

    #print(reviewB)
    # print(Bscore)
    # print(len(reviewB))
    # print(reviewB.count("Cher"))

    #print(reviewC)
    # print(Cscore)
    # print(len(reviewC))
    # print(reviewC.count("Cher"))

    # print(reviewtest)
    # print(scoretest)
    # print(len(reviewtest))
    # print(reviewtest.count("Cher"))

    # print(review_sentiment_score(0))
    # print(review_sentiment_score(1))
    # print(review_sentiment_score(2))

    # print(tokensA)
    # print(fdistA)
    # print(fdistA.most_common(10))
    
    # print(tokensB)
    # print(fdistB)
    # print(fdistB.most_common(10))

    # print(tokensC)
    # print(fdistC)
    # print(fdistC.most_common(10))

    # print(tokenstest)
    # print(fdisttest)
    # print(fdisttest.most_common(10))

    # print(freqdist_tokens(0))
    # print(freqdist_tokens(1))
    # print(freqdist_tokens(2))

    

if __name__ == '__main__':
    main()