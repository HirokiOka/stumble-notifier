import csv


def get_heart_data():
    csv_path = "./whs-data/test_1.csv"
    with open(csv_path, encoding='cp932', mode='r') as f:
        reader = list(csv.reader(f))[5:]
        data = reader[-1]
        result = {"time": data[0], "LF/LF": data[7]}
        return result
