from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)


@app.route('/')  # home的路徑
def hello_word():
    return 'Hello World!'

@app.route('/index')
def index():  # main
    return render_template('base.html')

@app.route('/input_customer', methods=['GET','POST'])
def input_customer():  # put application
    return render_template('input_customer.html')

@app.route('/result', methods=['GET','POST'])
def result():  # put application
    if request.method == 'POST':
        member_code = request.values["Name"]
    return render_template('result.html',member_code=member_code)

if __name__ == '__main__':
    app.run()
