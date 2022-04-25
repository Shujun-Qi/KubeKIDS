from ubuntu:18.04

RUN mkdir /root/enclave

COPY DHexchange.py /root/enclave/

COPY publickey.pem /root/enclave/

# VOLUME ["/imports"]
ENTRYPOINT ["/bin/bash", "/root/enclave/DHexchange.sh"]