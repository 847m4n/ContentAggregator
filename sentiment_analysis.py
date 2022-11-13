from textblob import TextBlob


# Read second
# Calculates the average of the respective data to give a single value
def calculate_average(data):
    if len(data) == 0:  # Added this line because of the zero division error
        return 0
    else:
        return sum(data) / len(data)


# Read third
# We get a single number from the calculate_average function.
# We check what range this number exists in and assign the polarity or subjectivity respectively
def calculate_sentiment(sentiment, category):
    sentiment_polarity = ""
    sentiment_subjectivity = ""
    if category == "polarity":
        if sentiment > 0.75:
            sentiment_polarity = "extremely positive"
        elif sentiment > 0.5:
            sentiment_polarity = "significantly positive"
        elif sentiment > 0.3:
            sentiment_polarity = "fairly positive"
        elif sentiment > 0.1:
            sentiment_polarity = "slightly positive"
        elif sentiment == 0:
            sentiment_polarity = "neutral"
        elif sentiment < -0.1:
            sentiment_polarity = "slightly negative"
        elif sentiment < -0.3:
            sentiment_polarity = "fairly negative"
        elif sentiment < -0.5:
            sentiment_polarity = "significantly negative"
        elif sentiment < -0.75:
            sentiment_polarity = "extremely negative"
        return sentiment_polarity
    elif category == "subjectivity":
        if sentiment > 0.75:
            sentiment_subjectivity = "extremely subjective"
        elif sentiment > 0.5:
            sentiment_subjectivity = "fairly subjective"
        elif sentiment > 0.3:
            sentiment_subjectivity = "fairly objective"
        elif sentiment > 0.1:
            sentiment_subjectivity = "Extremely objective"
        return sentiment_subjectivity
    else:
        print("Invalid Input.")


# Read first
def find_sentiment(news_story):
    news = TextBlob(news_story)
    sentiments = []
    for sentence in news.sentences:
        sentiment = sentence.sentiment  # Checks each and every sentence individually
        for metric in sentiment:
            sentiments.append(metric)  # Adds the sentiment of all the sentences to a list

    # The odd indexes are subjectivity and the even indexes are polarity so we now segregate them
    polarity_data = []
    subjectivity_data = []
    for i in range(len(sentiments)):
        if i % 2 == 0:
            polarity_data.append(sentiments[i])
        else:
            subjectivity_data.append(sentiments[i])

    polarity_score = calculate_average(polarity_data)  # Average score of the polarity
    subjectivity_score = calculate_average(subjectivity_data)  # Average score of the subjectivity

    print("Polarity : " + str(calculate_sentiment(polarity_score, "polarity")))
    print("Subjectivity : " + str(calculate_sentiment(subjectivity_score, "subjectivity")))
