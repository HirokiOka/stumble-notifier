import pickle
import pandas as pd
import time
import datetime
from db_request import get_codeparams_from_std_id, post_all_data_from_id
from read_csv import read_latest_data, calc_pnn50

pnn50_window_size = 100
multi_model_bin_path = '../models/multi_model.pickle'
code_model_bin_path = '../models/code_model.pickle'


def calc_elapsed_sec(current_saved_at, last_saved_at):
    c_saved_date = ''
    last_saved_date = ''
    if ('AM' in current_saved_at or 'PM' in current_saved_at):
        current_saved_at = current_saved_at.split(' ')
        current_saved_at = current_saved_at[0].split(',')[0] + ' ' + current_saved_at[1]
        c_saved_date = datetime.datetime.strptime(current_saved_at, '%m/%d/%Y %H:%M:%S')
    else:
        c_saved_date = datetime.datetime.strptime(current_saved_at, '%Y/%m/%d %H:%M:%S')

    if ('AM' in last_saved_at or 'PM' in last_saved_at):
        last_saved_at = last_saved_at.split(' ')
        last_saved_at = last_saved_at[0].split(',')[0] + ' ' +  last_saved_at[1]
        last_saved_at = datetime.datetime.strptime(last_saved_at, '%m/%d/%Y %H:%M:%S')
    else:
        last_saved_at = datetime.datetime.strptime(last_saved_at, '%Y/%m/%d %H:%M:%S')

    elapsed_seconds = (c_saved_date - last_saved_date).seconds
    return elapsed_seconds


def make_feature_data(std_id, codeparams, elapsed_sec, rri_chunk, whs_params):
    sloc = codeparams['sloc']
    ted = codeparams['ted']

    lf_hf = whs_params['lf/hf']
    pnn50 = calc_pnn50(rri_chunk)

    feature_data = pd.DataFrame([[lf_hf, pnn50, sloc, ted, elapsed_sec]],
                columns=['lfhf', 'pnn50', 'sloc', 'ted', 'elapsed-seconds'])
    return feature_data


def main():
    start_time = datetime.datetime.now()
    multi_model = ''
    code_model = ''

    """
    p_info = [
            {"id": "2030848h", "whs_path": "../whs-data/test_1.csv", "rri_chunk": []},
            {"id": "2041201h", "whs_path": "../whs-data/test_2.csv", "rri_chunk": []},
            {"id": "2070877H", "whs_path": "../whs-data/test_3.csv", "rri_chunk": []},
            {"id": "2110645H", "whs_path": "../whs-data/test_4.csv", "rri_chunk": []},
            {"id": "2120823h", "whs_path": "../whs-data/test_5.csv", "rri_chunk": []},
            {"id": "2141064h", "whs_path": "../whs-data/test_6.csv", "rri_chunk": []},
            ]
    """

    whs_csv_paths = [
        "../whs-data/test_1.csv",
        "../whs-data/test_2.csv",
        "../whs-data/test_3.csv",
        "../whs-data/test_4.csv",
        "../whs-data/test_5.csv",
        "../whs-data/test_6.csv",
        ]
    rri_lists = [[], [], [], [], [], []]
    student_ids = ["2030848h", "2041201h", "2070877H", "2110645H", "2120823h", "2141064h"]

    with open(multi_model_bin_path, 'rb') as f:
        multi_model = pickle.load(f)
    with open(code_model_bin_path, 'rb') as f:
        code_model = pickle.load(f)

    while(True):
        # Get latest whs data
        whs_params = [[], [], [], [], [], []]
        for i, p in enumerate(whs_csv_paths):
            whs_params[i] = read_latest_data(p)

        # Stock RRI data
        for i, r in enumerate(rri_lists):
            r.append(whs_params[i]['rri'])

        # Prediction
        last_saved_ats = [[-1], [-1], [-1], [-1], [-1], [-1]]
        for i, sid in enumerate(student_ids):
            if (len(rri_lists[i]) > pnn50_window_size):
                # Get code params
                latest_codeparams = get_codeparams_from_std_id(sid)[-1]
                source_code = latest_codeparams['code']
                saved_at = latest_codeparams['savedAt']
                elapsed_sec = 0
                if (last_saved_ats[i][0] == -1):
                    elapsed_sec = (datetime.datetime.now() - start_time).seconds
                else:
                    elapsed_sec = calc_elapsed_sec(saved_at, last_saved_ats[i])
                current_feature_data = make_feature_data(sid,
                                                         latest_codeparams,
                                                         elapsed_sec,
                                                         rri_lists[i],
                                                         whs_params[i])
                multi_result = int(multi_model.predict(current_feature_data)[0])
                code_result = int(code_model.predict(current_feature_data.loc[:,
                                                 'sloc':'elapsed-seconds'])[0])

                feature_dict = current_feature_data.to_dict()
                print(current_feature_data, multi_result, code_result)
                print(post_all_data_from_id(sid, saved_at, source_code,
                      feature_dict, multi_result, code_result))

                last_saved_ats[i] = saved_at
                rri_lists[i].pop(0)
            else:
                print(str(i) + ": " + str(len(rri_lists[i])))
        time.sleep(0.1)


if __name__ == '__main__':
    main()
