__author__ = 'alexander'

import subprocess
import os

DEFAULTS = {
    "type_name": "rps",
    "value_type": "rps",
    "times": 200,
    "rps": 10,
    "concurrency": 1
}


def create_test_file(path, tests):
    file_name = "test.yaml"
    result_test = open(file_name, "w")
    result_test.write("---\n\n")
    for test in tests:
        values_to_put = {}
        if 'type_name' in test:
            values_to_put["type_name"] = test["type_name"]
            if test['type_name'] == 'constant':
                value_type = 'concurrency'
            else:
                value_type = 'rps'
        else:
            values_to_put["type_name"] = DEFAULTS["type_name"]
            value_type = DEFAULTS["value_type"]

        if 'times' in test:
            values_to_put["times"] = test["times"]
        else:
            values_to_put["times"] = DEFAULTS["times"]

        if value_type in test:
            values_to_put["type_param"] = value_type + ': ' + str(test[value_type])
        else:
            values_to_put["type_param"] = value_type + ': ' + str(DEFAULTS[value_type])
        sample_file_path = path + '/' + test["name"] + '.yaml'
        with open(sample_file_path) as sample_file:
            for line in sample_file:
                line = line.replace('$type_name', values_to_put["type_name"])
                line = line.replace('$times', str(values_to_put["times"]))
                line = line.replace('$type_param', values_to_put["type_param"])
                result_test.write(line)
        result_test.write("\n")
    result_test.close()
    return os.path.abspath(file_name)


def load_tests(file):
    config = {}
    execfile(file, config)
    tests = config['tests']
    return tests


def run_tests(file):
    subprocess.call(["rally", "--noverbose", "task", "start", file])