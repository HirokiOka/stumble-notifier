import os
from flask import Flask, render_template, request
from db import connect_db, get_collection,\
        get_all_documents, get_latest_document,\
        get_latest_ten_documents, get_codeparams_from_time

app = Flask(__name__)


client = connect_db()
pp_coll = get_collection(client, "processed")
params_coll = get_collection(client, "codeparams")


@app.route('/')
def index():
    kwargs = {}
    unique_users = pp_coll.distinct("userName")
    unique_users.sort()
    kwargs["ids"] = unique_users
    return render_template("index.html", **kwargs)


@app.route('/student/<name>')
def student_data(name):
    kwargs = {}
    code_params = get_all_documents(client, params_coll, name)
    kwargs["id"] = name
    kwargs["data"] = code_params
    print(kwargs["data"])
    return render_template("student_data.html", **kwargs)


@app.route('/student/<name>/<time>')
def source(name, time):
    saved_at = time.replace('_', '/')
    kwargs = {}
    kwargs["id"] = name
    kwargs["time"] = saved_at
    codeparams = get_codeparams_from_time(client, params_coll,
                                          name, saved_at)
    kwargs["code"] = codeparams["code"]
    return render_template('source.html', **kwargs)


@app.route('/data', methods=['POST'])
def get_processed_data():
    payload = request.json
    names = payload.get('data')
    processed_results = []
    for name in names:
        processed_data = get_latest_ten_documents(pp_coll, name)
        mapped_data = [[x['processed_time'], x['multi'], x['code']] for x in processed_data]
        processed_results.append({'name': name, 'data': mapped_data})
    return processed_results


if __name__ == '__main__':
    """
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
    """
    app.run()
