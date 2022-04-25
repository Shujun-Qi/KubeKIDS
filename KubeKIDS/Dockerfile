from ubuntu:18.04

RUN mkdir /root/KubeKIDS

COPY KubeKIDS.py /root/KubeKIDS/
COPY KubeKIDS.sh /root/
COPY public.pem /root/KubeKIDS/
COPY private.pem /root/KubeKIDS

# VOLUME ["/imports"]
ENTRYPOINT ["/bin/bash", "/root/KubeKIDS.sh"]