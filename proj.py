from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/clothes/')
def clothes():
    context = {'title': 'Cтраница с одеждой'}
    return render_template('clothes.html', **context)


@app.route('/shoes/')
def shoes():
    context = {'title': 'Cтраница с обувью'}
    return render_template('shoes.html', **context)


@app.route('/jacket/')
def jacket():
    context = {'title': 'Cтраница с курткой'}
    return render_template('jacket.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
