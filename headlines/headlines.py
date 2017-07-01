from flask import Flask
import json

app = Flask(__name__)

@app.route("/")
def get_root():
    return_data = {"fail":"No data specified"}
    return json.dumps(return_data)

@app.route("/news/<publication>")
def get_news(publication=None):
    stories = []
    stories.append({'headline':'Bobcats attack local nursery, leave gore in their wake.'})
    stories.append({'headline':'White House runs out of plastic cutlery.'})
    stories.append({'headline':'NASCAR canceled for reruns of House.'})
    stories.append({'headline':'NASA discovery leads to finding more than $5 worth of coins under employee desks.'})

    return json.dumps(stories)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
