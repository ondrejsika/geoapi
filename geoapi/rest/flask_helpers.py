from functools import update_wrapper
from flask import  make_response

def access_controll_allow_all(f):
    def wrapper(*args, **kwargs):
        response = make_response(f(*args, **kwargs))
        response.headers['Access-Control-Allow-Origin'] = "*"
        response.headers['Access-Control-Allow-Methods'] = "*"
        response.headers['Access-Control-Allow-Headers'] = "*"
        return response
    f.provide_automatic_options = False
    return update_wrapper(wrapper, f)