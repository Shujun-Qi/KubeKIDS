from email.policy import default
import os


import requests
import rsa
from json import dumps as json_dumps
from random import getrandbits

enclaveID = "nafxpum0XMwwIMXV7rR1DXtlwhzzfaTz-3yXBGwJ27M="
g = 2
p=0xFFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD129024E088A67CC74020BBEA63B139B22514A08798E3404DDEF9519B3CD3A431B302B0A6DF25F14374FE1356D6D51C245E485B576625E7EC6F44C42E9A637ED6B0BFF5CB6F406B7EDEE386BFB5A899FA5AE9F24117C4B1FE649286651ECE45B3DC2007CB8A163BF0598DA48361C55D39A69163FA8FD24CF5F83655D23DCA3AD961C62F356208552BB9ED529077096966D670C354E4ABC9804F1746C08CA237327FFFFFFFFFFFFFFFF


def StartKeyExchange():
    a = getrandbits(32)
    A = pow(g, a, p)
    payload_dict = {'enclaveid': enclaveID, 'g': g, 'p': p, 'A':A}
    payload = json_dumps(payload_dict)
    headers = {'Content-Type': 'application/json',
                   'Accept-Charset': 'UTF-8'}
    r = requests.post('128.110.155.54:5000/',headers=headers,data=payload)
    r.json()
    sigmsg = r["data"]
    data_dict = {'enclaveid': enclaveID, 'sigmsg': sigmsg, 'g': g, 'p': p, 'A':A}
    data = json_dumps(data_dict)
    res = requests.post('128.110.155.76:5000/',headers=headers,data=data)
    res.json()
    res_data = res["data"]
    B, sigB = res_data.split(",")
    f = open("publickey.pem", 'r')
    publickey = f.read()
    pubkey = rsa.PublicKey.load_pkcs1(publickey)
    plainB = rsa.decrypt(sigB, pubkey)
    if B == int(plainB):
        K = pow(B, a, p)
    
StartKeyExchange()