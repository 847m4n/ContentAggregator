# This project contains different modules
# The first one is called extract, it extracts all the links from a news website
# The second one is called summarize and it creates a summary of an articleby using its link
# the ones above use the newspaper3k module
# the last one is called sentiment_analysis and it gives the polarity and subjectivity of the news
# polarity quantifies whether a statement is positive or negative
# subjectivity refers to personal opinion, emotion or judgement
# the package used for the last one is called textblob

from extract_news import *
from summarizw import *
from sentiment_analysis import *

print("welcome to the my news scraper, it's called 'Times of 0 and 1'"
      "\nShortly you will be provided all sorts of news from 'The NewYorkTimes"
      "\nYou will also be told whether the news is fake or not and the extent of the writers bias")

print()
article_links()  # Calling the link generator module

for url in url_list:  # Iterating over all the url in the url_list
    summary = summarize_article(url)  # calling the summary module
    find_sentiment(summary)  # calling the sentiment module
    print()
    print("--------------------------------------XXXXX-------------------------------------")
