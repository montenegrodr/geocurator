FROM python:3.6-alpine3.6
RUN  apk --no-cache add make

WORKDIR /srv

COPY geo_curator ./geo_curator
COPY setup.py Makefile requirements.txt customers.txt ./

RUN make build-python

ENTRYPOINT ["make", "run"]