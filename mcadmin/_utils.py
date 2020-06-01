import json


def make_json(subprocess_output):
    return json.loads('[' + subprocess_output.decode('utf-8').strip('\n').replace('\n', ',') + ']')
