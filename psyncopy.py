import requests
from client import *

#TODO

def check(resp):
    if resp.status_code != 201:
        raise requests.APIException("Internal Server Error {}".format(resp.status_code) )
        return False
    return True
