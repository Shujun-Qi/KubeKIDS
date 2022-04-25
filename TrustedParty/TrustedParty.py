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
    sigmsg = request.args.get('signedmessage', default = -1, type = str)
    g = request.args.get('g',default = -1, type = int)
    p = request.args.get('p',default = -1, type = int)
    A = request.args.get('A',default = -1, type = int)
    methodParams = [enclaveID]
    payload_dict = {'principal': "mac6Mkn2BB0yZ4SHFakqSLf0FvtlwDtVQ0ellN5ibLo=",
                        'methodParams': methodParams}
    payload = json_dumps(payload_dict)
    headers = {'Content-Type': 'application/json',
                   'Accept-Charset': 'UTF-8'}
    r = requests.post('localhost:7777/checkEnclavePublicKey',headers=headers,data=payload)
    r.json()
    keystring = r["mac6Mkn2BB0yZ4SHFakqSLf0FvtlwDtVQ0ellN5ibLo="]["PublicKey"]
    pubkey = rsa.PublicKey.load_pkcs1(keystring)
    msg = rsa.decrypt(sigmsg, pubkey)
    msgg, msgp, msgA = msg.split(",")
    if g == int(msgg) and p == int(msgp) and A == int(msgA):
        b = getrandbits(32)
        B = pow(g, b, p)
        K = pow(A, b, p)
        f = open("privatekey.pem", 'r')
        privatekey = f.read()
        privkey = rsa.PrivateKey.load_pkcs1(privatekey)
        signedB = rsa.encrypt(B,privkey)
        return f'{B},{signedB}'
    else:
        
        return "Failed Attestation"
    