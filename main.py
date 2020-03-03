from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Tyler'}
    items = [
        {'name':'Apple','price':2.34},
        {'name':'Orange','price':4.88},
        {'name':'Grape','price':2.44}
    ]
    return render_template('index.html', title='Home', user=user, items=items)


if __name__ == '__main__':
   app.run()