import json


def read_employee_json(filename):
    with open('./data/'+filename,'r',encoding='utf-8')as f:
        arr = []
        for data in json.load(f).values():
            arr.append(tuple(data.values()))

        return arr