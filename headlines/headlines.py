from flask import Flask
import json
import feedparser
from flask import request

app = Flask(__name__)

@app.route("/")
def get_root():
    return_data = {"fail":"No data specified"}
    return json.dumps(return_data)

@app.route("/news/<publication>")
def get_news(publication=None):
    stories = []

    BBC_URL = 'http://feeds.bbci.co.uk/news/rss.xml'
    feed = feedparser.parse(BBC_URL)

    query = request.args.get("publication")
    print query

    for story_index in range(0,10):
        story = {}
        story['summary'] = feed['entries'][story_index].summary_detail.value
        story['title'] = feed['entries'][story_index].title
        story['link'] = feed['entries'][story_index].link
        stories.append(story)

    return json.dumps(stories)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
