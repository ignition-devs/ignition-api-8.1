FROM coatldev/six:3.12 as devcontainer

COPY requirements /tmp/requirements/

# hadolint ignore=DL3042
RUN set -eux; \
    \
    python2 -m pip install --requirement \
        /tmp/requirements/dev.txt; \
    \
    python3 -m pip install --requirement \
        /tmp/requirements/build.txt

CMD ["/bin/bash"]
