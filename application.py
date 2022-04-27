from flask import Flask, render_template, url_for, send_file, request, flash, redirect
import requests



application = Flask(__name__)


@application.route("/", methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        data = request.form.getlist("data_input")
        data = data[0]

        url = "https://kko9j4ibhb.execute-api.eu-west-3.amazonaws.com/Prod/hello?text="+ data

        response = requests.get(url)
        keywords = response.json()['keywords']

        return render_template('home.html', data=keywords)
    return render_template('layout.html')


@application.route("/home", methods=['POST'])
def home():
        return render_template('home.html')


if __name__ == '__main__':
    application.run(debug=True)
