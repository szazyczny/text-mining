# Sarah Zazyczny Text Mining 

from imdbpie import Imdb
from nltk import * 
from nltk.sentiment.vader import SentimentIntensityAnalyzer

imdb = Imdb()
#print(imdb.search_for_title("Clueless")[:11])
reviews = imdb.get_title_user_reviews("tt0112697")

# import pprint
# pprint.pprint(reviews)

# reviewA
reviewA = (reviews['reviews'][0]['reviewText'])
Ascore = SentimentIntensityAnalyzer().polarity_scores(reviewA)

# test any review within [:11] by changing the [0]
review = (reviews['reviews'][8]['reviewText'])
score = SentimentIntensityAnalyzer().polarity_scores(review)


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

tokensA = text_process(reviewA)
fdistA = FreqDist(tokensA) 

tokens = text_process(review)
fdist = FreqDist(tokens) 

# ideas for testing
# https://www.nltk.org/book/ch01.html

def main():
    # type(reviews) # dictionary
    # print(reviews.keys())
    # print(reviews.values())

    # print(reviews['reviews'][0]['author']['displayName'])
    # print(reviews['reviews'][0]['reviewText'])

    # print(reviewA)
    # print(Ascore)
    # print(len(reviewA))
    # print(sorted(set(reviewA)))
    # print(reviewA.count("Cher"))

    # print(review)
    # print(score)
    # print(len(review))
    # print(sorted(set(review)))
    # print(review.count("Cher"))

    # print(tokensA)
    # print(fdistA)
    # print(fdistA.most_common(10))

    # print(tokens)
    # print(fdist)
    # print(fdist.most_common(10))

    

if __name__ == '__main__':
    main()