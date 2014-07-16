from flask import Flask, jsonify
import requests
import json
import ast
import config

app = Flask(__name__)

@app.route('/', methods=['POST'])
def yo_all():
    yo_all_request = requests.post("http://api.justyo.co/yoall/",
                                   data={'api_token': config.YO_API_TOKEN})
    if 'result' in yo_all_request.json() and yo_all_request.json()['result'] == 'OK':
        return json.dumps({'text': 'Yo sent to all!'})
    else:
        return json.dumps({'text': 'Error sending Yo. API may be down...'})

@app.route('/count', methods=['GET'])
def get_count_subscribers():
    get_count_request = requests.get("http://api.justyo.co/subscribers_count/",
                                     params={'api_token': config.YO_API_TOKEN})
    result = get_count_request.text.encode('utf-8')
    result_dict = ast.literal_eval(result)
    return jsonify(result_dict)

if __name__ == '__main__':
    app.run()
