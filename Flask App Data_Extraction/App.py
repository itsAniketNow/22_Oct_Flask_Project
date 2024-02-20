from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    # Fetch Chuck Norris joke from the API
    response = requests.get('https://api.chucknorris.io/jokes/random')

    if response.status_code == 200:
        data = response.json()
        joke = data['value']
        return render_template('index.html', joke=joke)
    else:
        return 'Error fetching Chuck Norris joke'

if __name__ == '__main__':
    app.run(debug=True)
