from ubuntu:18.04

RUN mkdir /root/TrustedParty

COPY TrustedParty.py /root/TrustedParty/
COPY TrustedParty.sh /root/
COPY privatekey.pem /root/TrustedParty/

# VOLUME ["/imports"]
ENTRYPOINT ["/bin/bash", "/root/TrustedParty.sh"]