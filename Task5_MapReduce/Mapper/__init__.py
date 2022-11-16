# This function is not intended to be invoked directly. Instead it will be
# triggered by an orchestrator function.
# Before running this sample, please:
# - create a Durable orchestration function
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import logging


def main(line: str) -> list:
    res = line.split()
    list_res = []
    for i in res:
        tup = tuple([i, 1])
        list_res.append(tup)
    return list_res




