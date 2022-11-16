# This function is not intended to be invoked directly. Instead it will be
# triggered by an orchestrator function.
# Before running this sample, please:
# - create a Durable orchestration function
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import logging

def main(pairs: list) -> dict:
    res = {}
    sorted_dict = {}
    for pair in pairs:
        if pair[0] in res.keys():
            res[pair[0].lower()].append(pair[1])
        else:
            res[pair[0].lower()] = [pair[1]]
    for key in sorted(res):
        sorted_dict[key] = res[key]

    return sorted_dict
