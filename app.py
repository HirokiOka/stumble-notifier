import os
from flask import Flask, render_template
from fetch_db import get_predictions_from_std_id, get_unique_ids, get_codeparams_from_std_id, get_codeparams_from_time

app = Flask(__name__)

stumble_seq_length = 60
p_data = [
        {"id": "2011234H", "code_stumble_states": [], "multi_stumble_states": []},
        {"id": "2061231H",  "code_stumble_states": [], "multi_stumble_states": []},
        {"id": "2140643H", "code_stumble_states": [], "multi_stumble_states": []},
        {"id": "2150505H", "code_stumble_states": [], "multi_stumble_states": []}
        ]
ids = []
for d in p_data:
    ids.append(d["id"])
ids.sort()

"""
def old_get_stumble_data():
    results = []
    for i, d in enumerate(p_data):
        try:
            print(d['id'])
            predictions = get_predictions_from_std_id(d["id"])[-1]
            print(predictions)
            d["code_stumble_states"].append(predictions['code_prediction'])
            d["multi_stumble_states"].append(predictions['multi_prediction'])
            current_states = []
            if ((len(d["code_stumble_states"]) - 1) > stumble_seq_length):
                current_states.append(is_stumble(d["code_stumble_states"]))
            if ((len(d["multi_stumble_states"]) - 1) > stumble_seq_length):
                current_states.append(is_stumble(d["multi_stumble_states"]))
            results.append(current_states)
        except:
            print(d["id"] + ': Prediction data not found')
    return results
"""

def is_stumble(state_queue, ratio=0.4):
    threshold = int(len(state_queue) * ratio)
    if (state_queue.count(0) > threshold):
        return False
    return True


@app.route('/')
def index():
    kwargs = {}
    kwargs["ids"] = ids
    return render_template("index.html", **kwargs)


@app.route('/student/<id>')
def student_data(id):
    kwargs = {}
    kwargs["id"] = id
    code_params = get_codeparams_from_std_id(id)
    kwargs["data"] = code_params
    return render_template("student_data.html", **kwargs)


@app.route('/student/<id>/<time>')
def source(id, time):
    saved_at = time.replace('_', '/')
    kwargs = {}
    kwargs["id"] = id
    kwargs["time"] = saved_at
    kwargs["code"] = get_codeparams_from_time(saved_at)["code"]
    return render_template('source.html', **kwargs)


@app.route('/data', methods=['GET'])
def get_stumble_data():
    results = []
    for i, d in enumerate(p_data):
        try:
            print(d["id"])
            predictions = get_predictions_from_std_id(d["id"])[-1]
            print(predictions)
            results.append([predictions['code_prediction'], predictions['multi_prediction']])
        except:
            results.append([0, 0])
            print(d["id"] + ': Prediction data not found')
    return results


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
    """
    app.run()
    """
