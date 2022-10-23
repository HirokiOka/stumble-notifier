from flask import Flask, render_template
from fetch_db import get_predictions_from_std_id, get_unique_ids, get_codeparams_from_std_id, get_codeparams_from_time

app = Flask(__name__)

stumble_seq_length = 10
p_data = [
        {"id": "2070877H", "code_stumble_states": [], "multi_stumble_states": []},
        {"id": "2110645H", "code_stumble_states": [], "multi_stumble_states": []},
        {"id": "2120823h",  "code_stumble_states": [], "multi_stumble_states": []},
        {"id": "2141064h", "code_stumble_states": [], "multi_stumble_states": []},
        {"id": "oka", "code_stumble_states": [], "multi_stumble_states": []}
        ]
ids = []
for d in p_data:
    ids.append(d["id"])
ids.sort()
# ids = ["oka", "Matsui", "2070877H", "2110645H", "2120823h", "2141064h"]
# code_stumble_states = [[], [], [], [], [], []]
# multi_stumble_states = [[], [], [], [], [], []]


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
        predictions = get_predictions_from_std_id(d["id"])[-1]
        d["code_stumble_states"].append(predictions['code_prediction'])
        d["multi_stumble_states"].append(predictions['multi_prediction'])
        current_states = []
        if ((len(d["code_stumble_states"]) - 1) > stumble_seq_length):
            current_states.append(is_stumble(d["code_stumble_states"]))
        if ((len(d["multi_stumble_states"]) - 1) > stumble_seq_length):
            current_states.append(is_stumble(d["multi_stumble_states"]))
        results.append(current_states)
    return results


if __name__ == '__main__':
    app.run(debug=True, port=8000)
