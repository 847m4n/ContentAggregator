from newspaper import Article
import nltk


def summarize_article(url):
    article = Article(url)

    article.download()
    article.parse()

    article.download('punkt')
    article.nlp()

    print()
    print("----------------------------------------------------------------------")
    print(f"The Article link: {url}")
    print("Author: " + str(article.authors))
    print("Publish Date: " + str(article.publish_date))
    print("Cover Picture: " + str(article.top_image))
    print()
    print("Article Summary: ")
    print(article.summary)
    print()
    print("Sentiment Analysis: ")

    return article.summary
