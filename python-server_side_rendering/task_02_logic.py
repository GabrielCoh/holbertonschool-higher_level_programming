from flask import Flask, render_template
import json


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def home():
    return render_template('about.html')


@app.route('/contract')
def contract():
    return render_template('contact.html')

@app.route('/items')
def items():
    with open('items.json') as file:
        data = json.load(file)
    items_list = data.get('items', [])
    return render_template('items.html', list=list)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
