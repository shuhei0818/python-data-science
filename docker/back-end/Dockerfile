FROM python:3.6-buster

ARG HTTP_PROXY
ARG HTTPS_PROXY

ENV WORKDIR /app/
WORKDIR ${WORKDIR}

COPY ./Pipfile* ${WORKDIR}

RUN pip install pipenv --no-cache-dir && \
    pipenv install --system --skip-lock

#RUN pip install pipenv --no-cache-dir && \
#    pipenv install --system --deploy