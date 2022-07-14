from flask import Flask, render_template

app = Flask(__name__)
title = "Stumble Notifier"


@app.route('/')
def index():
    ids = [1, 2, 3, 4, 5, 6]
    return render_template('index.html', title=title, ids=ids)


@app.route('/student/<id>')
def student_data(id):
    data = [
            {"time": "10:10", "sloc": 4, "ed": 2},
            {"time": "10:12", "sloc": 7, "ed": 3},
            {"time": "10:20", "sloc": 4, "ed": 5}
    ]
    return render_template('student_data.html', title=title, id=id, data=data)


@app.route('/student/<id>/<time>')
def source(id, time):
    time_exp = time.replace('_', ':')
    return render_template('source.html', title=title, id=id, time=time_exp)


if __name__ == '__main__':
    app.run(debug=True, port=8000)
