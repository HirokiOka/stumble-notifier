from flask import Flask, render_template
from fetch_db import get_predictions_from_std_id, get_unique_ids, get_codeparams_from_std_id, get_codeparams_from_time

app = Flask(__name__)
# conn = connect_db()


@app.route('/')
def index():
    kwargs = {}
    ids = ["test", "2041201h", "2070877H", "2110645H", "2120823h", "2141064h"]
    ids.sort()
    kwargs['ids'] = ids
    kwargs['code_pred'] = []
    kwargs['multi_pred'] = []
    for i in ids:
        predictions = get_predictions_from_std_id(i)[-1]
        kwargs['code_pred'].append(predictions['code_prediction'])
        kwargs['multi_pred'].append(predictions['multi_prediction'])
    return render_template('index.html', **kwargs)


@app.route('/student/<id>')
def student_data(id):
    kwargs = {}
    kwargs['id'] = id
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
