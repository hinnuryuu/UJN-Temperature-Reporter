import datetime

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def monitor():
    with open('log.txt', 'r', encoding='utf-8') as f:
        user_information = f.readlines()
    is_latest = True
    if datetime.datetime.now().hour < 18:
        is_latest = False
    return render_template("index.html", information=user_information, latest=is_latest)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
