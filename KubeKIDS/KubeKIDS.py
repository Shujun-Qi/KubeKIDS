from email.policy import default
import os

from flask import Flask
from flask import request

import requests
import rsa
from json import dumps as json_dumps
from random import getrandbits

app = Flask(__name__)

@app.route('/')
def HandleDH():
    enclaveID = request.args.get('enclaveid', default = -1, type = str)
    g = request.args.get('g',default = -1, type = int)
    p = request.args.get('p',default = -1, type = int)
    A = request.args.get('A',default = -1, type = int)
    
    privpath = f'/keyset/{enclaveID}/private.pem'
    pubpath = f'/keyset/{enclaveID}/public.pem'
    try:
        privf = open(privpath, 'r')
        pubf = open(pubpath, 'r')
    except IOError:
        return "Invalid enclave"
    
    privatekey = privf.read()
    privkey = rsa.PrivateKey.load_pkcs1(privatekey)
    
    publickey = pubf.read()

    methodParams = [enclaveID, publickey]
    payload_dict = {'principal': "mac6Mkn2BB0yZ4SHFakqSLf0FvtlwDtVQ0ellN5ibLo=",
                        'methodParams': methodParams}
    payload = json_dumps(payload_dict)
    headers = {'Content-Type': 'application/json',
                   'Accept-Charset': 'UTF-8'}
    r = requests.post('localhost:7777/postEnclavePublicKey',headers=headers,data=payload)
    
    msg = f'{g},{p},{A}'
    sigmsg = rsa.encrypt(msg,privkey)
    return f'{sigmsg}'
    