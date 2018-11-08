
from imdbpie import Imdb

imdb = Imdb()
print(imdb.search_for_title("Clueless")[0])
reviews = imdb.get_title_user_reviews("tt0112697")

# import pprint
# pprint.pprint(reviews)

print(reviews['reviews'][0]['author']['displayName'])
print(reviews['reviews'][0]['reviewText'])




from nltk.sentiment.vader import SentimentIntensityAnalyzer

# sentence = 'Software Design is my favorite class because learning Python is so cool!'
# score = SentimentIntensityAnalyzer().polarity_scores(sentence)
# print(score)

reviewscore = SentimentIntensityAnalyzer().polarity_scores(reviews)
print(reviewscore)