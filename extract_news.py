import newspaper

# Please note : It seems that if a link is used and exectued more than once consecutively
# The website somehow blocks the link and an empty list gets printed.

url_list = []


def article_links():
    # Here we ask the user to choose from four different news organizations
    name = input("Please enter your name : ")
    s = int(input("Please choose the news agency you'd like the articles from :"
                  "\n Press 1 for CNN"
                  "\n Press 2 for New York Times"
                  "\n Press 3 for Fox13now"
                  "\n press 4 for BBC (UK)"
                  "\n Enter Code : "))

    if s == 1:
        news_paper = newspaper.build('https://edition.cnn.com/')
        print("You picked CNN")
    elif s == 2:
        news_paper = newspaper.build('https://www.nytimes.com/international/')
        print("You picked New York Times")
    elif s == 3:
        news_paper = newspaper.build('https://www.fox13now.com/')
        print("You picked Fox13now")
    elif s == 4:
        news_paper = newspaper.build('https://www.bbc.co.uk/')
        print("You picked BBC (UK) ")
    else:
        print("Wrong input!")

    # To give the program a more organic feel
    print(f"Hey {name}! Apologies for the wait time...")
    print("extracting the article hyperlinks...")

    # NOTE : THIS WORKS WELL ONLY FOR AMERICAN PUBLISHERS
    # Now we will print all the url's from the selected website and produce all the titles of the links
    for article in news_paper.articles:
        url_list.append(article.url)
