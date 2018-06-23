from flask import Flask, make_response

app = Flask(__name__)
app.config.from_object('config')
print(app.config['DEBUG'])
headers = {
    'content-type': 'application/json',
    'location': 'http://www.bing.com'
}

@app.route('/hello')
def hello():
    #response = make_response('<html></html>', 301)
    #response.headers = headers
    return '<html></html>', 301, headers

def helloo():
    return 'Hello Clown'

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=app.config['DEBUG'])