# This function is not intended to be invoked directly. Instead it will be
# triggered by an HTTP starter function.
# Before running this sample, please:
# - create a Durable activity function (default name is "Hello")
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import logging
import json

import azure.functions as func
import azure.durable_functions as df


def orchestrator_function(context: df.DurableOrchestrationContext):
    
    
    data = yield context.call_activity("BlobStorage", "")
    
    mapped = []
    for line in data:
        mapped.append(context.call_activity("Mapper", line))

    result1 = yield context.task_all(mapped)
    result1 = [item for sublist in result1 for item in sublist]
   
    shuffled_dict = yield context.call_activity("Shuffler", result1)

    reduced = []
    for key in shuffled_dict.keys():
        res = context.call_activity("Reducer", [key, shuffled_dict[key]])
        reduced.append(res)

    result2 = yield context.task_all(reduced)
    
    return result2

main = df.Orchestrator.create(orchestrator_function)