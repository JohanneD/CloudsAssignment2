# This function is not intended to be invoked directly. Instead it will be
# triggered by an orchestrator function.
# Before running this sample, please:
# - create a Durable orchestration function
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import logging


def main(keyvalue: list) -> tuple:
    sum = 0
    for c in keyvalue[1]:
        sum = sum + c
    return (keyvalue[0], sum)
