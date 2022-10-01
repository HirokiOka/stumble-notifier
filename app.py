from flask import Flask, render_template
from code_db import connect_db, get_users, get_code_params, get_source_code
from heart_data import get_heart_data

app = Flask(__name__)
conn = connect_db()


@app.route('/')
def index():
    kwargs = {}
    unique_ids = set(get_users(conn))
    ids = list(unique_ids)
    kwargs['ids'] = ids
    return render_template('index.html', **kwargs)


@app.route('/student/<id>')
def student_data(id):
    kwargs = {}
    kwargs['id'] = id
    kwargs['data'] = get_code_params(conn, id)
    return render_template('student_data.html', **kwargs)


@app.route('/student/<id>/<time>')
def source(id, time):
    kwargs = {}
    kwargs['id'] = id
    kwargs['time'] = time
    kwargs['code'] = get_source_code(conn, id, time)
    return render_template('source.html', **kwargs)


if __name__ == '__main__':
    app.run(debug=True, port=8000)
