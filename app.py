from flask import Flask, render_template
from db import get_users, get_code_params, get_source_code

app = Flask(__name__)
title = "Stumble Notifier"


@app.route('/')
def index():
    kwargs = {}
    unique_ids = set(get_users())
    ids = list(unique_ids)
    kwargs['title'] = title
    kwargs['ids'] = ids
    return render_template('index.html', **kwargs)


@app.route('/student/<id>')
def student_data(id):
    kwargs = {}
    kwargs['title'] = title
    kwargs['id'] = id
    kwargs['data'] = get_code_params(id)
    return render_template('student_data.html', **kwargs)


@app.route('/student/<id>/<time>')
def source(id, time):
    kwargs = {}
    kwargs['title'] = title
    kwargs['id'] = id
    kwargs['time'] = time
    kwargs['code'] = get_source_code(id, time)
    return render_template('source.html', **kwargs)


if __name__ == '__main__':
    app.run(debug=True, port=8000)
