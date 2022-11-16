import logging

import azure.functions as func

from integral import integral

import json


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    integral_res = integral(0,3.1415).split('\n')
    integral_res_json = json.dumps(integral_res)

    return func.HttpResponse(integral_res_json, mimetype="text/json")
