FROM quay.io/ignition-devs/devcontainer-base:python

COPY ignition-api/requirements.txt /tmp/requirements.txt

# hadolint ignore=DL3042
RUN set -eux; \
    \
    python2 -m pip install --requirement \
        /tmp/requirements.txt; \
    rm -rf /tmp/*

CMD ["/bin/bash"]