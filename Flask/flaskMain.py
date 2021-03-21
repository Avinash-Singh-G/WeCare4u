# from predict import PredictForm
from flask import Flask, render_template, redirect, url_for, request,session
from newsapi import NewsApiClient
from itsdangerous import URLSafeTimedSerializer, SignatureExpired
app = Flask(__name__)
app.config.from_pyfile('config.cfg')
import requests

from datetime import datetime
import pytz
# mail = Mail(app)
app.secret_key = 'weCare123'

s = URLSafeTimedSerializer('secret123')


@app.route('/')
def index():
    return render_template('index.html')


def fetch_keyword_news(your_keyword_list, date, apiKey):
    all_description = []
    all_url = []
    all_title = []
    for i in range(len(your_keyword_list)):
        url = ('http://newsapi.org/v2/everything?'
               'q=' + str(your_keyword_list[i]) + '&'
                                                  'from=' + str(date) + '&'
                                                                        'language=en&'
                                                                        'sortBy=popularity&'
                                                                        'apiKey=' + str(apiKey))
        response = requests.get(url).json()
        # response = json.loads(respons)
        article = response['articles']

        # description = response["description"]
        # url = response["url"]
        # title = response["title"]

        for k in range(len(article)):

            if k <= 2:
                all_description.append(article[i]['description'])
                all_url.append(article[i]['url'])
                all_title.append(article[i]['title'])

    return all_description, all_url, all_title

@app.route('/info')
def info():
    api = NewsApiClient(api_key='0c121bea533546759ad2551c94d28118')
    api.get_sources()
    api.get_everything(sources='bbc-news', q='women AND safety')


    apiKey_list = ['20d469827dbb4eb384d22490ea5df888', '75d16a33351a44969f3a5ac41eb7cf20',
                   '6496b9cb73c34054a8b58a3dee86c672',
                   '5e6b9203fe4247369e70351f0ab2b1b3', '3907a8165aec4be89b2e12f3a5ad541a',
                   '79bbb20ec53e4d1b85c2caca76402488',
                   '388eff313e1a4d399d55ebb19d4db4cd', 'a0936894b7904a03a4c35ca6627ebc33',
                   'c15a4b03480c4081bd3d184bc8559f23',
                   'c05beec776fa4b1fbcc46bdad8efa951', 'be98dcb51dd64998ad08a6dd2c5f9e80',
                   '376c9dfc704748279df3e6f30a751a1e',
                   '46660f56bd6e45f986fea91dc87b1fc1', '5dbf8944da394e4ca003b7fea5b736c5',
                   '31ba8f79f57d41c8b03d3334760154b3',
                   '723db6ceb2e8465daffa882be629d6fb', '1a88fcc99b0b41de902fcdbc45bd4a97',
                   '06d039549c914c78a46d2c0c137b7f7c',
                   '1b47a4f26fc949c4ad280f9bfb81cd5d']  # List of different API Keys

    a, b, c = fetch_keyword_news(
        ["women", "women empowerment", "menstural cycle", "periods", "girl power", "women in business", "health"],
        datetime.now(pytz.timezone('US/Eastern')).date(),
        apiKey_list[4])  # List which will contain all the latest news inputs

    print(a,b,c)
    arr = [a[0:3],b[0:3],c[0:3]]
    print(arr)
    # session['final'] = final



    return render_template('info.html',final=arr)

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    # you must tell the variable 'form' what you named the class, above
    # 'form' is the variable name used in this template: index.html
    # form = PredictForm(request.form)
    if request.method == "POST":
        # ***************** 
        CycleWithPeakorNot = request.form.get('CycleWithPeakorNot')


        # ***************** 

        print(request.form.get('email'))
    return render_template('predict.html')


if __name__ == '__main__':
    app.secret_key = 'secret123'
    app.run(debug=True)

