from flask import Flask, render_template
# import news_api module
from newsapi import NewsApiClient

app = Flask(__name__)


# create a route function to render the HTML template
@app.route('/')
def home():
    # enter client id and api key for authorization
    newsapi = NewsApiClient(api_key='227c1a84dded40be8803b0bf374fb024')

    # for top headlines of news, we will code:
    top_headlines = newsapi.get_top_headlines(sources='bbc-news')
    # sources is meant by, where the news comes into your app by api

    # for all main articles we will code,
    # all_articles = newsapi.get_everything(sources='bbc-news')

    # fetch all the articles of top headlines
    t_articles = top_headlines['articles']
    # a_articles = all_articles[' ']

    # make a lisr of contents to store the values of that list
    news = []
    desc = []
    img = []
    p_date = []
    url = []

    # fetch all the content from the json file
    for i in range(len(t_articles)):
        main_article = t_articles[i]

        # at last append all the contents to each of the list
        news.append(main_article['title'])
        desc.append(main_article['description'])
        img.append(main_article['urlToImage'])
        p_date.append(main_article['publishedAt'])
        url.append(main_article['url'])
        # make a zip to find the contents directly and shrotly
        contents = zip(news, desc, img, p_date, url)

    return render_template('home.html', contents=contents)


if __name__ == '__main__':
    app.run(debug=True)
