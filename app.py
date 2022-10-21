from flask import Flask, render_template
from fetch_db import get_unique_ids, get_codeparams_from_std_id, get_codeparams_from_time

app = Flask(__name__)
# conn = connect_db()


@app.route('/')
def index():
    kwargs = {}
    # unique_ids = set(get_users(conn))
    # ids = list(unique_ids)
    ids = get_unique_ids()
    kwargs['ids'] = ids
    return render_template('index.html', **kwargs)


@app.route('/student/<id>')
def student_data(id):
    kwargs = {}
    kwargs['id'] = id
    # kwargs['data'] = get_code_params(conn, id)
    code_params = get_codeparams_from_std_id(id)
    kwargs['data'] = code_params
    return render_template('student_data.html', **kwargs)


@app.route('/student/<id>/<time>')
def source(id, time):
    saved_at = time.replace('_', '/')
    kwargs = {}
    kwargs['id'] = id
    kwargs['time'] = saved_at
    kwargs['code'] = get_codeparams_from_time(saved_at)['code']
    return render_template('source.html', **kwargs)


if __name__ == '__main__':
    app.run(debug=True, port=8000)
